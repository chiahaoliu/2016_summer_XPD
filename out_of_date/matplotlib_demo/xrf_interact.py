# https://drive.google.com/open?id=0B5vxvuZBEEfTRGdXZ2NXUjNKUUk

import h5py
import matplotlib.gridspec as gridspec
import matplotlib.widgets as mwidgets
from matplotlib import path
import numpy as np


# uncomment this to set the backend
# import matplotlib
# matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt


class XRFInteract(object):
    def __init__(self, counts, positions, fig=None, pos_order=None,
                 norm=None):

        if pos_order is None:
            pos_order = {'x': 0,
                         'y': 1}

        self.x_pos = xpos = positions[pos_order['x']]
        self.y_pos = ypos = positions[pos_order['y']]
        self.points = np.transpose((xpos.ravel(), ypos.ravel()))
        if norm is None:
            norm = np.ones_like(self.x_pos)

        norm = np.atleast_3d(norm[:])

        # TODO do not normalize up from?
        self.counts = counts[:] / norm

        dx = np.diff(xpos.mean(axis=0)).mean()
        dy = np.diff(ypos.mean(axis=1)).mean()

        left = xpos[:, 0].mean() - dx/2
        right = xpos[:, -1].mean() + dx/2

        top = ypos[0].mean() - dy/2
        bot = ypos[-1].mean() + dy/2

        if fig is None:
            import matplotlib.pyplot as plt
            fig = plt.figure(tight_layout=True)
        fig.clf()
        fig.canvas.set_window_title('XRF map')
        self.fig = fig
        gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])

        self.ax_im = fig.add_subplot(gs[0, 0], gid='imgmap')
        self.ax_im.set_xlabel('x [?]')
        self.ax_im.set_ylabel('y [?]')

        self.ax_spec = fig.add_subplot(gs[1, 0], gid='spectrum')
        self.ax_spec.set_ylabel('counts [?]')
        self.ax_spec.set_xlabel('bin number')
        self.ax_spec.set_yscale('log')

        self._EROI_txt = self.ax_spec.annotate('ROI: all',
                                               xy=(0, 1),
                                               xytext=(0, 5),
                                               xycoords='axes fraction',
                                               textcoords='offset points')
        self._pixel_txt = self.ax_spec.annotate('map average',
                                                xy=(1, 1),
                                                xytext=(0, 5),
                                                xycoords='axes fraction',
                                                textcoords='offset points',
                                                ha='right')

        self.im = self.ax_im.imshow(self.counts[:, :, :].sum(axis=2),
                                    cmap='viridis',
                                    interpolation='nearest',
                                    extent=[left, right, bot, top]
                                    )

        self.xy_plt = self.ax_im.plot(xpos.ravel(), ypos.ravel(), 'wo',
                                      visible=False)

        self.cb = self.fig.colorbar(self.im, ax=self.ax_im)

        self.mask = np.ones(self.x_pos.shape, dtype='bool')
        self.mask_im = self.ax_im.imshow(self._make_overlay,
                                         interpolation='nearest',
                                         extent=[left, right, bot, top],
                                         zorder=self.im.get_zorder())

        # do not consider for mouseover text
        self.mask_im.mouseover = False
        self.spec, = self.ax_spec.plot(
            self.counts.mean(axis=(0, 1)),
            lw=2)

        self.cid = self.fig.canvas.mpl_connect('button_press_event',
                                               self._on_click)

        self.selector = mwidgets.SpanSelector(self.ax_spec,
                                              self._on_span,
                                              'horizontal',
                                              useblit=True, minspan=2,
                                              span_stays=True)
        self.lasso = None

    @property
    def _make_overlay(self):
        ret = np.zeros(self.mask.shape + (4,), dtype='uint8')
        if np.all(self.mask):
            return ret
        ret[:, :, 0] = 255
        ret[:, :, 3] = 100 * self.mask.astype('uint8')
        return ret

    def _on_click(self, event):
        # not in the right axes, bail
        ax = event.inaxes
        if ax is None or ax.get_gid() != 'imgmap':
            return

        if event.key == 'alt':
            return self._lasso_on_press(event)
        # not holding down shift, bail
        if event.key == 'shift':
            return self._pixel_select(event)

    def _reset_spectrum(self):
        self.mask = np.ones(self.x_pos.shape, dtype='bool')
        self.mask_im.set_data(self._make_overlay)
        new_y_data = self.counts.mean(axis=(0, 1))
        self.spec.set_ydata(new_y_data)
        self._pixel_txt.set_text('map average')

        self.fig.canvas.draw_idle()

    def _pixel_select(self, event):
        if event.button == 3:
            return self._reset_spectrum()

        x, y = event.xdata, event.ydata
        # get index by assuming even spacing
        # TODO use kdtree?
        diff = np.hypot((self.x_pos - x),  (self.y_pos - y))
        y_ind, x_ind = np.unravel_index(np.argmin(diff), diff.shape)

        # get the spectrum for this point
        new_y_data = self.counts[y_ind, x_ind, :]
        self.mask = np.zeros(self.x_pos.shape, dtype='bool')
        self.mask[y_ind, x_ind] = True
        self.mask_im.set_data(self._make_overlay)
        self._pixel_txt.set_text(
            'pixel: [{:d}, {:d}] ({:.3g}, {:.3g})'.format(
                x_ind, y_ind,
                self.x_pos[x_ind, y_ind],
                self.y_pos[x_ind, y_ind]))

        self.spec.set_ydata(new_y_data)

        self.fig.canvas.draw_idle()

    def _on_span(self, vmin, vmax):
        vmin, vmax = map(int, (vmin, vmax))
        new_image = self.counts[:, :, vmin:vmax].sum(axis=2)
        new_max = new_image.max()
        self._EROI_txt.set_text('ROI: {}:{}'.format(vmin, vmax))
        self.im.set_data(new_image)
        self.im.set_clim(0, new_max)
        self.fig.canvas.draw_idle()

    def _lasso_on_press(self, event):
        self.lasso = mwidgets.Lasso(event.inaxes, (event.xdata, event.ydata),
                                    self._lasso_call_back)

    def _lasso_call_back(self, verts):
        p = path.Path(verts)

        new_mask = p.contains_points(self.points).reshape(*self.x_pos.shape)
        self.mask = new_mask
        self.mask_im.set_data(self._make_overlay)
        new_y_data = self.counts[new_mask].mean(axis=0)
        self._pixel_txt.set_text('lasso mask')
        self.spec.set_ydata(new_y_data)

        self.fig.canvas.draw_idle()


fn = 'scan_3624.h5'
F = h5py.File(fn, 'r')
g = F['xrfmap']

xrf = XRFInteract(g['detsum']['counts'][:], g['positions']['pos'][:],
                  norm=g['scalers']['val'][:, :, 0])

# comment out this line to not use in 'interacitve' mode

plt.ion()
plt.show()

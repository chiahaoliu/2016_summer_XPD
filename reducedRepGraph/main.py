from plot_analysis import reducedRepPlot
from file import get_files

def main():
    u_input = input("please input the directory that contains your files: ")
    r_plt =  reducedRepPlot(get_files(u_input), 0, 2048, 0, 2048, min=True)
    r_plt.plot()

try:
    main()
except(AssertionError):
    print(str(AssertionError) + " \ncaused by incorrect x or y start stop vals.")
    print("x_start must be less than x_stop and the same goes for y")
except(FileNotFoundError):
    print(FileNotFoundError)
    print("incorrect path to image directory")
    print("path must lead to a folder with the images, not an image itself")
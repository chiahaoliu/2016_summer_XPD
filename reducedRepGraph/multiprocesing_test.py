import multiprocessing
from file import get_files
from tifffile import imread
file_dir = get_files("C:\\Users\\josep\\Documents\\GitHub\\BNL_BEAMLINE\\TIFF data\\Cu18Se\\cu18\\cooling\\")

arr_list = []
for i in range(0,50):
    arr_list.append(imread(file_dir[i]))

def test_fn(x):
    return x*x


def get_total_intensity(arr):
    total_intensity = 0
    for i in range(0, 2048):
        for j in range(0, 2048):
            total_intensity = arr[i][j]

    return total_intensity

def result(val):
    print("callback accessed")
    print(val)

if __name__ == '__main__':
    list = []
    pool = multiprocessing.Pool()
    p = pool.map_async(get_total_intensity, arr_list, callback=result)
    p.wait()



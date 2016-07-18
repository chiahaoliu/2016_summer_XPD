from plot_analysis import reducedRepPlot
from file import get_files

def main():
    u_input = input("please input the directory that contains your files: ")
    r_plt =  reducedRepPlot(get_files(u_input))

    r_plt.plot()

main()
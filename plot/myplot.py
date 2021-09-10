import numpy as np
import matplotlib.pyplot as plt

# this is a pure virtual class and will not function without implenting a subclass. 
class MyPlot:
    def __init__(self, xmin:float, xmax:float, ymin:float, ymax:float, nstep:int=128) -> None:
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.nstep = nstep
        self.x = np.linspace(xmin, xmax, num=nstep)
        self.y = np.linspace(ymin, ymax, num=nstep)
        self.x, self.y = np.meshgrid(self.x, self.y)


    def _calc_psi(self):
        return 0


    def _calc_phi(self):
        return 0


    def construct(self, title:str, psi_levels:int=10, show_phi:bool=False, phi_levels:int=10, xlabel:str="x", ylabel:str="y") -> None:
        __, ax1 = plt.subplots()
        ax1.contour(self.x, self.y, self.psi, levels=psi_levels, colors="k")
        if show_phi:
            ax1.contour(self.x, self.y, self.phi, levels=phi_levels, colors="r")

        ax1.set_title(title)
        ax1.set_aspect("equal")
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)
    

    def show(self) -> None:
        plt.show()

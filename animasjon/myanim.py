import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class MyAnimation:
    def __init__(self, style:str, xmin:float, xmax:float, ymin:float, ymax:float, nstep:int=128) -> None:
        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.ln, = plt.plot([], [], style)
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

        self.ani = FuncAnimation(self.fig, self.update, frames=np.linspace(xmin, xmax, nstep),
                            init_func=self.init, blit=True)


    def init(self):
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)
        return self.ln,

    
    def update(self, frame):
        self.xdata.append(frame)
        self.ydata.append(self.f(frame))
        self.ln.set_data(self.xdata, self.ydata)
        return self.ln,

    
    def show(self) -> None:
        plt.show()


    def f(self, frame):
        pass
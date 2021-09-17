from plot.myplot import MyPlot
from plot.myplot import MyPlot
import numpy as np
import matplotlib.pyplot as plt


class Oving3Elem(MyPlot):
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, nstep: int,
                    A: float, alpha: float) -> None:
        super().__init__(xmin, xmax, ymin, ymax, nstep=nstep)

        self.A = A
        self.alpha = alpha

        self.psi = self._calc_psi()


    def _calc_psi(self):
        return self.A * np.sqrt(self.x**2 + self.y**2)**self.alpha * np.sin(self.alpha*np.arctan2(self.y, self.x))
        # return self.x + self.y


def run_problem() -> None:
    alpha_values = [3, 2, 1.5, 1, 2/3, 0.5]
    A = 1
    for i in range(len(alpha_values)):
        this_plot = plt.figure(i)
        elem = Oving3Elem(-5, 5, -5, 5, 128, A, alpha_values[i])
        elem.construct(f"alpha={alpha_values[i]}")

    plt.show()




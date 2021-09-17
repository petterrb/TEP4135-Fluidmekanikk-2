import numpy as np
import matplotlib.pyplot as plt
# from plot import myplot as mplt
from plot.myplot import MyPlot

class SourceElem(MyPlot):
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, nstep: int,
                    q:float, a:float, b:float) -> None:
        
        super().__init__(xmin, xmax, ymin, ymax, nstep=nstep)

        self.q = q
        self.a = a
        self.b = b


        self.psi = self._calc_psi()
        self.phi = self._calc_phi()


    def _calc_psi(self) -> np.array:
        return (self.q/(2*np.pi))*np.arctan2(self.y-self.b, self.x-self.a)


    def _calc_phi(self) -> np.array:
        return (self.q/(2*np.pi))*np.log(np.sqrt((self.x-self.a)**2 + (self.y-self.b)**2))


class UniformFlow(MyPlot):
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, nstep: int,
                    u:float, v:float) -> None:
        
        super().__init__(xmin, xmax, ymin, ymax, nstep=nstep)
        
        self.u = u
        self.v = v


    def _calc_psi(self):
        return self.u * self.y - self.v * self.x


    def _calc_phi(self):
        return self.u * self.x + self.v * self.y


class RankineHalfBody(MyPlot):
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, nstep: int, 
                    u: float, v: float, q: float, a: float, b: float) -> None:
        
        super().__init__(xmin, xmax, ymin, ymax, nstep=nstep)

        self.uniform_element = UniformFlow(xmin, xmax, ymin, ymax, nstep, u, v)
        self.source_element  = SourceElem(xmin, xmax, ymin, ymax, nstep, q, a, b)

        self.psi = self._calc_psi()
        self.phi = self._calc_phi()

    def _calc_psi(self):
        return self.uniform_element._calc_psi() + self.source_element._calc_psi()

    # calculate potential function
    def _calc_phi(self):
        return self.uniform_element._calc_phi() + self.source_element._calc_phi()
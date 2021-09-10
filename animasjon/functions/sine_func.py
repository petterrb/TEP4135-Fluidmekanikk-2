from animasjon import myanim as ma
import numpy as np

class SineAnim(ma.MyAnimation):
    def f(self, frame):
        return np.sin(frame)
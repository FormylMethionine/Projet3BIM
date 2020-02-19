import numpy as np


class bacteria:

    def __init__(self, Pdivmax, Kx, Pdeath,  resist, tol):

        self.Pmax = Pdivmax
        self.Kx = Kx
        self.Pdeath = Pdeath
        self.resist = resist

    def divide(self, nutr):

        if np.random.random() < (self.Pmax*nutr)/(nutr+self.Kx):
            return True

        else:
            return False

    def death(self, C):

        if np.random.random() < Pdeath:
            return True
        
        else:
            return False
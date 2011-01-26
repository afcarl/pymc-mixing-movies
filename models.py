""" Discussion on the PyMC mailing list indicates many people are
having trouble getting Adaptive Metropolis step methods to work.
Let's have a look at what's going on.
"""

import pylab as pl
import pymc as mc
import graphics

# simple models for some uniformly distributed subsets of the plane
def diagonal():
    X = mc.Uniform('X', lower=-1., upper=1., value=[0., 0.])

    @mc.potential
    def near_diag(X=X):
        if abs(X[0] - X[1]) < .05:
            return 0
        else:
            return -pl.inf

    return mc.MCMC(vars())

def make_examples():
    m = diagonal()
    m.sample(3000)
    graphics.visualize_steps(m, 'diag_M.avi')

if __name__ == '__main__':
    m = diagonal()
    m.sample(1000)
    reload(graphics)
    graphics.visualize_single_step(m, 500, .5)
    pl.show()

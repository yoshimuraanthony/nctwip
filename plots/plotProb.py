import matplotlib.pyplot as plt
from inspect import stack

# dxs modules
from eIrrad.plotExciProb import NPlot

# constants, unit conversions, and dictionaries
from constants import *

def exciProbHBN(
        outfile='hBNPVsEb.png',
        gls = '--',
        els = '-',
        gco = 'gray',
        nmax = 10,
        N = 4,

        colormap = 'plasma',
        offset = -5,
        multiplier = 10,
        xlim = [0, 100],
        ylim = [0, 1],
        view = False,
        
        grid = False,
        transparent = False,
        legend = False,
        ):
    """Plots probabilities of n = 0 thru 4 excitations vs Eb."""
    name, ext = outfile.split('.')
    cmap = plt.get_cmap(colormap, 10*N)
    for m in range(N+1):
        plot = NPlot(forslides=True)
        plot.addProb(mat='hBN', n=0, nmax=nmax, linestyle=gls, xlim=xlim,
                color=gco)

        for n in range(1,m+1):
            plot.addProb(mat='hBN', n=n, linestyle=els, nmax=nmax,
                    xlim=xlim, color=cmap(multiplier*n + offset))

        plot.decorate(xlim=xlim, ylim=ylim, legend=legend, grid=grid)
        moutfile = f'{name}{m}.{ext}'
        plot.save(moutfile, transparent=transparent, writedate=False)
        plot.show()

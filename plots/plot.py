import matplotlib.pyplot as plt

# eIrrad modules
from eIrrad.plotScatter import ScatterPlot

# constants, unit conversions, and dictionaries
from constants import *

#-----------------------------------------------------------------------------
# scatter

PEdir = "/p/lustre1/yoshia/radEffects/materials/PE/qe/kCon/07x02x01"
PDMSdir = "/p/lustre1/yoshia/radEffects/materials/PDMS/qe/kCon/04x04x01"

pinfile = 'newprob.txt'
kinfile = 'kpts.txt'
PEpinfile = f'{PEdir}/{pinfile}'
PEkinfile = f'{PEdir}/{kinfile}'
PEexroot = f'{PEdir}/tmp/hBN.export'
PDMSpinfile = f'{PDMSdir}/{pinfile}'
PDMSkinfile = f'{PDMSdir}/{kinfile}'
PDMSexroot = f'{PDMSdir}/tmp/hBN.export'

def scatterDirPE(
        outfile = 'scatterDirPE.png',
        markersize = 2,
        title = 'Polyethylene (PE)',
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(transition='direct', color='tab:orange', markersize=markersize,
            label='direct', zorder=3)
    plot.plot(transition='indirect', color='tab:blue', markersize=markersize,
            label='indirect', zorder=2)
    plot.decorate(title=title, grid=False, legend=False,
            xlim=(0, 36), xticks=(0, 18, 36),
            ylim=(1e-19, 10), yticks=(1e-19, 1e-9, 10),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterDirPDMS(
        outfile = 'scatterDirPDMS.png',
        markersize = 2,
        title = 'Polydimethylsiloxane (PDMS)',
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(transition='direct', color='tab:orange', markersize=markersize,
            label='direct', zorder=3)
    plot.plot(transition='indirect', color='tab:blue', markersize=markersize,
            label='indirect', zorder=2)
    plot.decorate(title=title, grid=False, legend=False,
            xlim=(0, 30), xticks=(0, 15, 30),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterPE(
        outfile = 'scatterPE.png',
        markersize = 2,
        title = 'Polyethylene (PE)',
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(markersize=markersize)
    plot.decorate(title=title, grid=False, legend=False,
            xlim=(0, 36), xticks=(0, 18, 36),
#             xlim=(5, 35), xticks=(5, 20, 35),
#             xlim=(0, 36), xticks=(0, 6, 36),
            ylim=(1e-19, 10), yticks=(1e-19, 1e-9, 10),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterPDMS(
        outfile = 'scatterPDMS.png',
        markersize = 2,
        title = 'Polydimethylsiloxane (PDMS)',
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(markersize=markersize)
    plot.decorate(title=title, grid=False, legend=False,
            xlim=(0, 30), xticks=(0, 15, 30),
#             xlim=(4, 30), xticks=(4, 30),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scattermaxPE(
        outfile='scattermax.png',
        markersize=2,
        title='Polyethylene',
        maxlabel='direct band-edge\ntransition at X',
        ):
    """"""
    pass

def scattermaxPDMS(
        outfile='scattermax.png',
        markersize=2,
        title='Polydimethylsiloxane',
        maxlabel='direct band-edge\ntransition at S',
        ):
    """"""
    pass


# scatter
#-----------------------------------------------------------------------------
# dxs

# dxs
#-----------------------------------------------------------------------------

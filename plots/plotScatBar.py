import matplotlib.pyplot as plt
from inspect import stack

# eIrrad modules
from eIrrad.plotScatter import ScatterPlot
from eIrrad.plotBar import BarPlot

# constants, unit conversions, and dictionaries
from constants import *

#-----------------------------------------------------------------------------
# scatter

PEdir = "/p/lustre1/yoshia/radEffects/materials/PE/qe/kCon/07x02x01"
PDMSdir = "/p/lustre1/yoshia/radEffects/materials/PDMS/qe/kCon/04x04x01"
hBNdir = "/p/lustre1/yoshia/radEffects/materials/hBN/qe/Eb/050000/08x08x01"

pinfile = 'newprob.txt'
kinfile = 'kpts.txt'
PEpinfile = f'{PEdir}/{pinfile}'
PEkinfile = f'{PEdir}/{kinfile}'
PEexroot = f'{PEdir}/tmp/hBN.export'
PDMSpinfile = f'{PDMSdir}/{pinfile}'
PDMSkinfile = f'{PDMSdir}/{kinfile}'
PDMSexroot = f'{PDMSdir}/tmp/hBN.export'
hBNpinfile = f'{hBNdir}/{pinfile}'
hBNkinfile = f'{hBNdir}/{kinfile}'
hBNexroot = f'{hBNdir}/tmp/hBN.export'

def scatterHBN(
        outfile = 'auto',
        markersize = 2,
        ):
    """One color."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(forslides=True, clip_on=True, logy=True)
    plot.readData(pinfile=hBNpinfile, kinfile=hBNkinfile, top=hBNdir)
    plot.plot(transition='all', color='tab:blue', markersize=markersize,
            label='hBN', zorder=3)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 34), xticks=(0, 17, 34),
            ylim=(1e-19, 1e1), yticks=(1e-19, 1e-9, 1e1),
            ylabel='probability density ($\AA^6$)',
            )
    plot.save(outfile=outfile)
    plot.show()

def scatterZoomLinPEPDMS(
        outfile = 'auto',
        markersize = 10,
        ):
    """Two colors: PE and PDMS."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(forslides=True, clip_on=True, logy=False)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(transition='all', color='tab:blue', markersize=markersize,
            label='PE', zorder=3)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(transition='all', color='tab:orange', markersize=markersize,
            label='PDMS', zorder=2)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(4, 16), xticks=(4, 10, 16),
            ylim=(1, 20), yticks=(1, 10, 20),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterZoomPEPDMS(
        outfile = 'auto',
        markersize = 10,
        ):
    """Two colors: PE and PDMS."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(forslides=True, clip_on=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(transition='all', color='tab:blue', markersize=markersize,
            label='PE', zorder=3)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(transition='all', color='tab:orange', markersize=markersize,
            label='PDMS', zorder=2)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(4, 16), xticks=(4, 10, 16),
            ylim=(1, 1e2), yticks=(1, 10, 100),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterPEPDMS(
        outfile = 'auto',
        markersize = 2,
        ):
    """Two colors: PE and PDMS."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(transition='all', color='tab:blue', markersize=markersize,
            label='PE', zorder=3)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(transition='all', color='tab:green', markersize=markersize,
            label='PDMS', zorder=4)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 36), xticks=(0, 18, 36),
            ylim=(1e-18, 1e2), yticks=(1e-18, 1e-8, 1e2),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterDirPE(
        outfile = 'scatterDirPE.png',
        markersize = 2,
        ):
    """Two colors: direct and indirect."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(transition='direct', color='tab:orange', markersize=markersize,
            label='direct', zorder=3)
    plot.plot(transition='indirect', color='tab:blue', markersize=markersize,
            label='indirect', zorder=2)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 36), xticks=(0, 18, 36),
            ylim=(1e-19, 10), yticks=(1e-19, 1e-9, 10),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterDirPDMS(
        outfile = 'scatterDirPDMS.png',
        markersize = 2,
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(transition='direct', color='tab:orange', markersize=markersize,
            label='direct', zorder=3)
    plot.plot(transition='indirect', color='tab:blue', markersize=markersize,
            label='indirect', zorder=2)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 30), xticks=(0, 15, 30),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterPE(
        outfile = 'scatterPE.png',
        markersize = 2,
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(markersize=markersize)
    plot.decorate(title=None, grid=False, legend=False,
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
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(markersize=markersize)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 30), xticks=(0, 15, 30),
#             xlim=(4, 30), xticks=(4, 30),
            ylim=(1e-12, 1e2), yticks=(1e-12, 1e-5, 1e2),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterLinPE(
        outfile = 'scatterLinPE.png',
        markersize = 6,
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True, logy=False)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.plot(markersize=markersize)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 36), xticks=(0, 18, 36),
#             xlim=(5, 35), xticks=(5, 20, 35),
#             xlim=(0, 36), xticks=(0, 6, 36),
            ylim=(0, 10), yticks=(0, 5, 10),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scatterLinPDMS(
        outfile = 'scatterLinPDMS.png',
        markersize = 6,
        ):
    """One color, all points."""
    plot = ScatterPlot(forslides=True, logy=False)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(markersize=markersize)
    plot.decorate(title=None, grid=False, legend=False,
            xlim=(0, 30), xticks=(0, 15, 30),
            ylim=(0, 30), yticks=(0, 15, 30),
            ylabel='probability density ($\AA^6$)')
    plot.save(outfile=outfile)
    plot.show()

def scattermaxPE(
        outfile='scattermax.png',
        markersize=2,
        maxlabel='direct band-edge\ntransition at X',
        ):
    """"""
    pass

def scattermaxPDMS(
        outfile='scattermax.png',
        markersize=2,
        maxlabel='direct band-edge\ntransition at S',
        ):
    """"""
    pass


# scatter
#-----------------------------------------------------------------------------
# bar

def barPEPDMS(
        number = 5,
        outfile = 'auto',
        ):
    """Most likely transitions."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = BarPlot(forslides=True)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.addBars(mode='number', number=number, color='tab:green')
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.addBars(mode='number', number=number, color='tab:blue')
    plot.plot()
    plot.decorate(title=None)
    plot.save(outfile=outfile)
    plot.show()

def barPE(
        include = .01,
        outfile = 'auto',
        ):
    """Most likely transitions."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = BarPlot(forslides=True)
    plot.readData(pinfile=PEpinfile, kinfile=PEkinfile, top=PEdir)
    plot.addBars(include=include)
    plot.plot()
    plot.decorate()
    plot.save(outfile=outfile)
    plot.show()
        
def barPDMS(
        include = .01,
        outfile = 'auto',
        ):
    """Most likely transitions."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = BarPlot(forslides=True)
    plot.readData(pinfile=PDMSpinfile, kinfile=PDMSkinfile, top=PDMSdir)
    plot.plot(include=include)
    plot.decorate()
    plot.save(outfile=outfile)
    plot.show()

# bar
#-----------------------------------------------------------------------------

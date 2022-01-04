from numpy import arange
import matplotlib.pyplot as plt
from inspect import stack

# dxs modules
from dxs.plots import DXSPlot
from dxs.classes import *

# constants, unit conversions, and dictionaries
from constants import *

Ed_dict = {
        'CH': 4.28,  # 413 kJ/mol
        'CC': 3.61,  # 348 kJ/mol
        'hBN': 12.85,
        'MoS2': 6.92,
        }

Eg_dict = {
        'hBN': 4.17,
        'MoS2': 1.88,
        }

def dxsPEH(outfile='auto'):
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    plot = DXSPlot(forslides=True)
    plot.plot(spec='H', Ed=Ed_dict['CH'], ebounds=[1,100])
    plot.decorate(
            xlim=[1,100],
            )
    plot.save(outfile=outfile)
    plot.show()


def dxsHBN(ebounds=[20,320], Ed=12.85):
    """Writes four plots of B and N sputtering with(out) maxima labels."""
    # get maxima
    BStatDXS = StatDXS('B', Ed, ebounds)
    B_dict = BStatDXS.getDict()
    Bdxs_ar = B_dict['dxs_ar']
    Bdxsmax = Bdxs_ar.max()
    Beb_ar = B_dict['Eb_ar']
    Bebmax = Beb_ar[where(Bdxs_ar==Bdxsmax)][0]

    NStatDXS = StatDXS('N', Ed, ebounds)
    N_dict = NStatDXS.getDict()
    Ndxs_ar = N_dict['dxs_ar']
    Ndxsmax = Ndxs_ar.max()
    Neb_ar = N_dict['Eb_ar']
    Nebmax = Neb_ar[where(Ndxs_ar==Ndxsmax)][0]

    xticks = [Bebmax, Nebmax]
    yticks = [Bdxsmax, Ndxsmax]
    
    # no maxima
    Plot = DXSPlot(forslides=True, clip_on=False)
    Plot.plot(spec='B', Ed=Ed, ebounds=ebounds, label='boron')
    Plot.plot(spec='N', Ed=Ed, ebounds=ebounds, label='nitrogen')
    Plot.decorate(xlabel='beam energy', ylabel='cross section',
            xticks=[], yticks=[])
    Plot.ax.scatter(Bebmax, Bdxsmax, zorder=10)
    Plot.ax.scatter(Nebmax, Ndxsmax, zorder=10)
    Plot.save('dxsHBN.png', '.')
    Plot.show()

    # x maxima
    Plot = DXSPlot(forslides=True, clip_on=False)
    Plot.plot(spec='B', Ed=Ed, ebounds=ebounds, label='boron')
    Plot.plot(spec='N', Ed=Ed, ebounds=ebounds, label='nitrogen')
    Plot.decorate(ylabel='cross section', xticks=xticks, yticks=[])
    Plot.ax.plot([Bebmax, Bebmax], [0, Bdxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.plot([Nebmax, Nebmax], [0, Ndxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.scatter(Bebmax, Bdxsmax, zorder=10)
    Plot.ax.scatter(Nebmax, Ndxsmax, zorder=10)
    Plot.save('dxsHBN_xmax.png', '.')
    Plot.show()

    # y maxima
    Plot = DXSPlot(forslides=True, clip_on=False)
    Plot.plot(spec='B', Ed=Ed, ebounds=ebounds, label='boron')
    Plot.plot(spec='N', Ed=Ed, ebounds=ebounds, label='nitrogen')
    Plot.decorate(xlabel='beam energy', xticks=[], yticks=yticks)
    Plot.ax.plot([0, Bebmax], [Bdxsmax, Bdxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.plot([0, Nebmax], [Ndxsmax, Ndxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.scatter(Bebmax, Bdxsmax, zorder=10)
    Plot.ax.scatter(Nebmax, Ndxsmax, zorder=10)
    Plot.save('dxsHBN_ymax.png', '.')
    Plot.show()

    # both maxima
    Plot = DXSPlot(forslides=True, clip_on=False)
    Plot.plot(spec='B', Ed=Ed, ebounds=ebounds, label='boron')
    Plot.plot(spec='N', Ed=Ed, ebounds=ebounds, label='nitrogen')
    Plot.decorate(xticks=xticks, yticks=yticks)
    Plot.ax.plot([Bebmax, Bebmax], [0, Bdxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.plot([Nebmax, Nebmax], [0, Ndxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.plot([0, Bebmax], [Bdxsmax, Bdxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.plot([0, Nebmax], [Ndxsmax, Ndxsmax], lw=.5, c='gray', zorder=-10)
    Plot.ax.scatter(Bebmax, Bdxsmax, zorder=10)
    Plot.ax.scatter(Nebmax, Ndxsmax, zorder=10)
    Plot.save('dxsHBN_xymax.png', '.')
    Plot.show()


def dxsContr(
        outfile = 'dxsContr.png',
        res = 100,
        ):
    """Plots contribution of each excitation to the total DXS."""
    name, ext = outfile.split('.')
    e_tdxs = ExciDXS(spec='B', Ed=12.85, ebounds=[20,120], res=res, tau=500,
            Ni=5)
    e_dict = e_tdxs.getDict()
    Eb_ar = e_dict['Eb_ar']
    dxs_a2 = e_dict['dxs_a2'].T
    totdxs_ar = e_dict['dxs_ar']

    N, _ = dxs_a2.shape
    cmap = plt.get_cmap('plasma', 10*(N-1))
    color_list = []
    for n in range(1, N):
        color=cmap(10*n - 5)
        color_list.append(color)

    # just the contributions
    for m in range(N):
        Plot = DXSPlot(forslides=True, clip_on=False)
        Plot.ax.plot(Eb_ar, dxs_a2[0], lw=2, color='gray', ls='dashed',
                clip_on=False)

        for n, dxs_ar, color in zip(range(m), dxs_a2[1:], color_list):
            Plot.ax.plot(Eb_ar, dxs_ar, lw=2, color=color, clip_on=False)

        Plot.decorate(xticks=[20,120], yticks=[0,40], ylim=[0,40])
        moutfile = f'{name}{m}.{ext}'
        Plot.save(moutfile)
        Plot.show()
    
    # show total
    Plot = DXSPlot(forslides=True, clip_on=False)
    Plot.ax.plot(Eb_ar, dxs_a2[0], lw=2, color='gray', ls='dashed')
    for n, dxs_ar, color in zip(range(N), dxs_a2[1:], color_list):
        Plot.ax.plot(Eb_ar, dxs_ar, lw=2, color=color, clip_on=False)

    Plot.ax.plot(Eb_ar, totdxs_ar, lw=2, color='white')
    Plot.decorate(xticks=[20,120], yticks=[0,40], ylim=[0,40])
    toutfile = f'{name}Tot.{ext}'
    Plot.save(toutfile)
    Plot.show()


def dxsExpHBN(
        outfile = 'auto',
        res = 100,
        ylim = [0,40],
        ):
    """Plots excited and ground state hBN dxs with expimerntal points."""
    if outfile=='auto':
        outfile = f'{stack()[0].function}.png'
    print(f'saving to {outfile}')

    g_tdxs = TempDXS(spec='B', Ed=12.85, ebounds=[20,120])
    g_dict = g_tdxs.getDict()
    e_tdxs = ExciDXS(spec='B', Ed=12.85, ebounds=[21,120], res=res, tau=500)
    e_dict = e_tdxs.getDict()

    # expt data
    Plot = DXSPlot(forslides=True, clip_on=False)
    Plot.plot(dxs_dict=g_dict)
    Plot.plot(dxs_dict=e_dict)
    Plot.ax.plot((30, 60, 60), (15, 18, 15), 's', color='white', markersize=7)
    Plot.decorate(xticks=[20, 120], yticks=ylim, ylim=ylim)
    Plot.save(outfile)
    Plot.show()

#---------------------------------- SCRATCH ----------------------------------

# def dxsPEC(outfile='auto'):
#     if outfile=='auto':
#         outfile = f'{stack()[0].function}.png'
#     print(f'saving to {outfile}')
# 
#     plot = DXSPlot(forslides=True)
#     plot.plot(spec='H', Ed=Ed_dict['CH'], ebounds=[1,100])
#     plot.decorate(
#             xlim=[1,100],
#             )
#     plot.save(outfile=outfile)
#     plot.show()


#     e_tdxs = ExciDXS(spec='B', Ed=12.85, ebounds=[20,120], res=40, tau=1000)
#     e_dict = e_tdxs.getDict()

#     Plot.ax.plot((30, 60, 60), (21.46, 33.66, 20.44), 's', color='white',
#             markersize=7)

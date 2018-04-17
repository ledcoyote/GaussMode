# appGaussMode.py
# Application for fitting a Gaussian mode to an intensity image from a beam
# profiling camera.
# Charlie J Keith 2018

from threading import Thread
from matplotlib.pyplot import imread
from numpy import zeros
from traits.api import HasTraits, Instance, String, Button, Array
from traitsui.api import Item, View, Group
from chaco.api import ArrayPlotData, Plot, gray
from enable.api import ComponentEditor
from optimize import hc_optimize

class OptimizerThread(Thread):
    def run(self):
        self.out_data.string = 'working...'
        
        initial_guess = [160, 128, 20, 10, 0]  # start at center of image, fairly small beam, 0 degree rotation
        mo_max, p = hc_optimize(self.im_data, initial_guess)
        self.out_data.string = 'Final Result:\nOverlap Integral = '+str(mo_max)+'\nParameters = '+str(p)

class OutputTextBox(HasTraits):
    string = String()
    view = View(Item('string',show_label=False,springy=True, style='custom'))

class PlotArea(HasTraits):

    filename = String()
    load_button = Button(label='Go!')
    im_data = Array()
    plot_area = Instance(Plot)
    out_data = Instance(OutputTextBox,())
    optimizer_thread = Instance(OptimizerThread)

    view = View(
                Group(
                    Item('filename',show_label=True,height=12),
                    Item('load_button',show_label=True),
                    Item('plot_area', editor=ComponentEditor(),show_label=False,
                        width=640, height=512),
                    'out_data',
                    orientation='vertical',style='custom'),
            resizable=True, title='appGaussMode')

    def _plot_area_default(self):
        im_data = zeros([256,320])
        self.plotdata = ArrayPlotData(imagedata=im_data)

        plot_area = Plot(self.plotdata)
        self.renderer = plot_area.img_plot('imagedata', colormap=gray)
        return plot_area

    def _load_button_fired(self):
        idata = imread(self.filename)
        self.im_data = idata
        self.plotdata.set_data('imagedata',self.im_data)
        
        if (not self.optimizer_thread) or (not self.optimizer_thread.isAlive()):
            self.optimizer_thread = OptimizerThread()
            self.optimizer_thread.im_data = self.im_data
            self.optimizer_thread.out_data = self.out_data
            self.optimizer_thread.start()

if __name__ == '__main__':
    PlotArea().configure_traits()


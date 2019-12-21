import numpy
import matplotlib.pyplot as pyplot


x_values = numpy.arange(0, 10, 0.05)

func1 = lambda x: 1/((x+2)**2)
func2 = lambda x: 0 if x<3 else 1 
func3 = lambda x: x if x<5 else 5*numpy.exp(-x+5)
func4 = lambda x: numpy.arctan(x)

functions = [func1, func2, func3, func4]
colors = ['k', 'r', "#009933", (51/255, 153/255, 1)] # black, red, green in hexadecimal, blue in RGB

# Creating a 2x2 grid of figures in subfig_array
# fig contains the global figure object(i.e. size of the window)
fig, subfig_array = pyplot.subplots(2,2,sharex=True)

# giving a function and a color to each subfigure
for subfig, func, color in zip(subfig_array.flatten(), functions, colors):
    y_values = list(map(func, x_values))

    subfig.tick_params(labelsize=11)
    subfig.set_xlabel(r"Parameter $r$", size=12)
    subfig.plot(x_values, y_values, color=color)

pyplot.tight_layout()
pyplot.show()

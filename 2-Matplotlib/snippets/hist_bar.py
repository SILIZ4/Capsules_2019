import numpy
import matplotlib.pyplot as pyplot


data = numpy.random.normal(0, 4, size=200)

pyplot.hist(data, bins=20)
pyplot.show()

occurence = [1, 4, 3, 1]
pyplot.bar([1, 2, 3, 4], occurence)
pyplot.show()

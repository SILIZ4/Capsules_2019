import numpy
import matplotlib.pyplot as pyplot


def curve(x):
    return numpy.sin(x)

# Crée matrice de 0 jusqu'à 6 avec un espacement de 0.1 (6 est exclu)
x_values = numpy.arange(0, 6, 0.1) 
# Applique la fonction sur tous les éléments de x_values et 
# les mets dans une liste
y_values = list(map(curve, x_values)) 

pyplot.plot(x_values, y_values)
pyplot.scatter(x_values, y_values)
pyplot.show()

import matplotlib.pyplot as mb
import random
r=500
d= range(r)
dr= [random.uniform(-1,1) for i in d]
mb.plot(d,dr, '+')
mb.show()

from solucio_funcions import iteracions_MCD_Euclides
import matplotlib.pyplot as plt

x = []
y = []
z = []

num = 10

for i in range(1, num+1):
    for j in range(1, num+1):
        x.append(i)
        y.append(j)
        z.append(iteracions_MCD_Euclides(i,j))

plt.scatter(x, y, c=z)
plt.colorbar()
plt.show()

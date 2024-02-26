x1 = int(input(""))
z1 = int(input(""))
dh = float()
dk = float()
ds = float()
dh = (((x1 - 34)**2 + (z1 - 220)**2))**(1/2)
h = dh
dk = (((x1 - 0)**2 + (z1 - 0)**2))**(1/2)
k = dk
ds = (((x1 - 140)**2 + (z1 - 456)**2))**(1/2)
s = ds
print("Distancia para Hogsmeade: %.2f" % h)
print("Distancia para Kakariko: %.2f" % k)
print("Distancia para Solitude: %.2f" % s)
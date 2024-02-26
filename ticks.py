d = int(input(""))
c = int(input(""))
d = ((d*24) - (d*21))
ticks = ((20*60*60)*d)/2
t = int(ticks/c)
print(t)
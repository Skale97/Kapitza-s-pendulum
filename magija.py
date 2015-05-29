import numpy as np
import matplotlib.pyplot as plt

n = 5000
g = 10
l = 1
a = 0.1
dt = 0.001
fip = []
fip.append(3.14+0.1)
vfi = []
vfi.append(0)
afi = 0
w = []
maxfi = []
maxfinb = []
for j in range(0, 122):
	w.append(j*2*3.14/10)
	fip = []
	fip.append(3.14+0.1)
	vfi = []
	vfi.append(0)
	for i in range(0, n):
		afi = -(g+a*w[j]*w[j]*np.cos(w[j]*i*dt))*np.sin(fip[i])/l
		vfi.append(vfi[i]+afi*dt)
		fip.append(fip[i]+vfi[i+1]*dt)
		afi = 0
	maxfinb.append(np.max(fip))
	if(np.max(fip) > 3*3.14/2):
		maxfi.append(1)
	else:
		maxfi.append(0)
	print(j)
	

plt.figure(1)
plt.plot(fip)
plt.figure(2)
plt.plot(w, maxfi)
plt.plot(w, maxfinb, '--r')
plt.show()


fo = open("foo.txt", "wb")
for i in range(0, n):
	fo.write(str(fip[i])+"\n")
fo.close()
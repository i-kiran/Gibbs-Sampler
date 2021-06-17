import math
import random
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure as fig
import seaborn as sns
no_iter = 10000 
miu = [1,2]
#a = 0
print("\n please enter one of these values for a ( 0 or  0.99) : ")
a = input()
a = float(a)
sigma = [[1,a],[a,1]]
def gibbs(miu , sigma):
	y = miu[1]
	g_samples = []
	for i in range(no_iter):
		sigma1 = sigma[0][0] - sigma[1][0] / sigma[1][1] * sigma[1][0]
		miu1 = miu[0] + sigma[1][0] / sigma[0][0] * (y-miu[1]) 
		x = np.random.normal(miu1 , sigma1)
		sigma2 = sigma[1][1] - sigma[0][1] / sigma[0][0] * sigma[0][1]
		miu2 = miu[1] + sigma[0][1] / sigma[1][1] * (x - miu[0])
		y = np.random.normal(miu2 , sigma2)

		r = [x , y]
		g_samples.append(r)

	return g_samples

result = gibbs(miu , sigma)
#print("Estimated values o : ")
#print(result[:5])
list1= []
list2 = []
for i in result:
	a,b = i
	list1.append(a)
	list2.append(b)

miu_ = np.mean(result)
print("Estimated miu  : ",miu_)
sigma_ = np.cov(result)
print("Estimated sigma: ", sigma_)


#traceplot 
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(3)
plt.title('Traceplot before burn')
plt.ylabel('parameters ')
plt.xlabel('time')
plt.plot(list1 , label = 'miu')
plt.plot(list2 ,  label = 'sigma')
plt.legend()
plt.show()

#traceplot after burn
if(a==0):
	burn = 200
else:
	burn = 500
x = list1
x = x[burn:]
y = list2
y= y[burn:]
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(3)
plt.title('Traceplot after burn')
plt.ylabel('parameters ')
plt.xlabel('time')
plt.plot(x , label = 'miu')
plt.plot(y ,  label = 'sigma')
plt.legend()
plt.show()

#1st histogram to show miu trends after burnt values 
fig, ax = plt.subplots(figsize =(8, 6))
ax.hist(x, alpha=0.5, histtype='bar', ec='black')
plt.ylabel('time')
plt.xlabel('miu')
plt.show()
#2nd histogram to show miu2 trends after burnt values
fig, ax = plt.subplots(figsize =(8, 6))
ax.hist(y, alpha=0.5, histtype='bar', ec='black')
plt.ylabel('time')
plt.xlabel('sigma')
plt.show()


#plotting samples x1 and x2
plt.title('X1 vs X2 samples after burn')
synth_plot = plt.plot(x, y, "+")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

import time
import numpy as np
import matplotlib.pyplot as plt
import convexhull as ch


P = np.random.normal(loc=0,scale=2,size=(50,2))
# P = np.loadtxt('data_sample.csv', delimiter=',', comments='#')
plt.scatter(P[:,0], P[:,1], c='gray', s=10)

start = time.time()
# L = ch.SlowConvexHull(P)
L = ch.ConvexHull(P)
end = time.time()
print('elapsed time:{0}'.format(end-start))
plt.scatter(L[:,0], L[:,1], c='red', s=20)

plt.plot(L[:,0], L[:,1], c='red') # draw convex hull
plt.plot([L[0,0],L[-1,0]],[L[0,1],L[-1,1]],c='red',linestyle='dashed') # connect between start and end

# plt.xlim(-7,7)
# plt.ylim(-7,7)
plt.show()
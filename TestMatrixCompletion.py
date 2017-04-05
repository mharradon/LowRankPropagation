import Rank1MatrixCompletion as mc
import numpy as np
import matplotlib.pyplot as plt

# Random Sampling
# Make an NxN rank-1 matrix
N = 100
sampleRate = 0.1
A = np.dot(np.random.randn(N,1),np.random.randn(1,N))
# Make mask with random sampling
mask = np.less(np.random.rand(N,N),sampleRate)
# Zero out matrix where mask is 0
A[np.logical_not(mask)] = 0

f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
ax1.imshow(A, interpolation="nearest")
ax2.imshow(mask, interpolation="nearest")
plt.show()

[AOut,maskOut] = mc.completeRank1Matrix(np.copy(A),np.copy(mask),True)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)
ax1.imshow(A, interpolation="nearest", vmin=-3, vmax=3)
ax3.imshow(mask, interpolation="nearest", vmin=-3, vmax=3)
ax2.imshow(AOut, interpolation="nearest", vmin=-3, vmax=3)
ax4.imshow(maskOut, interpolation="nearest", vmin=-3, vmax=3)
plt.show()


# Banded Diagonal Sampling
# Make an NxN rank-1 matrix
N = 50
sampleRate = 0.1
A = np.dot(np.random.randn(N,1),np.random.randn(1,N))
# Make mask with random sampling
mask = np.logical_or(np.diag(np.ones(N,dtype=bool)),np.diag(np.ones(N-1,dtype=bool),k=1))
# Zero out matrix where mask is 0
A[np.logical_not(mask)] = 0

f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
ax1.imshow(A, interpolation="nearest")
ax2.imshow(mask, interpolation="nearest")
plt.show()

[AOut,maskOut] = mc.completeRank1Matrix(np.copy(A),np.copy(mask),True)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)
ax1.imshow(A, interpolation="nearest", vmin=-3, vmax=3)
ax3.imshow(mask, interpolation="nearest", vmin=-3, vmax=3)
ax2.imshow(AOut, interpolation="nearest", vmin=-3, vmax=3)
ax4.imshow(maskOut, interpolation="nearest", vmin=-3, vmax=3)
plt.show()

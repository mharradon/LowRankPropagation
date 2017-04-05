import numpy as np
import matplotlib.pyplot as plt
import time

def completeRank1Matrix(observations,mask,PLOT=False):
  # observations and mask are two 2D numpy arrays of the same size, where observations is a
  # numerical matrix indicating the observed values of the matrix and mask is a boolean array
  # indicating where observations occur.

  if PLOT:
    f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    f.show()

  done = False
  while(done == False):
    
    # Identify nodes that have paths of length 3 between them and not paths of length 1
    maskInt = mask.astype(int)
    Q = np.logical_and(np.logical_not(mask),
                       np.greater(np.dot(np.dot(maskInt, np.transpose(maskInt)),maskInt),0))
    if not np.any(Q):
      done = True
      continue

    # For each entry in Q solve for new node
    solvable = np.argwhere(Q)
    for fillPt in solvable:
      # Need to find a length 3 path from the row to the column corresponding to entry.
      # A simple approach is to traverse a single edge from a given row and column and then test
      # if they are connected.
      rowConnected = np.argwhere(mask[fillPt[0],:])
      columnConnected = np.argwhere(mask[:,fillPt[1]])
      pathFound = False
      for j in rowConnected:
        for i in columnConnected:
          if mask[i,j]:
            pathFound = True
            break
        if pathFound:
          break

      # pdb.set_trace()
      assert(mask[i,fillPt[1]] and mask[fillPt[0],j] and mask[i,j] and not mask[fillPt[0],fillPt[1]])
      # We now have two points that are "diagonal" in the square
      observations[fillPt[0],fillPt[1]] = observations[i,fillPt[1]]*observations[fillPt[0],j]/observations[i,j]
      mask[fillPt[0],fillPt[1]] = True
    
    if PLOT:
      ax1.imshow(observations, interpolation="nearest")
      ax2.imshow(mask, interpolation="nearest")
      f.canvas.draw()
      time.sleep(0.5)

  plt.close(f)
  return [observations,mask]

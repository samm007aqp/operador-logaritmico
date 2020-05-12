import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('log_6.jpg')
output = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
row,cols = output.shape
total = row*cols
   

for i in range (row):
    for j in range(cols):
        output[i][j] = 100*math.log(1 + output[i][j],10)
        


cv2.imwrite('salida_log_6.jpg',output)
cv2.imshow('img',img)
cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(output.ravel(),256,[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show






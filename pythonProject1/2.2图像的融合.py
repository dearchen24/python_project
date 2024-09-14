import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('./image/cat.jpg')
img2=cv2.imread('./image/dog.jpg')
img3=cv2.resize(img2,(500,414))
img4=cv2.addWeighted(img1,0.7,img3,0.5,0)
img5=cv2.add(img1,img3)


# cv2.imshow('cat',img1)
# cv2.imshow('dog',img2)
# cv2.imshow('addWeighted',img4)
# cv2.imshow('add',img5)

plt.figure(figsize=(10,5))
plt.subplot(2,2,1),plt.title("cat"),plt.imshow(img1)
plt.subplot(2,2,2),plt.title("dog"),plt.imshow(img2)
plt.subplot(2,2,3),plt.title("addWeighted"),plt.imshow(img3)
plt.subplot(2,2,4),plt.title("add"),plt.imshow(img4)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
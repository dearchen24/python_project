# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# def passImg():
#     img=cv2.imread('./image/cat.jpg',0)
#     h,w=img.shape
#     #生成一个密码，加密
#     key_img=np.random.randint(0,256,size=(h,w),dtype=np.uint8)
#     img_addm=cv2.bitwise_xor(img,key_img)
#     print(key_img.shape,img.shape)
#     #解密
#     img_jm=cv2.bitwise_xor(key_img,img_addm)
#     plt.figure(figsize=(10, 7))
#     plt.subplot(2, 2, 1), plt.title("cat"), plt.imshow(img)
#     plt.subplot(2, 2, 2), plt.title("key"), plt.imshow(key_img)
#     plt.subplot(2, 2, 3), plt.title("addom"), plt.imshow(img_addm)
#     plt.subplot(2, 2, 4), plt.title("jiemi"), plt.imshow(img_jm)
#
#
#     plt.show()
#
# if __name__ == '__main__':
#     passImg()

import cv2
import numpy as np
import matplotlib.pyplot as plt


def passImg():
    img = cv2.imread('./image/cat.jpg', 1)  # 以彩色模式读取
    h, w, _ = img.shape
    # 生成一个密码，加密
    key_img = np.random.randint(0, 256, size=(h, w, 3), dtype=np.uint8)  # 生成彩色密码
    img_addm = cv2.bitwise_xor(img, key_img)
    # 解密
    img_jm = cv2.bitwise_xor(key_img, img_addm)

    plt.figure(figsize=(10, 7))
    plt.subplot(2, 2, 1), plt.title("cat"), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.subplot(2, 2, 2), plt.title("key"), plt.imshow(cv2.cvtColor(key_img, cv2.COLOR_BGR2RGB))
    plt.subplot(2, 2, 3), plt.title("addom"), plt.imshow(cv2.cvtColor(img_addm, cv2.COLOR_BGR2RGB))
    plt.subplot(2, 2, 4), plt.title("jiemi"), plt.imshow(cv2.cvtColor(img_jm, cv2.COLOR_BGR2RGB))

    plt.show()


if __name__ == '__main__':
    passImg()

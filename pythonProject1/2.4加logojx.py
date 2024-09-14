import cv2
import matplotlib.pyplot as plt
def imgLogo():

    #1,处理 log
    #对 LOGO 进行灰度化处理，得到两个 MASK
    img_logo=cv2.imread("./image/zgb.jpg")
    img_logo_gray=cv2.cvtColor(img_logo,cv2.COLOR_BGR2GRAY)
    #二值化转换为 0,255
    ret,img_logo_mask=cv2.threshold(img_logo_gray,200,255,cv2.THRESH_BINARY)
    img_logo_mask1=cv2.bitwise_not(img_logo_mask)
    cv2.imshow("img_logo", img_logo)
    cv2.imshow("img_logo_gray", img_logo_gray)
    cv2.imshow("img_logo_mask", img_logo_mask)
    #2,处理目标图像的 ROI
    img_target=cv2.imread("./image/jfj.jpg")
    rows,cols,channel=img_logo.shape
    rows1, cols1, channel1 = img_target.shape
    img_roi = img_target[:rows, cols1 - cols:cols1].copy()
    cv2.imshow("img_roi", img_roi)
    #3,合并 ROI 和 logo
    img_res0 = cv2.bitwise_and(img_roi, img_roi, mask=img_logo_mask)
    cv2.imshow("img_res0", img_res0)
    img_res1 = cv2.bitwise_and(img_logo, img_logo, mask=img_logo_mask1)
    cv2.imshow("img_res1", img_res1)
    img_res2 = cv2.add(img_res0, img_res1)
    cv2.imshow("img_res2", img_res2)
    img_target[:rows, cols1 - cols:cols1] = img_res2[:, :]
    cv2.imshow("img_final", img_target)
    cv2.waitKeyEx(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    imgLogo()
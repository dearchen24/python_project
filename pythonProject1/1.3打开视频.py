import cv2
import os
# 打开视频文件
# cap = cv2.VideoCapture('./image/test.mp4')
#
# # 检查视频文件是否成功打开
# if not cap.isOpened():
#     print("错误: 无法打开视频文件。")
# else:
#     while True:
#         # 读取一帧
#         ret, frame = cap.read()
#
#         # 如果成功读取帧
#         if ret:
#             # 显示帧
#             cv2.imshow('Video Frame', frame)
#
#             # 等待10毫秒，如果按下 'q' 键则退出
#             if cv2.waitKey(10) & 0xFF == ord('q'):
#                 break
#         else:
#             # 如果到达视频末尾，则重新开始
#             cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#
#     # 释放视频捕捉对象，并关闭所有OpenCV窗口
#     cap.release()
#     cv2.destroyAllWindows()

# if not cap.isOpened():
#     print("错误: 无法打开视频文件。")
#     exit()
#
# while True:
#     open,frame = cap.read()
#     if not open:
#         break
#         #显示帧
#     cv2.imshow('cap',frame)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


cap=cv2.VideoCapture(0)
# 定一个输出值
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('./image/cap.avi',fourcc,20.0,(640,480))

if not cap.isOpened():
    print("打开摄像头失败")
    exit()
while(True):
    open,frame=cap.read()
    if not open:
        break
    # 通过输出器保存视频
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(50) &0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




# 创建保存图片的目录
# output_dir = './images'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# # 打开摄像头
# cap = cv2.VideoCapture(0)
#
# # 检查摄像头是否成功打开
# if not cap.isOpened():
#     print("打开摄像头失败")
#     exit()
#
# frame_count = 0
# while True:
#     # 读取一帧
#     ret, frame = cap.read()
#
#     # 检查是否成功读取帧
#     if not ret:
#         print("读取帧失败")
#         break
#
#     # 保存每一帧为图片
#     img_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
#     cv2.imwrite(img_filename, frame)
#
#     # 显示帧
#     cv2.imshow('frame', frame)
#
#     # 按下 'q' 键退出循环
#     if cv2.waitKey(50) & 0xFF == ord('q'):
#         break
#
#     frame_count += 1
#
# # 释放摄像头
# cap.release()
#
# # 关闭所有OpenCV窗口
# cv2.destroyAllWindows()

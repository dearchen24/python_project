import sys
import cv2

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from win import Ui_Frame
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        # 调用父对象方法
        super(MainWindow, self).__init__(parent=None)
        self.setupUi(self)
        self.timer = QTimer()  # 定时器
        self.timer.timeout.connect(self.update_frame)  # 定时器与这个事件绑定触发
        self.cap = None

    def update_frame(self):
        # 从摄像头读取帧
        ret, frame = self.cap.read()
        if not ret:
            print("无法捕捉帧")
            self.timer.stop()
            return

        # 将帧从 BGR 转为 RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 转换为 QImage
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # 在 QLabel 中显示图像
        self.labCamera.setPixmap(QPixmap.fromImage(qt_image))


    def but_start_click(self):

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            QtWidgets.QMessageBox.warning(self, "Error", "打开摄像头失败！")
            return
        self.timer.start(30)

    def but_stop_click(self):
        # 关闭视频
        self.timer.stop()
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None
        self.labCamera.clear()  # 停止后清除 QLabel 中显示的内容

    def but_quit_click(self):
        # 退出系统
        self.timer.stop()
        if self.cap and self.cap.isOpened():
            self.cap.release()
        QtWidgets.QApplication.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwin = MainWindow()
    mainwin.show()
    sys.exit(app.exec_())
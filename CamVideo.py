#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2

# 初始化摄像头
cap = cv2.VideoCapture(0)
# 为保存视频做准备
#fourcc = cv2.cv.CV_FOURCC("D", "I", "B", " ")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# 第三个参数则是镜头快慢的，20为正常，小于二十为慢镜头
out = cv2.VideoWriter('output2.avi', fourcc,25.0,(640,480))

while cap.isOpened():
    # 采集一帧一帧的图像数据
    isSuccess,frame = cap.read()
    # 实时的将采集到的数据显示到界面上
    if isSuccess:
        #cv2.imshow("My Capture",frame)
        out.write(frame)
    # 实现按下“q”键退出程序
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
out.release()
cv2.destoryAllWindows()
import math
import Image
import pytesseract
from matplotlib import pyplot as plt
import cv2
import sys
import time


video_capture = cv2.VideoCapture(0)

while True:
	ret,frame = video_capture.read()
	cv2.imshow('Video',frame)
	video_capture.set(cv2.CAP_PROP_POS_MSEC,5000) 
	if ret:
		cv2.imwrite("frame.jpg", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
text = pytesseract.image_to_string(Image.open('frame.jpg'))
print text



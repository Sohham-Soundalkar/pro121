import cv2
import numpy as np

video = cv2.VideoCapture(0)
image = cv2.imread('grand_palace.jpg')

while True:
    ret, frame = video.read()
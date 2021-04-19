import numpy as np
import cv2
cap = cv2.VideoCapture("rtsp://admin:p1216ct2@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0")
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

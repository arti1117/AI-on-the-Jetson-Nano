import cv2
print(cv2.__version__)

dispW=320
dispH=240
flip=2

camId = '/dev/video0'
camSet='nvarguscamerarc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camId, cv2.CAP_V4L2)

while True:
    ret, frame=cam.read()
    cv2.imshow('pyCam', frame)
    if cv2.waitKey(1)==ord('q'):
        break;

cam.release()
cv2.destroyAllWindows()

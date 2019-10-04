import cv2
import matplotlib.pyplot as plt 


#カメラ起動
cap = cv2.VideoCapture(0)
while True:
    #画像として読み込み
    _,frame = cap.read()
    #グレイスケール化
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #ガウシアンフィルターで平滑化
    frame = cv2.GaussianBlur(frame,(7,7),0)
    #画像の2値化
    frame = cv2.threshold(frame,140,240,cv2.THRESH_BINARY_INV)[1]

    
    cv2.imshow('OpenCV Camera', frame)

    #終了受付
    k = cv2.waitKey(1)
    if k==27 or k == 13: break


#カメラのリリース
cap.release()
cv2.destroyAllWindows()
import cv2

#カメラ起動
cap = cv2.VideoCapture(0)
while True:
    #画像として読み込み
    _,frame = cap.read()
    
    
    
    frame = cv2.Canny(frame,100,200)
    cv2.imshow('OpenCV Camera', frame)

    #終了受付
    k = cv2.waitKey(1)
    if k==27 or k == 13: break

#カメラのリリース
cap.release()
cv2.destroyAllWindows()
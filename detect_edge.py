import cv2

#カメラ起動
cap = cv2.VideoCapture(0)
while True:
    #画像として読み込み
    _,frame = cap.read()

    edge_img = cv2.Canny(frame,100,200)

    size = (600,400)
    frame = cv2.resize(frame,size)
    edge_img = cv2.resize(edge_img,size)

    cv2.imshow('OpenCV Camera', frame)
    cv2.imshow('Edge_ver.',edge_img)

    #終了受付
    k = cv2.waitKey(1)
    if k==27 or k == 13: break

#カメラのリリース
cap.release()
cv2.destroyAllWindows()
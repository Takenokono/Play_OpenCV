import cv2
import matplotlib.pyplot as plt 

#カスケードの読み込み(from github/opencv/data)
cascade_file = './Cascade/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#カメラ起動
cap = cv2.VideoCapture(0)
while True:
    #画像として読み込み
    _,frame = cap.read()
    
    #カスケードを使って顔を認識するリスト(座標)を返す
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(img_gray,minSize=(50,50))
    
    for (x,y,w,h) in face_list:
        bule = (255,0,0)
        cv2.rectangle(frame,(x,y),(x+w,y+h),bule,thickness=10)

    cv2.imshow('OpenCV Camera', frame)

    #終了受付
    k = cv2.waitKey(1)
    if k==27 or k == 13: break

#カメラのリリース
cap.release()
cv2.destroyAllWindows()

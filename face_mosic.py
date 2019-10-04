import cv2
import matplotlib.pyplot as plt 

#カスケードの読み込み(from github/opencv/data)
cascade_file = './Cascade/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)


def mosaic(img,rect,size):
    (x1,y1,x2,y2) = rect
    w = x2 - x1
    h = y2 - y1
    tmp_img = img[y1:y2,x1:x2]
    i_small = cv2.resize(tmp_img,(size,size))
    mosic_img = cv2.resize(i_small,(w,h),interpolation=cv2.INTER_AREA)
    img2 = img.copy()
    img2[y1:y2,x1:x2] = mosic_img
    return img2



#カメラ起動
cap = cv2.VideoCapture(0)
while True:
    #画像として読み込み
    _,frame = cap.read()
    
    #カスケードを使って顔を認識するリスト(座標)を返す
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(img_gray,minSize=(100,100))
    

    for (x,y,w,h) in face_list:
        frame = mosaic(frame,(x,y,x+w,y+h),20)
        
    cv2.imshow('OpenCV Camera', frame)

    #終了受付
    k = cv2.waitKey(1)
    if k==27 or k == 13: break


#カメラのリリース
cap.release()
cv2.destroyAllWindows()
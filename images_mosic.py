import cv2
import os
import sys 

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

img_dir = './Images'
filename = sys.argv

Pass = os.path.join(img_dir,filename[1])

img = cv2.imread(Pass)

print('*'*20)
print(Pass)
print('*'*20)

#カスケードを使って顔を認識するリスト(座標)を返す
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_list = cascade.detectMultiScale(img_gray,minSize=(10,10))

for (x,y,w,h) in face_list:
        img = mosaic(img,(x,y,x+w,y+h),5)

cv2.imwrite(Pass + '_mosic.jpg',img)
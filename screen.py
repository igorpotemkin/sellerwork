import cv2
import time


def screen_shot(camera:str,num_c,nam_order):
    dir = "media/files/orders/"+nam_order+'/'
    c = 0
    while c<5:
        try:
            cam = cv2.VideoCapture(camera)
            cam.isOpened()
            result, images = cam.read()
            if result:
                files = str(dir)+str(num_c)+'foto.jpg'
                cv2.imwrite(dir+files, images)
                time.sleep(5)
        except:
            print('none')
        c = c +1

    return 'ok'
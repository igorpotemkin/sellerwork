import cv2
import time
import os
from webcams import models as cam_models


def screen_shot(camera:str,num_c,nam_order):
    if not os.path.exists("static/orders/"+nam_order):
        # if the demo_folder directory is not present
        # then create it.
        os.makedirs("static/orders/"+nam_order)

    dir = "static/orders/"+nam_order+'/'
    c = 0
    while c<5:
        try:
            cam = cv2.VideoCapture(camera)
            cam.isOpened()
            result, images = cam.read()
            if result:
                files = str(dir)+str(num_c)+'foto.jpg'
                try:
                    cv2.imwrite(files, images)
                    m = cam_models.foto_order.objects.update_or_create(link=files,defaults={"order":nam_order,
                                                                                                 "link":files})
                    time.sleep(5)
                except:
                    print('none')
        except:
            print('none')
        c = c +1

    return 'ok'


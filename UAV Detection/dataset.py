"""
* Bu kod OpenCV modülünü kullanarak videolardan düzenli aralıklarla ekran görüntüsü alınmasını ve kaydedilmesini sağlamaktadır.
! Düzenlemelerinizi ayrı bir branch olarak ana projeye pr atınız.
? Sorularınızı ekibe iletebilirsiniz.
TODO: Kod denenerek dataset oluşturmaya başlanacak.
"""

import cv2
import os
import time

cam = cv2.VideoCapture("/path/to/videoIn.mp4")   # Video'ya ait dizini seçiyoruz.

try:
    if not os.path.exists('data'):   # Ekran görüntülerini depolamak için yeni klasör açıyoruz.
        os.makedirs('data')

except OSError:
    print('Error: Creating directory of data')

intvl = 2   # Ekran görüntüsü alınacak aralığı seçiyoruz.

fps= int(cam.get(cv2.CAP_PROP_FPS))
print("fps : " ,fps)

currentframe = 0
while (True):
    ret, frame = cam.read()
    if ret:
        if(currentframe % (fps*intvl) == 0):
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()

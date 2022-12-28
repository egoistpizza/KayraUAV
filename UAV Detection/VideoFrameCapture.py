"""
* Bu kod OpenCV modülünü kullanarak videolardan düzenli aralıklarla ekran görüntüsü alınmasını ve kaydedilmesini sağlamaktadır.
? Sorularınızı discord üzerinden iletebilirsiniz
TODO: Kod denenerek dataset oluşturmaya başlanacak.
TODO: Videoları otomatik olarak klasörden bulmalı
"""

import cv2 as cv
import os
import time
from math import floor,ceil


#*---Önemli Değişkenler---
video_dir = os.path.join(os.getcwd(),"videos","video.mp4") # Videoya ait dizini seçiyoruz. Şu an da "%current_working_directory%/videos/video.mp4" dizini seçili
interval = 2 # Interval in seconds
img_extension = ".png" # Target image type

try:
    if not os.path.exists('data'):   # Ekran görüntülerini depolamak için yeni klasör açıyoruz.
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

save_dir = "data"


#----The Main Program----
if __name__ == "__main__":
    cap = cv.VideoCapture(video_dir) #The capture object
            
    fps = cap.get(cv.CAP_PROP_FPS)                  #FPS of the video
    total_frames = cap.get(cv.CAP_PROP_FRAME_COUNT) #total frame count of the video
    duration = total_frames/fps                     #duration of the video
    max_iter = floor(duration/interval)

    for i in range(max_iter):
        cap.set(cv.CAP_PROP_POS_FRAMES, i*interval*fps-1)
        ret, frame = cap.read()
        if ret:
            cv.imwrite(os.path.join(save_dir,"SS_{2}{0}{1}".format(str(i),img_extension,floor(time.time_ns()/1000000))), frame)
        else:
            print("An error occured while reading from the capture.")
            break
    cap.release()

    print("Total of {} images saved.".format(str(max_iter)))
    print("Save directory: {}".format(save_dir))
    print("Exiting in 10 seconds")
    time.sleep(10) #Giving time for the console to see the error

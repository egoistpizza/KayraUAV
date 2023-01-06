"""
* Bu kod OpenCV modülü kullanılarak bir klasördeki videolardan periyodik olarak frame yakalanmasını ve kaydedilmesini sağlamaktadır.
* Kullanım amacı, dataset kaynağı olan videolardan frame elde edilerek labeling işlemine tabi tutulmasıdır.
? Sorularınız için: kayraproject@gmail.com
! OS modülünün dosya işlemlerini gerçekleştirebilmesi için yönetici olarak çalıştırınız.
TODO: Kod dataset oluşturmak için hazır, tüm testler başarıyla tamamlandı, proje kapsamında kullanılabilir.
"""

import cv2 as cv
import os
import time
from math import floor,ceil

# * ---Önemli Değişkenler---

video_dir = "/home/egoist/Videolar/dataset-test/Videos"   # Videoya ait dizini seçiyoruz. Varsayılan olarak "%current_working_directory%/Videos" dizini seçili
save_dir = os.path.join(video_dir,"frames")   # Framelerin kaydedileceği dizini seçiyoruz.
interval = 2   # Saniye cinsinden periyot (bekleme süresi).
img_extension = ".png"   # Framelerin kaydedileceği dosya uzantısı.

videos = []   # Verilen klasördeki videolara ait uzantıların toplanacağı lise.
video_exts = [".mp4",".mov",".webm",".wmv",".avi","mkv"]   # Desteklenen video uzantıları (genişletilebilir).

for item in os.listdir(video_dir):
    if os.path.isfile(os.path.join(video_dir,item)):
        if os.path.splitext(item)[1].lower() in video_exts:
            videos.append(os.path.join(video_dir,item))

print(f"{len(videos)} videos were found in the specified folder.")

try:
    if not os.path.exists(save_dir):   # Eğer bulunmuyorsa, ekran görüntülerini depolamak için yeni bir klasör açıyoruz.
        os.makedirs(save_dir)
        
except OSError:
    print('OS_Error: Creating directory of data.\nPlease run the code as administrator to complete the file operations.\nIf you continue to receive errors, you can create an issue or contact us. (Contact: kayraproject@gmail.com)')

def getFramesFromVideo(video_file):
    cap = cv.VideoCapture(video_file)   # Video yakalama objesi.
    
    fps = cap.get(cv.CAP_PROP_FPS)   # Videoya ait FPS değeri.
    total_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)   # Videodaki toplam frame sayısı.
    duration = total_frames/fps   # Saniye cinsinden video süresi.
    max_iter = floor(duration/interval)   # Belirlenen periyotta çekilebilecek maksimum frame sayısı.

    for i in range(max_iter):
        cap.set(cv.CAP_PROP_POS_FRAMES, i*interval*fps-1)
        ret, frame = cap.read()
        if ret:
            cv.imwrite(os.path.join(save_dir,f"frame_{floor(time.time_ns()/1000000)}_{str(i)}{img_extension}"), frame)
            print(f"\nThe frame has been successfully saved to the directory: {save_dir}, {i}")
        else:
            print("A problem occurred while capturing the frame.\nTry again by changing the interval value.\nIf it is repeated, it means there is a video reading error.\nYou can open an issue or contact us for help or bugfix. (Contact: kayraproject@gmail.com)")
            break
    cap.release()

    print(f"\n\n\nTotal of {str(max_iter)} images saved.\nSave directory: {save_dir}")

for video in videos:
    getFramesFromVideo(video)

print("\n\n\nAll videos in the destination folder have been processed successfully.\nThere is nothing to do.")

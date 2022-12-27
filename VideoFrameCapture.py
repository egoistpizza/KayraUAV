import cv2 as cv
import os
from time import sleep
from math import floor,ceil


curr_dir = os.getcwd()

video_dir = os.path.join(curr_dir,"Resources","Videos","dog.mp4")
save_dir = os.path.join(curr_dir, "Saved Screenshots")

interval = 1 #interval in seconds
img_extension = ".png" #Target image type


#----The Main----
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
            cv.imwrite(os.path.join(save_dir,"SS_{0}{1}".format(str(i),img_extension)), frame)
        else:
            print("An error occured while reading from the capture.")
            break
    cap.release()

    print("Total of {} images saved.".format(str(max_iter)))
    print("Save directory: {}".format(save_dir))
    print("Exiting in 10 seconds")
    sleep(10)

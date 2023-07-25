import cv2
import os
from utils import mkdir
from glob import glob
#OUT_PATH = "data/output/baby"

def saveVideo(OUT_PATH):
    mkdir(OUT_PATH)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter()

    images = sorted(glob(os.path.join(OUT_PATH+'/', '*.' + 'png')))
    height, width, layers = cv2.imread(images[0]).shape
    size = (width, height)
    success = out.open(OUT_PATH + '_output' +'.mp4', fourcc, 20.0, size, True)

    frames=[]
    if success:
        images = sorted(glob(os.path.join(OUT_PATH+'/', '*.' + 'png')))
        for image in images:
            frame = cv2.imread(image)
            out.write(frame)

    out.release()

def getFrame(sec, VID_PATH, vidcap, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(VID_PATH+"/image"+str(count)+".PNG", image)     # save frame as png file
    return hasFrames

def getFrames(VID_PATH):
    mkdir(VID_PATH)
    vidcap = cv2.VideoCapture(VID_PATH+".mp4")
    sec = 0
    frameRate = 0.1 #//it will capture image in each 0.5 second
    count=1
    success = getFrame(sec, VID_PATH, vidcap, count)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, VID_PATH, vidcap, count)
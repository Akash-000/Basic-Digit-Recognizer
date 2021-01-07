import cv2
import os
import sys
import numpy as np
import pyautogui
import time
from PIL import ImageGrab


try:
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])

except:
    print("Argument missing")
    print("Please provide valid label name and number of samples")

img_data="image_data"
image_label_path = os.path.join(img_data,label_name)

try:
    os.mkdir(img_data)
except(FileExistsError):
    pass

try:
    os.mkdir(image_label_path)
except(FileExistsError):
    print("Adding to existing folder")



def saveimg():
    
    if(saveimg.count<num_samples):
        image = ImageGrab.grab(bbox=(130,150,700,450))
        save_path = os.path.join(image_label_path, "{}.jpg".format(saveimg.count+1))
        image.save(save_path)
        saveimg.count+=1
        canvas.delete("all")
        return
    elif(saveimg.count==num_samples):
        print("Max limit reached")
        master.destroy()



saveimg.count=0


from tkinter import *
master = Tk()
master.title("Data Collector")
master.geometry("+100+100")
canvas = Canvas(master, width=600, height=300, bg='white')
canvas.pack(padx=20, pady=20)


def click(click_event):
    global prev
    prev = click_event


def move(move_event):
    global prev
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=20)
    prev = move_event


canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>', move)


button = Button(master, text = "Save", command = saveimg)
button.pack()


mainloop()









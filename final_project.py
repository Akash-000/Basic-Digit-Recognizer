import cv2
import numpy as np
import os
from keras.models import load_model
from tkinter import *
from PIL import ImageGrab
#image_save = "final_pics"


    


window=Tk()
window.title("Answer")
window.geometry("200x200+700+100")
heading=Label(window,text="Answer", font="times 20 bold")
heading.pack()
answer=Label(window,text="?", font="times 60 bold")
answer.pack()

def labeler(n):
    answer["text"]=str(n)

    

Class_map={
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    }

def mapper(val):
    return Class_map[val]



def predictimg():
    image_drawn = ImageGrab.grab(bbox=(160,175,800,550))

    image_drawn.save("image_drawn.jpg")
    
    
    image = cv2.imread("image_drawn.jpg")
    image = cv2.resize(image, (227,227))
    pred = model.predict(np.array([image]))
    img_code = np.argmax(pred[0])
    img_digit_name = mapper(img_code)

    print(img_digit_name)
    labeler(img_digit_name)
    

def destroy():
    window.destroy()
    master.destroy()
    

def clear():
    answer["text"]="?"
    canvas.delete("all")



model = load_model("digit_recognizers.h5")

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


buttonpred = Button(master, text = "Save", command = predictimg)
buttonpred.place(x=220, y=310)

exit_button=Button(master, text="Exit", command = destroy)
exit_button.place(x=270, y=310)
clear_button = Button(master, text="Clear Canvas", command = clear)
clear_button.place(x=320, y=310)
mainloop()
window.mainloop()

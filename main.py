#Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import wfc

if __name__ == '__main__':
    #Create an instance of tkinter frame
    win = Tk()

    #Set the geometry of tkinter frame
    win.geometry("300x300")

    #Create a canvas
    canvas= Canvas(win, width= 300, height= 300)
    canvas.pack()

    #Load an image in the script
    img= ImageTk.PhotoImage(Image.open("Temp1.jpg"))

    #Add image to the Canvas Items
    canvas.create_image(0,0,anchor=NW,image=img)

    win.mainloop()
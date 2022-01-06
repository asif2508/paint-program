from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from PIL import ImageTk, Image, ImageDraw, ImageGrab
from tkinter import messagebox
from tkinter import filedialog
import time
root = Tk()
root.title("Paint")
root.geometry("800x520")
#brush default color
brush_color = "black"
#creating line function
def paint(lavender):
    brush_size = brush_slider.get()
    brush_type = rb.get()
    #creating line
    x1 = lavender.x - 1
    y1 = lavender.y - 1
    x2 = lavender.x + 1
    y2 = lavender.y + 1
    my_canvas.create_line(x1,y1,x2,y2, fill=brush_color, width=brush_size, capstyle=brush_type, smooth=True)
#update brush color
def change_brush_size(thing):
    slider_label.config(text=int(brush_slider.get()))
def brush_color_function():
    global brush_color
    brush_color = colorchooser.askcolor()[1]
    pass
def canvas_color_function():
    global canvas_color
    canvas_color = colorchooser.askcolor()[1]
    my_canvas.config(bg=canvas_color)
#clearing screen function
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")
def save():
    result = filedialog.asksaveasfilename(initialdir="/home/asif/Pictures/", filetypes=(("PNG file", "*.png"),("ALL files","*.*")))
    if result.endswith(".png"):
        pass
    else:
        result = result + ".png"
    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        time.sleep(2)
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)
    #popup message
    messagebox.showinfo("Picture saved!", "Your picture has been saved!")    

#main frame
mainframe = Frame(root, height=500, width=800, bg="darkgrey")
mainframe.pack(fill="both", expand=1)
#canvas
my_canvas = Canvas(mainframe, height=490, width=650,bg="white",bd=5, relief="sunken")
my_canvas.grid(row=0, column=1, columnspan=5, pady=5, sticky=N)
#mouse binding
my_canvas.bind('<B1-Motion>', paint)

#adding slider
brush_slider_frame = LabelFrame(mainframe, text="Brush Width", font=("roboto"), bg="lavender", fg="black", relief="raised")
brush_slider_frame.grid(row=0,column=0, padx=5, sticky=N, pady=10)
global brush_slider
brush_slider = ttk.Scale(brush_slider_frame, from_=100, to=1, command=change_brush_size, orient=VERTICAL, value=10)
brush_slider.pack()
slider_label = Label(brush_slider_frame, text=int(brush_slider.get()), font=("roboto"))
slider_label.pack()

#brush type 
brush_type_frame = LabelFrame(mainframe, text="Brush Type", font=("roboto"), bg="lavender", fg="black", relief="raised", width=9)
brush_type_frame.grid(row=0, column=0, padx=5, sticky=N, pady=165)
global rb
rb = StringVar()
rb.set("round")
rb1 = Radiobutton(brush_type_frame, text="Round", variable=rb, value="round", font=("roboto"), bg="lavender", fg="black", width=8)
rb1.pack(pady=2, anchor=W)
rb1 = Radiobutton(brush_type_frame, text="Lines", variable=rb, value="butt", font=("roboto"), bg="lavender", fg="black", width=8)
rb1.pack(pady=2,anchor=W)
rb1 = Radiobutton(brush_type_frame, text="Square", variable=rb, value="projecting", font=("roboto"), bg="lavender", fg="black", width=8)
rb1.pack(pady=2,anchor=W)

#color chooser frame
color_chooser_frame = LabelFrame(mainframe, text="Choose color",font=("roboto"), bg="lavender", fg="black", relief="raised", width=9)
color_chooser_frame.grid(row=0, column=0, padx=5, pady=283, sticky=N)
#brush color button
brush_color_buton = Button(color_chooser_frame, text="Brush color",command=brush_color_function, bg="black", width=8, font=("roboto"))
brush_color_buton.pack()
#canvas color button
canvas_color_buton = Button(color_chooser_frame, text="Canvas color",command=canvas_color_function, bg="black", width=8, font=("roboto"))
canvas_color_buton.pack()

#programe options
programme_option_frame = LabelFrame(mainframe, text="Options", font=("roboto"), bg="lavender", fg="black", relief="raised",width=9)
programme_option_frame.grid(row=0,column=0, padx=5, pady=380)

clear_button = Button(programme_option_frame, text="Clear",command=clear_screen, bg="black", width=8, font=("roboto"))
clear_button.pack()
save_button = Button(programme_option_frame, text="Save",command=save, bg="black", width=8, font=("roboto"))
save_button.pack()
exit_button = Button(programme_option_frame, text="Exit",command=root.quit, bg="black", width=8, font=("roboto"))
exit_button.pack()








root.mainloop()
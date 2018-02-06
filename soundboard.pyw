import tkinter
import winsound
import sys

main=tkinter.Tk()
main.title("Aaron Soundboard v1")
main.geometry("810x720")
main.configure(background="#193073")
sound1="sounds/abspacken.wav"
sound2="sounds/alsob.wav"
sound3="sounds/entertaste.wav"
sound4="sounds/hae.wav"
sound5="sounds/husten.wav"
sound6="sounds/iminlove.wav"
sound7="sounds/iminlove2.wav"
sound8="sounds/lachen.wav"
sound9="sounds/rooftop.wav"
sound10="sounds/shapeofyou.wav"
normal="transparent_button_normal.png"
pressed="transparent_button_pressed.png"
button_normal=tkinter.PhotoImage(file=normal)
button_pressed=tkinter.PhotoImage(file=pressed)

def show_pressed(b):
    b.configure(image=button_pressed)
    b.configure(bg="#193073")
    b.image=button_pressed
    main.update()
    return
def show_released(b):
    b.configure(image=button_normal, bg="#193073")
    b.image=button_normal
    main.update()
    return

def playsound(sound,b):
    winsound.PlaySound(sound,winsound.SND_ASYNC)

    

b1=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound1,b1))
b1.grid(row="0",column="0")
b1.image=button_normal
b1.bind('<ButtonPress-1>',lambda event: show_pressed(b1))
b1.bind('<ButtonRelease-1>',lambda event: show_released(b1))
b2=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound2,b2))
b2.grid(row="0",column="1")
b2.image=button_normal
b2.bind('<ButtonPress-1>',lambda event: show_pressed(b2))
b2.bind('<ButtonRelease-1>',lambda event: show_released(b2))
b3=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound3,b3))
b3.grid(row="0",column="2")
b3.image=button_normal
b3.bind('<ButtonPress-1>',lambda event: show_pressed(b3))
b3.bind('<ButtonRelease-1>',lambda event: show_released(b3))
b4=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound4,b4))
b4.grid(row="0",column="3")
b4.image=button_normal
b4.bind('<ButtonPress-1>',lambda event: show_pressed(b4))
b4.bind('<ButtonRelease-1>',lambda event: show_released(b4))
b5=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound5,b5))
b5.grid(row="2",column="0")
b5.image=button_normal
b5.bind('<ButtonPress-1>',lambda event: show_pressed(b5))
b5.bind('<ButtonRelease-1>',lambda event: show_released(b5))
b6=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound6,b6))
b6.grid(row="2",column="1")
b6.image=button_normal
b6.bind('<ButtonPress-1>',lambda event: show_pressed(b6))
b6.bind('<ButtonRelease-1>',lambda event: show_released(b6))
b7=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound7,b7))
b7.grid(row="2",column="2")
b7.image=button_normal
b7.bind('<ButtonPress-1>',lambda event: show_pressed(b7))
b7.bind('<ButtonRelease-1>',lambda event: show_released(b7))
b8=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound8,b8))
b8.grid(row="2",column="3")
b8.image=button_normal
b8.bind('<ButtonPress-1>',lambda event: show_pressed(b8))
b8.bind('<ButtonRelease-1>',lambda event: show_released(b8))
b9=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound9,b9))
b9.grid(row="4",column="0")
b9.image=button_normal
b9.bind('<ButtonPress-1>',lambda event: show_pressed(b9))
b9.bind('<ButtonRelease-1>',lambda event: show_released(b9))
b10=tkinter.Button(main,image=button_normal,bg="#193073",activebackground="#193073",border="0",command=lambda:playsound(sound10,b10))
b10.grid(row="4",column="1")
b10.image=button_normal
b10.bind('<ButtonPress-1>',lambda event: show_pressed(b10))
b10.bind('<ButtonRelease-1>',lambda event: show_released(b10))
l1=tkinter.Label(main,text="Abspacken"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l1.grid(row="1",column="0")
l2=tkinter.Label(main,text="Als ob"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l2.grid(row="1",column="1")
l3=tkinter.Label(main,text="Entertaste"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l3.grid(row="1",column="2")
l4=tkinter.Label(main,text="Hä"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l4.grid(row="1",column="3")
l5=tkinter.Label(main,text="Husten"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l5.grid(row="3",column="0")
l6=tkinter.Label(main,text="I'm in love with"+"\n"+"the Shape of you",fg="white",bg="#193073",font=("Helvetica", 13, "bold"))
l6.grid(row="3",column="1")
l7=tkinter.Label(main,text="I'm in love with"+"\n"+"the Shape of you 2",fg="white",bg="#193073",font=("Helvetica", 13, "bold"))
l7.grid(row="3",column="2")
l8=tkinter.Label(main,text="Lachen"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l8.grid(row="3",column="3")
l9=tkinter.Label(main,text="Rooftop"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l9.grid(row="5",column="0")
l10=tkinter.Label(main,text="Shape of you"+"\n",fg="white",bg="#193073",font=("Helvetica", 14, "bold"))
l10.grid(row="5",column="1")
l11=tkinter.Label(main,text="\n"+"Mehr folgt..."+"\n",fg="white",bg="#193073",font=("Helvetica", 16, "bold"))
l11.grid(row="4",column="3")
main.mainloop()

"""
Made by Kevin Rossmeier
Twitter: Fedoz_Gameplays
Instagram: fedoz_1308
"""
import tkinter
import winsound
import sys
import os

""" Variablen """
buttons = []
labels = []
sounds = []
filenames = ["abspacken.wav", "alsob.wav", "entertaste.wav", "hae.wav", "husten.wav", "iminlove.wav",
             "iminlove2.wav", "lachen.wav", "rooftop.wav", "shapeofyou.wav"]
label_text = ["Abspacken", "Als ob", "Entertaste", "Hä", "Husten", "I'm in love", "I'm in love 2",
              "Lachen", "Rooftop", "Shape of you"]

""" Funktionen """


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def show_pressed(b):
    b.configure(image=button_pressed, bg="#193073")
    b.image = button_pressed
    main.update()


def show_released(b):
    b.configure(image=button_normal, bg="#193073")
    b.image = button_normal
    main.update()


def playsound(sound, b):
    winsound.PlaySound(sound, winsound.SND_ASYNC)


""" Tkinter-Fenster erstellen """
main = tkinter.Tk()
main.title("Aaron Soundboard v2")
main.configure(background="#193073")


""" Sounds und Bilder laden """
for i in range(len(filenames)):
    sounds.append(resource_path("sounds/"+filenames[i]))
normal, pressed = resource_path("transparent_button_normal.png"), resource_path("transparent_button_pressed.png")
button_normal, button_pressed = tkinter.PhotoImage(file=normal), tkinter.PhotoImage(file=pressed)

""" Buttons und Labels """
for i in range(len(filenames)):
    buttons.append(tkinter.Button(main, image=button_normal, bg="#193073", activebackground="#193073", border="0", command=lambda i=i: playsound(sounds[i], buttons[i])))
    buttons[i].bind("<ButtonPress-1>", lambda event, i=i: show_pressed(buttons[i]))
    buttons[i].bind('<ButtonRelease-1>', lambda event, i=i: show_released(buttons[i]))
    labels.append(tkinter.Label(main, text=label_text[i], fg="white", bg="#193073", font=("Helvetica", 14, "bold")))
    if i <= 3:
        buttons[i].grid(row="0", column=i)
        labels[i].grid(row="1", column=i)
    elif i >= 4 and i <= 7:
        buttons[i].grid(row="2", column=i-4)
        labels[i].grid(row="3", column=i-4)
    elif i >= 8 and i <= 11:
        buttons[i].grid(row="4", column=i-8)
        labels[i].grid(row="5", column=i-8)

main.mainloop()

from tkinter import *
import webbrowser

def open_wahab_project():
    webbrowser.open_new("https://barayaa.github.io/Niebe-phone/")

#creer une fenetre

window = Tk()
frame = Frame(window, bg='#41B77F')

window.title("My Python Page")
window.geometry("1080x720")
window.minsize(460, 360)
window.config(background='#41B77F')
frame = Frame(window, bg='#41B77F')

label_title = Label(window, text="Bienvenue sur Ma page", font=("Courrier", 40), bg='#41B77F', fg='white')
label_title.pack()

label_subtitle = Label(frame, text="Vous voulez voir mon projet", font=("Courrier", 25), bg='#41B77F', fg='white')
label_subtitle.pack()

yt_button = Button(frame, text="Cliquer ici", font=("Courrier", 25), bg='white', fg='#41B77F', command=open_wahab_project)
yt_button.pack()

frame.pack(expand=YES)


window.mainloop() 
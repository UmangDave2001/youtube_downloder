import tkinter
import customtkinter
from pytube import YouTube


def startdownloding():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink , on_progress_callback= on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        
        title.configure(text = ytObject.title, text_color = "white")
        finishLabel.configure(text = "")
        video.download(output_path= "Downloads")  # here i am gave this pc "Downloads path."
        finishLabel.configure(text = "Downloaded!")
    except:
        finishLabel.configure(text = "Download Error", text_color = "red")


def on_progress(stream , chunk , bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size*100
    per = str(int(percentage_of_completion))
    Precentage.configure(text = per + '0%')
    Precentage.update()


# we design UI so we need to SYSTEM SETTINGS 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# our app frame
app = customtkinter.CTk()
app.geometry("710x480")
app.title("YouTube Downloader")

# adding ui elements
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(pady =10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350 , height = 40 , textvariable= url_var)
link.pack()


# finished download
finishLabel = customtkinter.CTkLabel(app ,text = "")
finishLabel.pack()


# progress bar
Precentage = customtkinter.CTkLabel(app , text ="0%")
Precentage.pack()

progressBar  =  customtkinter.CTkProgressBar(app , width = 400)
progressBar.set(0)  
progressBar.pack(pady = 10)


# download button
download = customtkinter.CTkButton(app, text = "Download" , command= startdownloding)
download.pack(pady = 10)


# for running app
app.mainloop()
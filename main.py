try:
    from pytube import YouTube
    from pytube import Playlist
    from tkinter import *
    from tkinter import ttk
    from tkinter import filedialog, messagebox
    from ttkthemes import themed_tk as tk

    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme('radiance')
    root.minsize(350, 200)
    root.title("Youtube Video Downloader")
    root.iconbitmap("images/icon.ico")
    root.resizable(0,0)


    def downlaod():
        urlid = url_entry.get()

        if urlid == "":
            messagebox.showwarning("Error", "The Url is empty")
        else:
            ytd = YouTube(urlid).streams.first().download()
            suc_label = Label(root, text=f"Succesfully Downloaded "+{ytd}, fg='blue',
                               font=('tahoma', 12, "bold")).place(x=30, y=190)





    name_label = Label(root, text="YOUTUBE VIDEO DOWNLOADER", fg='blue',
                      font=('tahoma', 12, "bold")).place(x=30, y=5)
    url_label = Label(root, text="URL:", fg='#197BB5', font=('tahoma', 10, "bold")).place(x=30, y=45)
    url_entry = Entry(root, font=('tahoma', 12), width=29)
    url_entry.place(x=70, y=45)

    res_label = Label(root, text="RESOLUTION: Highest Quality", fg='#17B255',
                      font=('tahoma', 10, "bold")).place(x=30, y=85)

    btn = ttk.Button(root, text="Download", command=downlaod).place(x=150, y=120)



    root.mainloop()


except Exception as e:
    print("Some Modules are missing {}".format(e))

# url = ""
#
# ytd = YouTube(url).streams.first().download()
# print(ytd)




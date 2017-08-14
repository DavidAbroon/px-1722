import tkinter as tk
from tkinter import ttk
import paramiko
import os

LARGE_FONT = ("Verdana", 12)


class Begin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set Up Menu
        MainMenu(self)

        # General Settings
        # tk.Tk.wm_iconbitmap(self, default=os.path.dirname(os.path.realpath(__file__)) + "\\images\\3d.bmp")
        self.geometry('450x450')
        self.title("My First Application with Python")

        # Set Up Frames
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frameCollection = (StartPage, PageOne, PageTwo)

        for Frame in frameCollection:
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

    @staticmethod
    def take_picture(ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        ssh.connect(ip.get(), port=22, username='pi', password='raspberry')
        stdin, stdout, stderr = ssh.exec_command("python /home/pi/thomas_obale/camera.py")
        stdin.flush()
        sftp = ssh.open_sftp()

        sftp.get('/home/pi/thomas_obale/imgs/example.jpg', 'img.jpg')
        sftp.remove("/home/pi/thomas_obale/imgs/example.jpg")

        sftp.close()

        output = stdout.readlines()
        print(type(output))
        print("\n".join(output))

        ssh.close()


def displayMessage(message):
    print(message)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lable = ttk.Label(self, text='Start Page', font=LARGE_FONT)
        lable.pack(padx=10, pady=10)

        self.ipAddress = tk.StringVar()

        ipBox = ttk.Entry(self, textvariable=self.ipAddress)
        ipBox.pack(padx=10, pady=10)

        takePicture = ttk.Button(self, text='Take new Pictures',
                             command=lambda: controller.take_picture(self.ipAddress))
        takePicture.pack()

        button1 = ttk.Button(self, text='Visit Page',
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lable = ttk.Label(self, text='Page One', font=LARGE_FONT)
        lable.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text='Back To Home',
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button1 = ttk.Button(self, text='Page Two',
                             command=lambda: controller.show_frame(PageTwo))
        button1.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lable = ttk.Label(self, text='Page Two', font=LARGE_FONT)
        lable.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text='Back To Home',
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button1 = ttk.Button(self, text='Page One',
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()


class MainMenu:
    def __init__(self, parent):
        menuBar = tk.Menu(parent)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Exit", command=parent.quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        editMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=editMenu)

        parent.config(menu=menuBar)


app = Begin()
app.mainloop()
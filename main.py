from tkinter import *
import qrcode
from PIL import Image
import tkinter as tk

from PIL.ImageColor import colormap


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.center_window(500,500)
        #self.root.geometry("400x400")
        self.root.title("QR Code Generator")

        #Label
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.label = tk.Label(self.root,
                              text="Enter QR Link:",
                              font=('Ariel', 13),
                              pady=30
                              )
        self.label.grid(row=0,column=0)

        #entry -- where they will put link for QR
        self.entry = tk.Entry(self.root,
                              font=('Ariel', 16),
                              )
        self.entry.grid(row=0,column=1)

        #checkbox
        self.check1 = tk.IntVar()
        self.check2 = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.root,
                                       text="Download",
                                       variable=self.check1,
                                       onvalue=1,
                                       offvalue=0,
                                       command=self.downloadQR)
        self.checkbox.grid(row=1, column=0)

        self.checkbox2 = tk.Checkbutton(self.root,
                                       text="Open",
                                       variable=self.check2,
                                       onvalue=1,
                                       offvalue=0,
                                       command=self.openQR)
        self.checkbox2.grid(row=1, column=1)



        #run GUI
        self.root.mainloop()

    def downloadQR(self):
        if self.check1.get() == 1:
            print("Download")
    def openQR(self):
        if self.check2.get() == 1:
            print("Open QR")

    def center_window(self, width, height):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window geometry to the new coordinates
        self.root.geometry(f'{width}x{height}+{x}+{y}')

data = "https://github.com/almuqsitm"

qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')

#img.save('MyQRCode2.png')
#img.show()

MyGUI()


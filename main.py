import qrcode
import tkinter as tk




class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.center_window(500,200)
        #self.root.geometry("400x400")
        self.root.title("QR Code Generator")
        self.root.config(bg="black")

        #Label
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.label = tk.Label(self.root,
                              text="Enter QR Link:",
                              font=('Ariel', 13),
                              fg="#7bf71b",
                              pady=30,
                              bg="black"
                              )
        self.label.grid(row=0,column=0)

        #entry -- where they will put link for QR
        self.entry = tk.Entry(self.root,
                              font=('Ariel', 16),
                              bg='#444647',
                              fg="#7bf71b"
                              )
        self.entry.grid(row=0,column=1)

        #checkbox
        self.check1 = tk.IntVar()
        self.check2 = tk.IntVar()
        #self.check3 = tk.IntVar()

        self.checkbox = tk.Checkbutton(self.root,
                                       text="Download",
                                       variable=self.check1,
                                       onvalue=1,
                                       offvalue=0,
                                       fg='#7bf71b',
                                       bg="black",
                                       activebackground="black",
                                       activeforeground="#7bf71b",
                                       selectcolor="white"
                                       )
        self.checkbox.grid(row=1, column=0)

        self.checkbox2 = tk.Checkbutton(self.root,
                                       text="Open",
                                       variable=self.check2,
                                       onvalue=1,
                                       offvalue=0,
                                       fg="#7bf71b",
                                        bg="black",
                                        activebackground="black",
                                        activeforeground="#7bf71b",
                                        selectcolor="white"
                                       )
        self.checkbox2.grid(row=1, column=1)

        #generate button
        self.button = tk.Button(self.root,
                                text="Generate",
                                font=('Ariel', 16),
                                command=self.generateQR,
                                bg="#444647",
                                fg="#7bf71b",
                                bd=5,
                                relief="raised"
                                )
        self.button.grid(row=2, column=0, columnspan=2, pady=20)

        #run GUI
        self.root.mainloop()

    '''def downloadQR(self):
        if self.check1.get() == 1:
            print("Download")
    def openQR(self):
        if self.check2.get() == 1:
            print("Open QR")'''
    def generateQR(self):
        #print("button clicked", self.entry.get())

        data = self.entry.get()
        qr = qrcode.QRCode(version=1,
                           box_size=10,
                           border=5)

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

        if self.check1.get() == 1:
            img.save('MyQRCode.png')
        if self.check2.get() == 1:
            img.show()


        self.root.destroy()

    def center_window(self, width, height):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window geometry to the new coordinates
        self.root.geometry(f'{width}x{height}+{x}+{y}')

'''data = "https://github.com/almuqsitm"

qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')
'''
#img.save('MyQRCode2.png')
#img.show()
#
MyGUI()


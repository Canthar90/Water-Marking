from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
from datetime import datetime


class Screen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermarker")
        self.resizable(width=True, height=True)
        self.config(padx=50, pady=50)



        self.image_add_btn = Button(self, text="Plis select image", command=self.open_img, width=18)
        self.image_add_btn.grid(column=1, row=0)


        self.watermark_to_select = Button(text="Plis select watermark", command=self.open_watermark, width=18)
        self.watermark_to_select.grid(column=2, row=0)

        self.watermark_button = Button(text="Watermark Image", width=18, command=self.watermak_it)
        self.watermark_button.grid(column=1, row=3)

        self.quit_button = Button(text="Quit", command=self.destroy, width=18)
        self.quit_button.grid(column=2, row=3)
        # self.Button(frm, text="Quit", command=self.destroy).grid(column=1, row=0)
        self.mainloop()



    def open_img(self):
        x = self.openfilename()

        img = Image.open(x)

        self.image_to_work = img

        img.thumbnail((800,800), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(img)

        self.panel = Label(self, image=img)

        self.panel.image = img
        self.panel.grid(column=1, row=2)


    def open_watermark(self):
        x = self.openfilename()
        img = Image.open(x)
        img.thumbnail((200, 200))
        self.watermark_img = img
        img = ImageTk.PhotoImage(img)

        self.watermark_panel = Label(self, image=img)

        self.watermark_panel.image = img
        self.watermark_panel.grid(column=2, row=2)


    def openfilename(self):
        # open file dialog box to select image
        # The dialogue box has a title "Open"
        self.filename = filedialog.askopenfilename(title='Wybierz obraz', filetypes=[('PNG','png jpg'), ('JPG', 'png')])
        return self.filename
        pass


    def watermak_it(self):
        now = datetime.now()
        watermarked = self.image_to_work
        watermarked.paste(self.watermark_img, (0, 0))
        print(now)
        now = str(now)
        now = now.replace('.', '')
        now = now.replace(':', "")
        path=f'{now}.jpg'
        with open(path, mode='w') as fp:
            watermarked.save(fp=fp)
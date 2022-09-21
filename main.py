import qrcode
import cv2
from tkinter import StringVar, Tk, Toplevel, ttk, PhotoImage
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
from time import sleep

class QR_CODE:
    def __init__(self, file_name: str, content: str) -> None:
        self.file_name = file_name
        self.content = content

    def generate(self) -> None:
        img = qrcode.make(self.content)
        img.save("qr_codes/"+self.file_name+'.png')

    def decode(self) -> str:
        d = cv2.QRCodeDetector()
        val, _, _ = d.detectAndDecode(cv2.imread("qr_codes/" + self.file_name + ".png"))
        return "Decoded text is: " + val

class Gui:
    def __init__(self, window: Tk) -> None:
        self.window = window
        self.main_frame = ttk.Frame(window)
        self.main_frame.pack()
        # Entrys
        self.file_name = StringVar()
        self.file_name_entry = ttk.Entry(self.main_frame, textvariable=self.file_name)
        self.content = StringVar()
        self.content_entry = ttk.Entry(self.main_frame, textvariable=self.content)
        # Labels
        self.label_file_name = ttk.Label(self.main_frame, text='File Name:')
        self.label_content = ttk.Label(self.main_frame, text='Content:')
        # Buttons
        self.generate_button = ttk.Button(self.main_frame, text='Generate', command=self.display_qr_code)
        # Layout
        self.label_file_name.grid(row=1, column=1)
        self.file_name_entry.grid(row=1, column=2)
        self.label_content.grid(row=1, column=3)
        self.content_entry.grid(row=1, column=4)
        self.generate_button.grid(row=1, column=5)

    def display_qr_code(self):
        content = self.content.get()
        file_name = self.file_name.get()
        if len(content) != 0 and len(file_name) != 0:
            q1 = QR_CODE(file_name, content)
            q1.generate()
            sleep(5)
            qr_code_window = Toplevel()
            image1 = ImageTk.PhotoImage(Image.open(f"C:\\Programovanie\\Python\\QR Code Generator\\qr_codes\\xxx.png"))
            label1 = ttk.Label(qr_code_window, image=image1)
            label1.pack()
        else:
            showerror('ERROR', 'Fields cannot be empty')

window = Tk()
window.title('QR Code Generator')
window.geometry('600x600')

gui = Gui(window)

window.mainloop()
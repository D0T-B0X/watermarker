from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

filename = None


def textsize(text_, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text_, font=font)
    return width, height


def file_upload():
    global watermark_, filename
    file_types = [("Image files", "*.png *.jpg *.jpeg *.webm")]
    filename = filedialog.askopenfilename(filetypes=file_types)

    if len(filename):
        file_name = filename.split("/")[-1]
        filedisp = Label(window, text=f"Uploaded {file_name}", bg="#5A639C", fg='white')
        filedisp.place(relx=0.55, rely=0.18)

    watermark_label.place(relx=0.5, rely=0.30, anchor='center')
    watermark_.place(relx=0.5, rely=0.35, anchor='center')
    apply.place(relx=0.5, rely=0.42, anchor='center')


def apply_watermark():
    global filename
    string = "©" + watermark_.get()

    img = Image.open(filename)
    w, h = img.size
    font_size = round(20 * (h / 300))
    font = ImageFont.truetype("Atlane-PK3r7.otf", font_size)
    watermark_w, watermark_h = textsize(text_=string, font=font)
    pos = w - watermark_w - round((h / 20 + 3)), (h - watermark_h) - round((h / 20))
    c_text = Image.new('RGB', (watermark_w, watermark_h), color='#000000')

    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), string, fill="#ffffff", font=font)
    c_text.putalpha(100)
    img.paste(c_text, pos, c_text)

    string_ = ""
    for word in filename.split("/")[1:]:
        string_ += "/" + word
    img.save(string_)


window = Tk()
window.geometry('1280x720')
window.config(bg='#5A639C')

text = Label(window, text="Upload an Image:", bg="#5A639C", fg="#E2BBE9", pady=20, padx=20)
text.config(font=("Dosis", 20, "normal"))
text.place(relx=0.5, rely=0.1, anchor='center')

button = Button(window, text="Upload Image", command=file_upload)
button.place(relx=0.5, rely=0.2, anchor='center')

watermark_label = Label(window, text="Enter your watermark:", bg="#5A639C", fg='white', font=("Dosis", 15))
watermark_ = Entry(window, width=40)

label = Label()
label.place(relx=0.5, rely=0.4, anchor='center')

apply = Button(window, text="Apply Watermark", command=apply_watermark)

window.mainloop()

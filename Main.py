import shutil
from tkinter import *
from tkinter.filedialog import *

def zip():
    source_dir = askdirectory()
    dest_dir = source_dir
    print("Start Zip")
    shutil.make_archive(dest_dir, 'zip', source_dir)
    print("Done ZIP")


def unzip():
    source_dir = askopenfilename()
    dest_dir = source_dir.replace('.zip', '')
    print("Start Unzip")
    shutil.unpack_archive(source_dir, dest_dir, 'zip')
    print("Done Unzip")

#zip()
#unzip()

window = Tk()
window.geometry("300x150")
window.title("Chain Zipper")

lbl = Label(window, text='Chain Zip & Unzip', fg='red', font=("Helvetica"))
lbl.place(x=50, y=20)
btn = Button(window, text="Zip Your Folder", fg="blue", command=zip)
btn.place(x=80, y=60)
btn = Button(window, text="Unzip Your File", fg="green", command=unzip)
btn.place(x=80, y=100)

window.mainloop()
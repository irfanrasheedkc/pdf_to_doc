from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import os

files=Tk()
files.title('Easy Files')
files.geometry(f'400x600')
files.resizable(False,False)
# Add a frame to set the size of the window
frame= Frame(files, relief= 'sunken')
frame.pack(fill= BOTH, expand= True, padx= 10, pady=0)

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Pdf files",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")))
    label_file_explorer.config(text=os.path.split(filename)[1])

def convert_pdf():
    global filename
    global name
    name = name_entry.get()
    start=int(Entry2.get())
    end=int(Entry3.get())
    with open(filename, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        doc_path = os.path.expanduser("~\Desktop") +'\\'+ name + '.doc'
        print(doc_path)
        # Open a file with access mode 'a'
        file_object = open(doc_path, 'a')
        for i in range(start-1,end):
            page = reader.getPage(i)
            # Append page content at the end of file
            file_object.write(page.extractText())
            # Close the file
        file_object.close()

        return messagebox.showinfo('Success', f'File saved in desktop as {name}.doc')

        #Print success
        label_success.pack()

#Create heading
label = Label(
    frame,
    font = "Helvetica 40 bold",
    foreground = "grey", text = "Welcome")
label.pack(pady=30)

#Create a File Explorer button
button1 = Button(frame, text="Browse file", command=browseFiles)
button1.pack(pady=1)

# Create a File Explorer label
label_file_explorer = Label(frame,
                            text="Upload pdf",
                            width=100, height=4,
                            fg="grey")
label_file_explorer.pack(pady=1)

#Frame 2
frame2=Frame(files)
frame2.pack(fill= BOTH, expand= True, padx= 10, pady=0)
#Page Range
Label2 = Label(frame2,width=25)
Label2.configure(text='''                           Enter page range ''')
Label2.grid(row=0,column=0)

Entry2 = Entry(frame2,width=3)
Entry2.grid(row=0,column=1)

Entry3 = Entry(frame2,width=3)
Entry3.grid(row=0,column=3)

Label3 = Label(frame2)
Label3.configure(text='''-''')
Label3.grid(row=0,column=2)

#Frame3
frame3=Frame(files)
frame3.pack(fill= BOTH, expand= True, padx= 10, pady=0)
#Enter name of new file
name_label = Label(frame3, text = 'New file name', font=('calibre',10, 'bold'))
name_label.pack()
name_entry = Entry(frame3, font=('calibre',10,'normal'))
name_entry.pack()


#Create a File Converter button
button2 = Button(frame3, text="Convert File",height=5,bg='grey',fg='white', command= convert_pdf)
button2.pack(pady=50)


# Create a Message label
label_success = Label(frame3,
                            text='Success!!',
                            fg='green',
                            font=("Arial", 15),
                            width=100, height=4)

#   close window after 3 seconds
#files.after(3000, lambda: files.destroy())

files.mainloop()
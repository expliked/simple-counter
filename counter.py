from tkinter import Tk, Label
from tkinter.ttk import Button
from tkinter.filedialog import askopenfile
from keyboard import add_hotkey

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Text Document', '*.txt')])

    global filename
    filename = file.name
    
    if file is not None:
        global text
        global hotkey
        global value

        lines = file.read().split("\n")

        for line in lines:
            try:
                if (line[:7] == "hotkey:"):
                    hotkey = line[7:].strip(" ")

                if (line[:5] == "text:"):
                    text = line[5:].strip(" ")

                if (line[:6] == "value:"):
                    value = int(line[6:].strip(" "))

            except IndexError:
                pass
        
    else:
        raise Exception("exit")
    
    file.close()
    root.destroy()


def increase():
    global text
    global hotkey
    global value

    value += 1
    label["text"] = text.format(value)
    with open(filename, "w") as file:
        file.write(f"hotkey: {hotkey}\n"
                   f"text: {text}\n"
                   f"value: {value}"
        )

def decrease():
    global text
    global hotkey
    global value

    value -= 1
    label["text"] = text.format(value)
    with open(filename, "w") as file:
        file.write(f"hotkey: {hotkey}\n"
                   f"text: {text}\n"
                   f"value: {value}"
        )

# First Window:
root = Tk()

file_prompt = Label(root, text = "First, select the file that has the counter data:", font = "Arial 10")
file_prompt.pack(side = "left", padx = 5, pady = 15)

file_button = Button(root, text = "Open", command = lambda:open_file())
file_button.pack(side = "bottom", padx = 5, pady = 15)

root.title("Select a file containing your counter")
root.resizable(False, False)
root.mainloop()

# Second Window:
root2 = Tk()

label = Label(root2, text = text.format(value), font = "Arial 50", bg = "black", fg = "white")
label.pack()
    
inc_hk = add_hotkey(hotkey, increase)
dec_hk = add_hotkey(f"ctrl+shift+{hotkey}", decrease)

root2.title(f"{hotkey} to increase the counter, ctrl+shift+{hotkey} to decrease the counter. You can put this window on streamlabs too.")
root2.resizable(False, False)
root2.mainloop()

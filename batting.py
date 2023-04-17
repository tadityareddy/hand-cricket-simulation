import random

from score import get_machine_input

import tkinter as tk
import tkinter.messagebox as message
# Create the main window
root = tk.Tk()
root.title("Batting")
root.geometry("600x300")

# Define the function to open a new pop up window
s=0
time=[]
for i in range(6):
    time.append(random.randint(1,6))
out=False
def open_popup():
    global time
    global out
    global s
    input=entry.get()
    entry.delete(0, 'end')
    if input not in ["1","2","3","4","5","6"]:
        message.showerror("error", "invalid input")
    # Create the new pop up window
    elif out:

        popup = tk.Toplevel(root)
        popup.title("New Pop Up Window")

        # Add contents to the new pop up window
        label = tk.Label(popup, text="you are out",font=('Times', 24))
        label.pack(pady=20)

        lab=tk.Label(popup,text="your total score is "+ str(s),font=('Times', 24))
        lab.pack(pady=20)

        # Add a button to close the new pop up window
        close_button = tk.Button(popup, text="OK",font=('Times', 24), command=popup.destroy)
        close_button.pack(pady=10)
    else:

        s+=int(input)
        v=get_machine_input(time)
        text_label.config(text="Machine Score" + str(v), font=('Times', 24))
        result_label.config(text="score = "+str(s), font=('Times', 24))
        if v==int(input):
            out=True
        time.append(int(input))
        time=time[1:]


# Add a button to open the new pop up window
entry = tk.Entry(root)
entry.pack(side="top",padx=10,pady=10,anchor="nw")

text_label = tk.Label(root, text='')
text_label.pack(side="top", padx=10, pady=10)


popup_button = tk.Button(root, text="bat",font=("Times",25), command=open_popup)
popup_button.pack(pady=20)

result_label = tk.Label(root)
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()

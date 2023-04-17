import tkinter as tk
import random
import tkinter.messagebox as messagebox
import subprocess


# Create the main window
root = tk.Tk()
root.title("Even or Odd Game")

# Define the function to check whether a number is even or odd
def check_number():
    # Get the input value and the user's choice from the widgets
    input_value = entry.get()
    user_choice = choice_var.get()
    if input_value not in ["1","2","3","4","5","6"]:
        messagebox.showerror("error", "invalid input")
    else:

        input_value=int(input_value)+random.randint(1,6)
        # Check if the input value is even or odd
        if input_value % 2 == 0:
            result = "even"
        else:
            result = "odd"

        # Check if the user's choice matches the result
        if user_choice == result:
            result_label.config(text="You win!",font=('Times',24))
            popup = tk.Toplevel(root)
            popup.title("Congratulations!")
            label = tk.Label(popup, text="choose bat or bowl",font=('Times',24))
            label.pack(padx=20, pady=20)
            close_button = tk.Button(popup, text="Bat",font=('Times',24), command=bat)
            close_button.pack(pady=10)
            close_button = tk.Button(popup, text="Bowl",font=('Times',24), command=popup.destroy)
            close_button.pack(pady=10)
        else:
            result_label.config(text="You lose!",font=('Times',24))
            pop = tk.Toplevel(root)
            pop.title("Congratulations!")
            d=random.choice(["bat", "bowl"])
            label = tk.Label(pop, text="Machine choose " + d,font=('Times',24))
            label.pack(padx=20, pady=20)
            if d=="bat":
                close_button = tk.Button(pop, text="Ohk", font=('Times', 24), command=bat)
                close_button.pack(pady=10)
            else:
                close_button = tk.Button(pop, text="Ohk", font=('Times', 24), command=bat)
                close_button.pack(pady=10)




def bat():
    cmd = ["python", "C:/Users/ACER/PycharmProjects/handcricket/batting.py"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output and error messages
    print(out.decode())
    print(err.decode())


# Create the label and entry widget for the user to enter a number
number_label = tk.Label(root, text=" Enter your choice between 1-6 ",font=('Times',24),bg="#00ffbf",fg="#1400ff")
number_label.pack(pady=10)

entry = tk.Entry(root,font=(25))
entry.pack(pady=5)


# Create the radio buttons for the user to choose even or odd
choice_label = tk.Label(root, text="Even or Odd",font=('Times',24))
choice_label.pack(pady=10)

choice_var = tk.StringVar()
choice_var.set("even")

even_radio = tk.Radiobutton(root, text="Even",font=('Times',24),padx=40,indicatoron=False, variable=choice_var, value="even")
even_radio.pack()

odd_radio = tk.Radiobutton(root, text="Odd",font=('Times',24),padx=40,indicatoron=False, variable=choice_var, value="odd")
odd_radio.pack()

# Create the button to check whether the number is even or odd
check_button = tk.Button(root, text="toss",font=('Times',24), command=check_number)
check_button.pack(pady=10)

# Create the label to display the result
result_label = tk.Label(root)
result_label.pack(pady=10)



# Start the main event loop
root.mainloop()


import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the background color to white
window.configure(background="white")

# Create the input field
input_field = tk.Entry(window, width=30, fg="#000000", bg="#FAFAFA")
input_field.pack()

# Create the buttons
button_add = tk.Button(window, text="+", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_add.pack(side="left")

button_subtract = tk.Button(window, text="-", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_subtract.pack(side="left")

button_multiply = tk.Button(window, text="*", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_multiply.pack(side="left")

button_divide = tk.Button(window, text="/", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_divide.pack(side="left")

button_equal = tk.Button(window, text="=", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_equal.pack(side="left")

# Define the functions for the buttons
def add():
    first_number = float(input_field.get())
    second_number = float(input_field.get())
    result = first_number + second_number
    input_field.delete(0, tk.END)
    input_field.insert(0, result)

def subtract():
    first_number = float(input_field.get())
    second_number = float(input_field.get())
    result = first_number - second_number
    input_field.delete(0, tk.END)
    input_field.insert(0, result)

def multiply():
    first_number = float(input_field.get())
    second_number = float(input_field.get())
    result = first_number * second_number
    input_field.delete(0, tk.END)
    input_field.insert(0, result)

def divide():
    first_number = float(input_field.get())
    second_number = float(input_field.get())
    result = first_number / second_number
    input_field.delete(0, tk.END)
    input_field.insert(0, result)

# Bind the functions to the buttons
button_add.config(command=add)
button_subtract.config(command=subtract)
button_multiply.config(command=multiply)
button_divide.config(command=divide)

# Add the other buttons
button_0 = tk.Button(window, text="0", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_0.pack(side="left")

button_1 = tk.Button(window, text="1", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_1.pack(side="left")

button_2 = tk.Button(window, text="2", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_2.pack(side="left")

button_3 = tk.Button(window, text="3", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_3.pack(side="left")

button_4 = tk.Button(window, text="4", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_4.pack(side="left")

button_5 = tk.Button(window, text="5", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_5.pack(side="left")

button_6 = tk.Button(window, text="6", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_6.pack(side="left")

button_7 = tk.Button(window, text="7", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_7.pack(side="left")

button_8 = tk.Button(window, text="8", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_8.pack(side="left")

button_9 = tk.Button(window, text="9", font=("Helvetica Neue", 16), bg="#007AFF", fg="#FAFAFA")
button_9.pack(side="left")

# Start the main loop
window.mainloop()
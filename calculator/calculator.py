import tkinter as tk
from math import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("320x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        input_frame = tk.Frame(self.root, bd=5, relief="ridge")
        input_frame.pack(side="top", fill="both")

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                               textvariable=self.input_text, width=25,
                               bg="#eee", bd=0, justify="right")
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Buttons
        btns_frame = tk.Frame(self.root, bg="grey")
        btns_frame.pack()

        # Button layout
        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("**", 5, 2), ("=", 5, 3),
        ]

        for (text, row, col) in buttons:
            b = tk.Button(btns_frame, text=text, width=10, height=3,
                          command=lambda t=text: self.on_button_click(t))
            b.grid(row=row, column=col, padx=1, pady=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression, {"__builtins__": None}, vars()))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

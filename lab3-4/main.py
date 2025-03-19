import tkinter as tk
from tkinter import ttk
import math

COLORS = {
    "primary": "#2A3D4C",
    "secondary": "#A1B2B7",
    "background": "#F1F5F9",
    "text": "#3C4A55",
    "button": "#E1ECF4",
    "button_text": "#2A3D4C"
}

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x500")
        self.root.title("Калькулятор")
        self.root.configure(bg=COLORS["background"])
        self.configure_styles()
        
        self.current_input = ""
        self.create_widgets()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure(".", background=COLORS["background"], foreground=COLORS["text"])
        style.configure("TButton", 
                       font=('Arial', 12), 
                       padding=10,
                       borderwidth=2,
                       relief="flat",
                       background=COLORS["button"],
                       foreground=COLORS["button_text"])
        style.map("TButton", 
                 background=[('active', COLORS["secondary"])])
        
        style.configure("Special.TButton", 
                       background=COLORS["primary"],
                       foreground="white")
        
        style.configure("Display.TEntry",
                       font=('Arial', 20),
                       fieldbackground="white",
                       bordercolor=COLORS["primary"],
                       relief="flat")

    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.display = ttk.Entry(main_frame, style="Display.TEntry", justify="right", font=('Arial', 20))
        self.display.state(["readonly"])
        self.display.pack(fill="x", pady=10)
        
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(expand=True, fill="both")
        
        buttons = [
            ('7', '8', '9', '/', '√'),
            ('4', '5', '6', '*', 'x²'),
            ('1', '2', '3', '-', '←'),
            ('0', '.', '±', '+', '='),
            ('C', 'CE')
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = ttk.Button(buttons_frame, text=btn_text, 
                                command=lambda t=btn_text: self.on_button_click(t))
                if btn_text in {'=', '√', 'x²', '←', 'C', 'CE'}:
                    btn.configure(style="Special.TButton")
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
                buttons_frame.columnconfigure(col_idx, weight=1)
            buttons_frame.rowconfigure(row_idx, weight=1)

    def on_button_click(self, value):
        if value == "=":
            self.calculate()
        elif value == "C":
            self.current_input = ""
        elif value == "CE":
            self.current_input = self.current_input[:-1]
        elif value == "±":
            if self.current_input and self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = f'-{self.current_input}'
        elif value == "x²":
            self.current_input += "**2"
            self.calculate()
        elif value == "√":
            try:
                result = math.sqrt(float(self.current_input))
                self.current_input = str(result)
            except:
                self.current_input = "Ошибка"
        else:
            self.current_input += value
        
        self.update_display()

    def calculate(self):
        try:
            result = eval(self.current_input)
            self.current_input = str(result)
        except:
            self.current_input = "Ошибка"
        self.update_display()

    def update_display(self):
        self.display.state(["!readonly"])
        self.display.delete(0, "end")
        self.display.insert(0, self.current_input)
        self.display.state(["readonly"])

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

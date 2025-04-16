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
        self.root.geometry("1080x640")
        self.root.title("Калькулятор")
        self.root.configure(bg=COLORS["background"])
        self.configure_styles()
        
        self.current_input = ""
        self.memory = 0.0
        self.angle_mode = "Градусы"
        self.last_operation = None
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
        
        mode_frame = ttk.Frame(main_frame)
        mode_frame.pack(fill="x", pady=5)
        mode_buttons = ['МС', 'MR', 'MS', 'M+', 'M-', 'Градусы', 'Радианы', 'Грады']
        for btn_text in mode_buttons:
            btn = ttk.Button(mode_frame, text=btn_text, command=lambda t=btn_text: self.on_mode_button_click(t))
            btn.pack(side="left", padx=2)
        
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(expand=True, fill="both")
        
        button_rows = [
            ['Inv', 'In', '(', ')', '←', 'CE', 'C', '±', '√'],
            ['Int', 'sinh', 'sin', 'x²', 'n!', '7', '8', '9', '/', '%'],
            ['dms', 'cosh', 'cos', 'x^y', 'y√x', '4', '5', '6', '*', '1/x'],
            ['π', 'tanh', 'tan', 'x³', '3√x', '1', '2', '3', '-', '='],
            ['F-E', 'Exp', 'Mod', 'log', '10^x', '0', '.', '+', '', '']
        ]
        
        for row_idx, row_buttons in enumerate(button_rows):
            for col_idx, btn_text in enumerate(row_buttons):
                if not btn_text.strip():
                    continue
                btn = ttk.Button(buttons_frame, text=btn_text, 
                                command=lambda t=btn_text: self.on_button_click(t))
                if btn_text in {'√', 'x²', 'x³', 'sinh', 'cosh', 'tanh', 'sin', 'cos', 'tan', 
                                'π', '1/x', 'log', '10^x', 'Exp', 'Mod', 'Int', 'dms', 'F-E', 'x^y', 'y√x', '3√x', 'n!'}:
                    btn.configure(style="Special.TButton")
                if btn_text == '=':
                    btn.grid(row=row_idx, column=col_idx, columnspan=2, sticky="nsew", padx=2, pady=2)
                else:
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
                buttons_frame.columnconfigure(col_idx, weight=1)
            buttons_frame.rowconfigure(row_idx, weight=1)

    def on_mode_button_click(self, value):
        if value in ['МС', 'MR', 'MS', 'M+', 'M-']:
            if value == 'МС':
                self.memory = 0.0
            elif value == 'MR':
                self.current_input = str(self.memory)
            elif value == 'MS':
                try:
                    self.memory = float(self.current_input)
                except:
                    pass
            elif value == 'M+':
                try:
                    self.memory += float(self.current_input)
                except:
                    pass
            elif value == 'M-':
                try:
                    self.memory -= float(self.current_input)
                except:
                    pass
            self.update_display()
        elif value in ['Градусы', 'Радианы', 'Грады']:
            self.angle_mode = value

    def on_button_click(self, value):
        if value == "=":
            self.calculate()
        elif value == "C":
            self.current_input = ""
        elif value == "CE":
            self.current_input = self.current_input[:-1] if self.current_input else ""
        elif value == "±":
            if self.current_input and self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = f'-{self.current_input}'
        elif value == "x²":
            self._apply_unary_operation(lambda x: x ** 2)
        elif value == "x³":
            self._apply_unary_operation(lambda x: x ** 3)
        elif value == "√":
            self._apply_unary_operation(math.sqrt)
        elif value == "3√x":
            self._apply_unary_operation(lambda x: x ** (1/3))
        elif value == "1/x":
            self._apply_unary_operation(lambda x: 1 / x)
        elif value == "sin":
            self._apply_trig_operation(math.sin)
        elif value == "cos":
            self._apply_trig_operation(math.cos)
        elif value == "tan":
            self._apply_trig_operation(math.tan)
        elif value == "sinh":
            self._apply_unary_operation(math.sinh)
        elif value == "cosh":
            self._apply_unary_operation(math.cosh)
        elif value == "tanh":
            self._apply_unary_operation(math.tanh)
        elif value == "π":
            self.current_input += str(math.pi)
        elif value == "log":
            self._apply_unary_operation(math.log10)
        elif value == "10^x":
            self._apply_unary_operation(lambda x: 10 ** x)
        elif value == "Exp":
            self._apply_unary_operation(math.exp)
        elif value == "Mod":
            self.current_input += "%"
        elif value == "Int":
            self._apply_unary_operation(lambda x: int(x))
        elif value == "dms":
            self._convert_to_dms()
        elif value == "F-E":
            self._toggle_fe_notation()
        elif value == "n!":
            self._apply_unary_operation(lambda x: math.factorial(int(x)))
        elif value == "x^y":
            self._prepare_binary_operation("**")
        elif value == "y√x":
            self._prepare_binary_operation("**(1/")
        elif value == "←":
            self.current_input = self.current_input[:-1]
        elif value == "%":
            self._apply_unary_operation(lambda x: x / 100)
        else:
            self.current_input += value
        self.update_display()

    def _apply_unary_operation(self, func):
        try:
            num = float(self.current_input)
            result = func(num)
            self.current_input = str(result)
        except Exception as e:
            self.current_input = "Ошибка"

    def _apply_trig_operation(self, func):
        try:
            angle = float(self.current_input)
            if self.angle_mode == "Градусы":
                angle = math.radians(angle)
            elif self.angle_mode == "Грады":
                angle = math.radians(angle * 0.9)
            result = func(angle)
            self.current_input = str(result)
        except:
            self.current_input = "Ошибка"

    def _convert_to_dms(self):
        try:
            degrees = float(self.current_input)
            d = int(degrees)
            m = int((degrees - d) * 60)
            s = (degrees - d - m/60) * 3600
            self.current_input = f"{d}°{m}'{s:.2f}\""
        except:
            self.current_input = "Ошибка"

    def _toggle_fe_notation(self):
        try:
            num = float(self.current_input)
            if 'e' in self.current_input.lower():
                self.current_input = f"{num:.10f}".rstrip('0').rstrip('.')
            else:
                self.current_input = f"{num:.10e}"
        except:
            pass

    def _prepare_binary_operation(self, operator):
        if self.current_input:
            self.last_operation = (operator, float(self.current_input))
            self.current_input = ""

    def calculate(self):
        try:
            if self.last_operation:
                op, first_num = self.last_operation
                second_num = float(self.current_input)
                if "**(1/" in op:
                    result = second_num ** (1/first_num)
                else:
                    result = eval(f"{first_num}{op}{second_num}")
                self.current_input = str(result)
                self.last_operation = None
            else:
                result = eval(self.current_input)
                self.current_input = str(result)
        except ZeroDivisionError:
            self.current_input = "Ошибка: деление на ноль"
        except Exception as e:
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

import tkinter as tk

DIGITS = {
    7: (1, 0), 8: (1, 1), 9: (1, 2),
    4: (2, 0), 5: (2, 1), 6: (2, 2),
    1: (3, 0), 2: (3, 1), 3: (3, 2),
    0: (4, 1), '.': (4, 2)
}

OPERATORS = {
    '/': '\u00F7',
    '*': '\u00D7',
    '-': '-',
    '+': '+'
}

APP_NAME = 'Calculator'
SCREEN_SIZE = (290, 480)
ICON = 'icon.png'
FONT_STYLE = ('Consolas', 20)


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # main setup
        self.title(APP_NAME)
        self.geometry(f'{SCREEN_SIZE[0]}x{SCREEN_SIZE[1]}')

        icon = tk.PhotoImage(file=ICON)
        self.iconphoto(True, icon)

        # display
        CalculatorView(self)

    def run(self):
        self.mainloop()


class CalculatorLogic:
    def __init__(self):
        super().__init__()

        # Text calculations
        self.calculation_text = ''
        self.equation_label = tk.StringVar()

    def add_to_calculation(self, num):
        self.calculation_text += str(num)
        self.update_label()

    def evaluate_calculation(self):
        try:
            self.calculation_text = str(eval(self.calculation_text))
            self.update_label()
        except ZeroDivisionError:
            self.equation_label.set("ERROR")
        except SyntaxError:
            self.equation_label.set("ERROR")

    def clear_calculation(self):
        self.calculation_text = ''
        self.update_label()

    def delete_calculation(self):
        self.calculation_text = self.calculation_text[0:-1]
        self.update_label()

    def calculate_percent(self):
        decimal_text = ''
        try:
            for char in self.calculation_text[::-1]:
                if char.isnumeric() or char == '.':
                    decimal_text = char + decimal_text
                else:
                    break

            length_difference = len(self.calculation_text) - len(decimal_text)
            decimal_text = float(decimal_text)

            self.calculation_text = self.calculation_text[:length_difference] + str(decimal_text / 100)
            self.update_label()

        except ValueError:
            self.equation_label.set("ERROR")

    def update_label(self):
        self.equation_label.set(self.calculation_text)


class CalculatorView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.calc_logic = CalculatorLogic()

        # create frame for both screen and buttons
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(expand=True, fill='both')

        self.button_frame = tk.Frame(self, bg='#3b3940')
        self.button_frame.pack(expand=True, fill='both')

        # grid adjustment for button frame
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(0, 4):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

        # UI
        self.create_screen_label()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.pack(expand=True, fill='both')

    def create_screen_label(self):
        screen = tk.Label(self.display_frame,
                          textvariable=self.calc_logic.equation_label,
                          font=FONT_STYLE,
                          bg='#262529',
                          height=4,
                          anchor=tk.E,
                          fg='white')
        screen.pack(expand=True, fill='both')

    def create_digit_buttons(self):
        for digit, grid in DIGITS.items():
            button = tk.Button(self.button_frame,
                               text=str(digit),
                               command=lambda number=digit: self.calc_logic.add_to_calculation(number),
                               fg='white',
                               bg='#3b3940',
                               activeforeground='white',
                               activebackground='#4e4c53',
                               borderwidth=0,
                               relief='flat',
                               height=3,
                               width=6,
                               font=24)
            button.grid(row=grid[0], column=grid[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, sign in OPERATORS.items():
            button = tk.Button(self.button_frame,
                               text=sign,
                               command=lambda function=operator: self.calc_logic.add_to_calculation(function),
                               fg='white',
                               bg='#2c2c2e',
                               activeforeground='white',
                               activebackground='#414142',
                               borderwidth=0,
                               relief='flat',
                               height=3,
                               width=6,
                               font=24
                               )
            button.grid(row=i, column=3, sticky=tk.NSEW)
            i += 1

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_decimal_button()
        self.create_remove_button()
        self.create_equal_button()

    def create_clear_button(self):
        button = tk.Button(self.button_frame,
                           text='C',
                           command=lambda: self.calc_logic.clear_calculation(),
                           fg='white',
                           bg='#2c2c2e',
                           activeforeground='white',
                           activebackground='#414142',
                           borderwidth=0,
                           relief='flat',
                           height=3,
                           width=6,
                           font=24
                           )
        button.grid(row=0, column=0, sticky=tk.NSEW)

    def create_remove_button(self):
        button = tk.Button(self.button_frame,
                           text='\u25C4',
                           command=lambda: self.calc_logic.delete_calculation(),
                           fg='white',
                           bg='#2c2c2e',
                           activeforeground='white',
                           activebackground='#414142',
                           borderwidth=0,
                           relief='flat',
                           height=3,
                           width=6,
                           font=24
                           )
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_decimal_button(self):
        button = tk.Button(self.button_frame,
                           text='%',
                           command=lambda: self.calc_logic.calculate_percent(),
                           fg='white',
                           bg='#2c2c2e',
                           activeforeground='white',
                           activebackground='#414142',
                           borderwidth=0,
                           relief='flat',
                           height=3,
                           width=6,
                           font=24
                           )
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equal_button(self):
        button = tk.Button(self.button_frame,
                           text='=',
                           command=lambda: self.calc_logic.evaluate_calculation(),
                           fg='white',
                           bg='#e69500',
                           activeforeground='white',
                           activebackground='#e89f19',
                           borderwidth=0,
                           relief='flat',
                           height=3,
                           width=6,
                           font=24
                           )
        button.grid(row=4, column=3, sticky=tk.NSEW)


if __name__ == "__main__":
    calc = CalculatorApp()
    calc.run()

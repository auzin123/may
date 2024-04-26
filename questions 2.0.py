import tkinter
import random

questions = [
    {
        'вопрос': 'Какой оператор умножает числа в Питоне?',
        'ответы': ['-', 'x', '*', '**'],
        'индекс правильного ответа': 2
    },
    {
        'вопрос': 'Какой из этих типов изменяемый?',
        'ответы': ['list', 'str', 'tuple', 'int'],
        'индекс правильного ответа': 0
    },
]


class App:
    def __init__(self, shuffle_quiestion) -> None:
            self.window = tkinter.Tk()
            self.window.option_add('*Font', ('Arial', 30))
            self.window.bind('<Escape>', lambda _: self.window.destroy)
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            self.window.geometry(f'{screen_width}x{screen_height}')
            '''
            self.main_frame = tkinter.Frame(self.window, bg='red')
            self.main_frame.place(
                relx=0.5,
                rely=0.5,
                anchor='center',
                width=1000,
                height=1000
                    )
            '''
            self.quiestion_index = 0
            self.right_anwers = 0
            self.wrong_anwers = 0
            self.shuffle_question = False
            self.start()
            self.window.mainloop()

    def start(self) -> None:
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0
        if self.shuffle_question:
            random.shuffle(questions)

    def show_question(self) -> None:
        question = questions[self.quiestion_index]
        tkinter.Label(self.main_frame, text=question['вопрос']).pack()
        for option in question['ответы']:
            tkinter.Button(self.main_frame,
                           text=option,
                           command=lambda _: self.on_button(option)
            ).pack


    def on_button(self, button_text) -> None:
        question = questions[self.quiestion_index]
        if button_text == question['ответ']
            self.right_anwers += 1
        else:
             self.wrong_anwers += 1

        for widget in self.main_frame.winfo_children():
             widget.destroy()


        self.quiestion_index += 1
        if self.quiestion_index < len(question):
            self.show_question
        else: 
            pass # когда кончились вопросы


App(shuffle_quiestion=True)
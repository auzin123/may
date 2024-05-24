import tkinter as tk



class Game:
    def __init__(self) -> None:
        # создать окно
        self.window = tk.Tk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')
        self.window.mainloop()
        self.start()
        # создание переменной отвечающая сообщения в бою
        '''
        self.combat_messages = tk.Listbox(self.window)
        self.combat_messages.insert(0, 'Вася')
        self.combat_messages.insert(tk.END, 'Ася')
        self.combat_messages.pack()
        '''
    def start(self):
        tk.Button(text='Начать игру').pack(side='right', ipadx=25, ipady=25)


Game()

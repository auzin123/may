'''
Изначально - 3 кнопки:
1 - начать игру
2 - настройки
3 - закончить игру

начать игру:
спрашивать ник
предыстория
обучение

'''
'''
print('━'*31)
print('                 ┃         _          ┃')
print('  НАЧАТЬ ИГРУ    ┃        ╱ ╲         ┃')
print('                 ┃       ╱   ╲        ┃')
print('                 ┃      ╱     ╲       ┃')
print('   НАСТРОЙКИ     ┃      │     │       ┃')
print('                 ┃      |  [] |       ┃')
print('                 ┃      |     |       ┃')
print('                 ┃      |  [] |       ┃')
print('  ЗАКОНЧИТЬ ИГРУ ┃     /       \      ┃')
print('                 ┃    /         \     ┃')
print('                 ┃   /           \    ┃')
print('━'*31)
'''
def menu():
    print('''   
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                           ┃         _          ┃
    ┃                           ┃        ╱ ╲         ┃
    ┃                           ┃       ╱   ╲        ┃
    ┃     1 - НАЧАТЬ ИГРУ       ┃      ╱ ( ) ╲       ┃
    ┃                           ┃      │     │       ┃
    ┃                           ┃      | ( ) |       ┃
    ┃     2 - НАСТРОЙКИ         ┃      |     |       ┃
    ┃                           ┃      | ( ) |       ┃
    ┃                           ┃      |     |       ┃
    ┃     3 - ЗАКОНЧИТЬ ИГРУ    ┃     /       \      ┃
    ┃                           ┃    /         \     ┃
    ┃                           ┃   /           \    ┃
    ┃                           ┃  ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''')
    option_menu = input('Что выбераем? ')
    if option_menu == '1':
        start_game()

def start_game():
    pass

def settings():
    pass

def finish():
    pass

menu()
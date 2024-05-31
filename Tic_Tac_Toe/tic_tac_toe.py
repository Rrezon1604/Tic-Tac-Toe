import tkinter as tk
from tkinter import *
import random


def home_page():
    def close_game():
        home_root.destroy()

    def play():
        home_root.destroy()
        play_game_page()

    home_root = tk.Tk()
    home_root.state('zoomed')
    home_root.title('Tic Tac Toe')
    home_root.config(bg='#4E0D71')

    space1 = tk.Label(home_root, text='', height=3, bg='#4E0D71')
    space1.pack()

    frame = tk.Frame(home_root)
    frame.config(highlightthickness=5,
                 highlightbackground='#AF0F1B', bg='blueviolet')
    frame.pack()

    tic_tac_toe_label = tk.Label(frame, text='Tic\n\nTac\n\nToe', font=(
        'Arival', 60), bg='#4E0D71', fg='white', highlightbackground='#05D5FF', highlightthickness=5)
    tic_tac_toe_label.grid(row=0, column=0, padx=20, pady=20)

    img = tk.PhotoImage(file='tic_tac_toe_img.PNG')
    tic_tac_toe_img = tk.Label(
        frame, image=img, highlightbackground='#AF0F1B', highlightthickness=5)
    tic_tac_toe_img.grid(row=0, column=1, padx=20, pady=20)

    space2 = tk.Label(home_root, text='', bg='#4E0D71')
    space2.pack()

    buttons_frame = tk.Frame(home_root)
    buttons_frame.config(
        bg='blueviolet', highlightbackground='#05D5FF', highlightthickness=5)
    buttons_frame.pack()

    play_game_button = tk.Button(
        buttons_frame, text='Play Game', width=10, font=('Arial', 20), bg='#2BCB12', command=play)
    play_game_button.grid(row=0, column=0, padx=35, pady=35)

    space_between = tk.Label(buttons_frame, text='\t', bg='blueviolet')
    space_between.grid(row=0, column=1, padx=35, pady=35)

    close_game_button = tk.Button(buttons_frame, text='Close Game', width=10,
                                  fg='white', font=('Arial', 20), bg='#CF1919', command=close_game)
    close_game_button.grid(row=0, column=2, padx=35, pady=35)

    home_root.mainloop()


def play_game_page():

    def next_turn(row, column):
        global player
        if buttons[row][column]['text'] == '' and check_winner() is False:
            if player == players[0]:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[1]
                    label.config(text=(players[1]+" Turn"))
                elif check_winner() is True:
                    label.config(text=(player[0] + ' Wins'))
                elif check_winner() == "Draw":
                    label.config(text=("Draw!"))
            else:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0] + " Turn"))
                elif check_winner() is True:
                    label.config(text=(players[1]+' Wins'))
                elif check_winner() == "Draw":
                    label.config(text=("Draw!"))

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]["text"] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="lime")
                buttons[row][1].config(bg="lime")
                buttons[row][2].config(bg="lime")
                return True
        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]["text"] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="lime")
                buttons[1][column].config(bg="lime")
                buttons[2][column].config(bg="lime")
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="lime")
            buttons[1][1].config(bg="lime")
            buttons[2][2].config(bg="lime")
            return True
        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="lime")
            buttons[1][1].config(bg="lime")
            buttons[2][0].config(bg="lime")
            return True
        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Draw"
        else:
            return False

    def empty_spaces():
        spaces = 9
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != '':
                    spaces -= 1
        if spaces == 0:
            return False
        else:
            return True

    def new_game():
        global player

        player = random.choice(players)
        label.config(text=player + " Turn")
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg='#F0F0F0')

    def close():
        window.destroy()
        home_page()

    window = tk.Tk()
    window.state('zoomed')
    window.config(bg='#4E0D71')

    window.title("Tic-TacToe")
    players = ["X", "O"]
    player = random.choice(players)
    buttons = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    label = Label(text=player + " Turn", font=('consolas', 40), width=15, highlightbackground='#AF0F1B',
                  highlightthickness=5)
    label.pack(side="top")

    space2 = tk.Label(text='', bg='#4E0D71')
    space2.pack()

    frame = Frame(window)
    frame.config(highlightthickness=5, highlightbackground='#AF0F1B')
    frame.pack()

    space3 = tk.Label(text='', bg='#4E0D71')
    space3.pack()

    buttons_frame = tk.Frame(window)
    buttons_frame.config(
        bg='blueviolet', highlightbackground='#05D5FF', highlightthickness=5)
    buttons_frame.pack()

    play_game_button = tk.Button(
        buttons_frame, text='Start New Game', width=15, font=('Arial', 20), bg='#2BCB12', command=new_game)
    play_game_button.grid(row=0, column=0, padx=35, pady=35)

    space_between = tk.Label(buttons_frame, text='\t', bg='blueviolet')
    space_between.grid(row=0, column=1, padx=35, pady=35)

    close_game_button = tk.Button(buttons_frame, text='Close Game', width=10,
                                  fg='white', font=('Arial', 20), bg='#CF1919', command=close)
    close_game_button.grid(row=0, column=2, padx=35, pady=35)

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text='', font=('consolas', 40), width=5, height=2,
                                          command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)

    window.mainloop()


home_page()

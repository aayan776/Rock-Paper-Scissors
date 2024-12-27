from tkinter import *
import random
root = Tk()
root.title("Rock Paper Scissors game")
root.geometry("500x500")
root.configure(bg = "light blue")
play_choice = ""
comp_choice = ""
#Labels
result_label = Label(root, text = "", font = ("Arial", 12), bg = "light blue")
label1 = Label(root, text = "Choice:", font = ("Arial", 12), bg = "light blue")
label2 = Label(root, text = "Player choice:", font = ("Arial", 12), bg = "light blue")
label3 = Label(root, text = "Computer:", font = ("Arial", 12), bg = "light blue")
#Functions
def calculate(play_choice):
    print("hellow")
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)
    label3.configure(text=f"Computer: {comp_choice}")
    if comp_choice == play_choice:
        result_label.configure(text = "Draw")
    elif comp_choice == "rock" and play_choice == "paper":
        result_label.configure(text = "Player win!")
    elif comp_choice == "paper" and play_choice == "scissors":
        result_label.configure(text = "Player win!")
    elif comp_choice == "scissors" and play_choice == "rock":
        result_label.configure(text = "Player win!")
    elif comp_choice == "rock" and play_choice == "scissors":
        result_label.configure(text = "Player lose!")
    elif comp_choice == "paper" and play_choice == "rock":
        result_label.configure(text = "Player lose!")
    elif comp_choice == "scissors" and play_choice == "paper":
        result_label.configure(text = "Player lose!")
def set_rock():
    play_choice = "rock"
    label2.configure(text = f"Player choice: {play_choice}")
    calculate(play_choice)
def set_paper():
    play_choice = "paper"
    label2.configure(text=f"Player choice: {play_choice}")
    calculate(play_choice)
def set_scissors():
    play_choice = "scissors"
    label2.configure(text=f"Player choice: {play_choice}")
    calculate(play_choice)
#Buttons
rock_button = Button(root, text = "Rock", command = set_rock)
paper_button = Button(root, text = "Paper", command = set_paper)
scissors_button = Button(root, text = "Scissors", command = set_scissors)
#Geometry
result_label.place(x = 225, y = 100)
label1.place(x = 100, y = 200)
label2.place(x = 100, y = 250)
label3.place(x = 100, y = 300)
rock_button.place(x = 200, y = 200)
paper_button.place(x = 250, y = 200)
scissors_button.place(x = 300, y = 200)
root.mainloop()
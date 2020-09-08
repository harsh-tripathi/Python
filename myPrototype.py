# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!
import random
i = 0
while i < 10 :
    List = ["s","w","g"]
    comp_sel = random. choice(List)
    per_sel = input("Enter your choice : ")
    if per_sel == "s" :
        if comp_sel == "s" :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So it's a DRAW!")
        elif comp_sel == "w" :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So you WON!")
        else :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So you LOST!")
    elif per_sel == "w" :
        if comp_sel == "s" :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So you LOST!")
        elif comp_sel == "w" :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So it's a DRAW!")
        else :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So you WON!")
    else :
        if comp_sel == "s" :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So you WON!")
        elif comp_sel == "w" :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So you LOST!")
        else :
            print("Computer Selected",comp_sel,"and you selected",per_sel)
            print("So it's a DRAW!")
    i = i+1
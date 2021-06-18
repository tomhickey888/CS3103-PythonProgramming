import turtle
import random
import time

#Generate and set up screen
s = turtle.getscreen()
turtle.ht()
turtle.title("The Turtle Race")

#Create player one turtle
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)

#Create player two turtle
player_two = player_one.clone()
player_two.color("purple")
player_two.penup()
player_two.goto(-200,-100)

#Create homes for turtles and send back to the starting line
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

while True:
    if player_one.pos() >= (300,100):
        print('Player One Wins!')
        player_two.penup()
        player_two.goto(-200,-100)
        player_two.ht()
        player_one.home()
        for i in range(40,800,100):
            player_one.home()
            player_one.dot(i)
        break

    elif player_two.pos() >= (300,-100):
        print('Player Two Wins!')
        player_one.penup()
        player_one.goto(-200,-100)
        player_one.ht()
        player_two.home()
        for i in range(40,800,100):
            player_two.home()
            player_two.dot(i)
        break

    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.randint(1,6)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.randint(1,6)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)

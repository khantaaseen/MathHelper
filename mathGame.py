#taaseen khan
#project 1

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sys import exit
import random
import subprocess
from difficulty import *
from operations import *
from fatigue import *

app = Flask(__name__)
app.config['SQLALHEMY_DATABASE_URL'] = 'sqlite.///test.db'

@app.route('/')

def index():
    return render_template('mathgame.html')

app.run(debug=True)

def swap(numbers, operation):
    
    numbers_t = numbers
    if operation == "-":
        if numbers_t[0] < numbers_t[1]:
            numbers_t = (numbers_t[1], numbers_t[0])
    elif operation == "/":
        if numbers_t[1] == 0:
            numbers_t = (numbers_t [0],1)
    return numbers_t


def evaluate(numbers, operation):
    
    answer = eval(str(numbers[0]) + operation + str(numbers[1]))
    return answer

def main():
    print()
    print("Difficulties:")
    print("---------------")
    print("1: single digit integers\n2: double digit integers\n3: triple digit integers")
    user_difficulty = int(input("Enter difficulty: "))
    correct = 0
    wrong = 0

    while True:
        print("\n1 = addition")
        print("2 = subtraction")
        print("3 = multiplication")
        print("4 = division")
        print("5 = random operation\n")
        user_operation = int(input("Enter desired operation 1-5, or -1 to exit: "))
        print()
        
        if user_operation == -1:
                print("Correct:\n", correct)
                print("Wrong:\n", wrong)
                print("Thanks for playing")
                exit()
        
        numbers = difficulty(user_difficulty)
        sign = operations(user_operation)
        numbers = swap(numbers, sign)
        
        print("What is", str(numbers[0]), "", sign, "", str(numbers[1]) + "?")
        
        answer = round(evaluate(numbers, sign))

        while True:
            user_answer = int(input("Enter an answer or -1 to exit: "))
            if user_answer == -1:
                print("Correct:\n", correct)
                print("Wrong:\n", wrong)
                print("Thanks for playing")
                exit()
                
            if answer == user_answer:
                print(fatigue(True))
                correct += 1
                break
            else:
                print(fatigue(False))
                wrong += 1
                continue
            
main()
            

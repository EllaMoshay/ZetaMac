import random
import time
import datetime
import threading

def countdown(seconds):
    total_seconds = seconds
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        time.sleep(1)
        total_seconds -= 1

def valid_input(user_answer):
    while not user_answer.isdigit():
        user_answer = input("Input a number: ")
    else:
        return int(user_answer)

def questions(seconds):
    correct_answers = 0
    start_time = time.time()
    while time.time() - start_time < seconds:
        correct = 0
        user_answer = 1
        random_symbol = random.randint(1, 4)
        random_number_one = random.randint(1, 100)
        random_number_two = random.randint(1, 10)
        random_number_one_string = str(random_number_one)
        random_number_two_string = str(random_number_two)
        if random_symbol == 1:
            print((random_number_one_string) + " + " + random_number_two_string)
            correct = random_number_one + random_number_two
            user_answer = input()
            user_answer = valid_input(user_answer)
            while correct != user_answer:
                user_answer = input("Try Again: ")
                user_answer = valid_input(user_answer)
            
            else:
                correct_answers += 1
        elif random_symbol == 2:
            print(random_number_one_string + " - " + random_number_two_string)
            correct = random_number_one - random_number_two
            user_answer = input()
            user_answer = valid_input(user_answer)
            while correct != user_answer:
                user_answer = input("Try Again: ")
                user_answer = valid_input(user_answer)
        
            else:
                correct_answers += 1
        elif random_symbol == 3:
            print(random_number_one_string + " * " + random_number_two_string)
            correct = random_number_one * random_number_two
            user_answer = input()
            user_answer = valid_input(user_answer)
            while correct != user_answer:
                user_answer = input("Try Again: ")
                user_answer = valid_input(user_answer)
            else:
                correct_answers += 1
        else:
            print(random_number_one_string + " / " + random_number_two_string)
            correct = int(round(random_number_one / random_number_two, 1))
            user_answer = input()
            user_answer = valid_input(user_answer)
            while correct != user_answer:
                user_answer = input("Try Again, Round down to the nearest whole number: ")
                user_answer = valid_input(user_answer) 
            else:
                correct_answers += 1
    print("Time's up! Game over")
    print("You answered", correct_answers, "questions correctly.")  
    
def zetamac():
    print("\nWelcome to Zetamac!!")
    print("\nThis is a fast-paced speed drill where you are given a set amount of time to solve as many problems as you can.")
    print("\nLet's Start!") #description

while True:  # Loop until the user decides to stop playing
    zetamac()
    seconds = input("Seconds? ")
    while not seconds.isdigit():
        seconds = input("Enter a number: ")
    seconds = int(seconds)
    while seconds > 800:
        seconds = int(input("Enter a number under 800: "))
    
    countdown_thread = threading.Thread(target=countdown, args=(seconds,))
    countdown_thread.start()

    questions(seconds)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!!!")
        break
        
        





        
  
    


        

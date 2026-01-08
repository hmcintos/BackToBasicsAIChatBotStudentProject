import numpy as np
import asyncio
import time

# For now ignore these imports as they are to do with the AI implementation I will walk you through it next class.
# import vertexai
# from vertexai.generative_models import GenerativeModel 
# from google.oauth2 import service_account

"""
In here you will make your menu functions. This function requires you to output to the console at least two options
1. a way to exit your program
2. a way to interact with the AI
3. anything else you wish to add feel free to do so. I recommend you make functions for most options. Exit does not need one
"""
def menu():
    print("This is where the menu should output") # python is a less wordy language than java. for example to print to the console you just need to use the print function not
                                                    # systenm.out.println() like you do in java
    

    
    # another important thing to note about python is that they do not use semi colons to denote different lines. just type out your code as you would normally and leave out semicolons. 
    # they are not needed

"""
In your code you will call this function when your user chooses to interact with your AI from your menu. So when you have built your menu make sure that you call it IF the CASE is 
the selection for ai interaction. 
"""
def AI():
    print("This is where we do AI things. For now we will leave it blank and we will build it up throughout the next couple classes.")

    # importantly python does not require a main to run your program. However to maintain good programming practices ours will have one as that is the standard in industry
    # under this function is where all the code to run your program will go. I have already put some example code below it. Follow the directions in the comments and you will be fine

async def main():

    menu()
    userInput = input("What is your name?: ") # this is how python handles user input using the input function with a string inside the parenthese you can ask a question and take in a response
                                                # much better than dealing with scanner right?
    print("Hi! " + userInput + " I hope you have a great day! if you need help figuring this assignment out don't worry, you're smart. \n Take a deep breath break the problem down and start by tackling the easiest bit first.")
    # when adding in variables to strings this works exactly like in java. 

    # once you have your menu working you will need to handle userinput and determine what choice they chose. Don't worry. in python there are multiple options
    
    # the if statement is one youre familiar with 
    userInput = input("Choose a number 1,2 or 3: ")

    if userInput == "1":
        print("You chose 1!")

    elif userInput == "2": # else if statements in python have been shortened to be elif
        print("You chose 2!")

    elif userInput == "3":
        print("You chose 3!")

    else:
        print("That wasn't one of the choices but great attempt at breaking the program!")
    
    # there is also a match case statement at your disposal
    userInput = input("Choose one of the three letters here. A, B, or C: ")
    match userInput.lower(): #.lower is used to take whatever input is given and make sure everything is lowercased

        case 'a': # just like in java we use single quotes '' to denot a single character
            print("You chose A")

        case 'b':
            print("You chose B")

        case 'c':
            print("You chose C")

        case _:
            print("Thats not one of the options. In Match case statements the _ character is a special character which denots anything not covered by the previous cases. \n It basically works like an Else statement.")
    # you may have noticed I haven't been specifying data types while writing this code. Thats because python is a smart coding language and typically will assume what datatype youre using
    # boolean values ar no exceptions lets look at a while loop using a boolean value

    running = True # for python just ensure that your True False choices have a capital T or F respectively and youre good to go on boolean values

    while(running == True):
        userInput("Would you like this loop to stop? (Y/N): ")
        match userInput.lower:
            case 'y':
                print("alright suit yourself loop de loop it is!")
                running == True
            case 'n':
                print("Fair enough I wouldn't want to loop either this is kind of a boring loop.")
                running == False
            case _:
                print("Thats not an option wanna try again? oh also do you remember what the _ character does in a match case statemet?")

    # alright I think thats everything I wanted to show you. For today focus on getting your menus done and have them set up so you can use the AI multiple times and exit when you wish
    # I think you know the answer to what youll need to do to make that work but if youre stuck heres a hint. How did we ensure that the code above ran through continuously until you wanted it to stop?
    # Figure that out and youll be on your way in no time to mastering python and making our AI helpers. 



if __name__ == "__main__":
    asyncio.run(main())
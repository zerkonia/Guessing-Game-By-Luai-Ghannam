#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
import os
import matplotlib.pyplot as plt

clear = lambda: os.system('cls') #on Windows System

value = 0
guess = 0
saved_guesses = []
old_guess = 0
iteration = 0
number_of_iterations = []
min_limit = 1
max_limit = 100
#deleting = False

clear()# Used to clear the dialog below for each new game.

print('Guessing Game Rules:')
print('1-If a player\'s guess is less than 1 or greater than 100, say "OUT OF BOUNDS"\n')
print('2-On a player\'s first turn, if their guess is:\n')
print('       2.1-within 10 of the number, return "WARM!"\n')
print('       2.2-further than 10 away from the number, return "COLD!"\n')
print('3-On all subsequent turns, if a guess is:\n')
print('       3.1-closer to the number than the previous guess return "WARMER!"\n')
print('       3.2-farther from the number than the previous guess, return "COLDER!"\n')
print('       3.3-If the new guess has the same difference as the previous one, return "The same"\n')
print('4-When the player\'s guess equals the number, tell them they\'ve guessed correctly by returning "HOT!!!" and how many guesses it took!\n')
print('5-Finaly, plot the game performance list.\n')
#Target value is saved:
value =  int(randint(min_limit,max_limit))
#print(value)
while(guess != value):
    iteration += 1
    number_of_iterations.append(iteration)
    old_guess = guess
    if iteration == 1:
        print('Enter a guess:')
        guess = int(input())
        saved_guesses.append(guess)
    else:
        print('Enter a new guess:')
        guess = int(input())
        saved_guesses.append(guess)
    if guess < min_limit or guess > max_limit:
        print('Out of Bound')
    else:
        if iteration == 1:
            if guess - value == 0:
                print('Solved in the first iteration!!!')
            elif abs(guess - value)<= 10:
                print('Warm')
            elif abs(guess - value)> 10:
                print('Cold')
            
        else:
            if abs(guess - value) < abs(old_guess - value) and guess != value:
                print('Warmer!')
            elif guess == value:
                print('HOT!!!')
            elif abs(guess - value) > abs(old_guess - value):
                print('Colder!')
            else:
                print('The same')
                
                
if iteration > 1:   
    
    print('Solved in {} iterations'.format(iteration))       
                
game_history = list(zip(number_of_iterations,saved_guesses))
print('Game performance:\n{}'.format(game_history))
print('guessing technique effectiveness = {r:1.3f}%, lower is better. Best possible score = {s:1.3f}%'.format(r = (iteration/value)*100, s=(1/value)*100))
plt.axline((0, value), (1, value), linewidth=2, color='r')
for (x, y) in game_history:
    plt.scatter(x, y)
plt.show()
    


# In[ ]:





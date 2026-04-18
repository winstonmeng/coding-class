#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 14:50:40 2025

question 1:which bear lives at the north pole?
Answer 1:polar bear

Question 2:which is the fastest land animal?
Answer 2:cheetah

Question 3:which is the largest animal?
Answer 3: blue whale
@author: winstonmeng
"""
def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            score = score + 1
            print('correct answer')
            still_guessing = False
        else:
            attempt = attempt + 1
            if attempt < 3:
                guess = input('Sorry.Wrong answer.Try again')
                
        if attempt == 3:
            print('the correct answer is ' + answer)
                
            
            
       
score = 0
guess1 = input('which bear lives at the north pole?')
check_guess(guess1,'polar bear')
guess2 = input('which is the fastest land animal?')
check_guess(guess2,'cheetah')
guess3 = input('which is the largest animal?')
check_guess(guess3,'blue whale')
print('your score is ' + str(score))


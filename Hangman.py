import random
import numpy as np
import os
import pandas as pd

board = ['''>>>>>>>>> Hagman <<<<<<<<<''', 
         '''
    +---+
    |   |
        |
        |
        |
    ========    
    ''',
        
        '''
    +---+
    |   |
    O   |
        |
        |
    ========         
        
        ''','''
    +---+
    |   |
    O   |
    |   |
        |
    ========        
        
        ''', '''
    +---+
    |   |
    O   |
   /|   |
        |
    ========         
        
        ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
    ========        
        
        ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
    ========          
        
        ''','''
        
    +---+
    |   |
    O   |
   /|\  |
   / \  |
    ========          
        
        ''']

class HangMan():
    
    def __init__(self, words, board):
        self.word = words[0]
        self.synonyms1 = words[1]
        self.synonyms2 = words[2]
        self.translated = words[3]
        self.board = board
    
    def guess(self):
        lifes = 6
        complet = False
        hangman = 1
        wrong_letters = []
        correct_letters = []
        synonyms1 = 0
        translated = 0
        self.hide_word()
        while complet == False and lifes > 0:
            self.letter = input('Write a letter or 1 for a synonyms or 2 for the translation:')
            if self.letter == '1':
                synonyms1+=1
            elif self.letter == '2':
                translated = 1
            elif self.letter in self.word.lower():
                print(f'Correct letter: {self.letter}')
                if self.letter not in correct_letters:
                    correct_letters.append(self.letter)
                x = [pos for pos, char in enumerate(self.word.lower())\
                     if char == self.letter]
                for j in x:
                    self.lista[j]=self.word[j]
            else:
                print(f'Incorrect letter: {self.letter}')
                lifes = lifes-1
                hangman +=1
                if self.letter not in wrong_letters:
                    wrong_letters.append(self.letter)
            if self.lista == list(self.word):
                complet=True
            os.system("clear")
            print(board[0])
            print(board[hangman])
            if synonyms1 > 0:
                print(f'Synonyms 1: {self.synonyms1}')
            if synonyms1 > 1:
                print(f'Synonyms 2: {self.synonyms2}')
            if translated == 1:
                print(f'In Spanish: {self.translated}') 
            print(f'Word with {len(self.word)} letters:')
            [print(x, end=' ') for x in self.lista]
            print('\n')
            print(f'''Correct letters: {correct_letters} Total = {len(correct_letters)}\nWrong letters: {wrong_letters} Total = {len(wrong_letters)}''')
            print('\n')
        if lifes == 0:
            self.hangman_over()
            
        else:
            self.hangman_won()
        
           
                
    def hangman_over(self):
        print(f'You Lose! The word was: {self.word}')
    def hangman_won(self):
        print(f'You Won! The word was: {self.word}')
    def hide_word(self):
        self.lista =[]
        for i in self.word:
            self.lista.append('_')
        
            
    def print_game_status(self):
        pass
    

def rand_word():
    df = pd.read_csv('words_synonyms.csv')
    y = random.randint(0,len(df.index))
    return list(df.iloc[y,:])

def main():
    game = HangMan(rand_word(), board)
    game.guess()

if __name__ == "__main__":
    main()

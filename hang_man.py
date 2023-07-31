 

#Word bank of animals
from hangman_words import word_list
#or import hangman_words...hangman_words.word_list
import random
choosen_word=random.choice(word_list)
#print(f"the choosen word is{choosen_word}")

n=len(choosen_word)
lives=6
end=False

from hangman_words import logo
print(logo)

display=[]
for i in range(n):
    display+="_"
print(display)

while not end:
    guess=input("Guess a word: ").lower()
    for i in range(n):
        letter=choosen_word[i]
        if letter==guess:
         display[i]=letter
          
    if guess not in choosen_word:
          lives-=1
          if lives==0:
              print("YOU LOOSE")
            
    print(display)
    if "_" not in display:
     end=True
     print("YOU WIN!!")
    from hangman_words import stages
    print(stages[lives])


        

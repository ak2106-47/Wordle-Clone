#Name - Apoorva Kumar
#College Enrollment Number - BT19CSE008
#Coditation Systems: Associate Software Developer | Assignment

import random, pygame, sys
from pygame.locals import *
pygame.init()

#initializing basic terms used in the program
white = (255,255,255)
yellow = (255,255,102)
grey = (211, 211, 211)
black = (0,0,0)
green=(0,255,0)
lightGreen=(153,255,204)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

winner = bigFont.render("You Win!",       True, lightGreen)
loser = bigFont.render("You Lose!",     True, lightGreen)
playAgain = bigFont.render("Play Again?", True, lightGreen)

#evaluating the guess made by the user
def checkGuess(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessByUser = [grey,grey,grey,grey,grey]#setting all default colour codes to grey, which will change later according to data entered by user

    for x in range(0,5):
        
        #condition for changing the value to yellow
        if userGuess[x] in word:
            guessByUser[x] = yellow
            
        #condition for changing the value to green
        if word[x] == userGuess[x]:
            guessByUser[x] = green

    list(userGuess)

    #drawing the recrangles required for the words to get displayed
    for x in range(0,5):
        renderList[x] = font.render(userGuess[x], True, black)
        pygame.draw.rect(window, guessByUser[x], pygame.Rect(60 +spacing, 50+ (turns*80), 50, 50))
        window.blit(renderList[x], (70 + spacing, 50 + (turns*80)))
        spacing+=80

    #final condition if the user gets the guess right
    if guessByUser == [green,green,green,green,green]:
        return True



def main():
    
    #randomly assigning a word
    file = open("words.txt","r")
    wordList = file.readlines()
    word = wordList[random.randint(0, len(wordList)-1)].upper()

    height = 600
    width = 500
    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    print(word)

    for x in range(0,5):
        for y in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60+(x*80), 50+(y*80), 50, 50),2)

    pygame.display.set_caption("Wordle!")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess+=event.unicode.upper()

                if event.key == K_RETURN and win == True:
                    main()

                #if user exceeds 6 turns then program terminates
                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

                if event.key == K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, window)
                    turns+=1
                    guess = ""
                    window.fill(black,(0,500, 500, 200))

        window.fill(black,(0,500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))
        
        #Displayed if user guesses the word correctly within 6 turns             
        if win == True:
            window.blit(winner,(90,200))
            window.blit(playAgain,(60,300))

        #Displayed if user is unable to guess the word correctly
        if turns == 6 and win != True:
            window.blit(loser,(90,200))
            window.blit(playAgain,(60,300))
        pygame.display.update()
        clock.tick(FPS)
main()

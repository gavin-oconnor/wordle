import random
from tabnanny import check
import pygame
pygame.font.init()


WIDTH = 560
HEIGHT = 670
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WORDLE")
font = pygame.font.Font(pygame.font.get_default_font(),60)

def draw_background_Square(win, x, y, color, text, text_rect):
    pygame.draw.rect(win, color, (10*(x+1)+100*x, 10*(y+1)+100*y, 100, 100))
    text_rect.center = (10*(x+1)+100*x+50,10*(y+1)+100*y+50)
    win.blit(text, text_rect)
    if(color == (0,0,0)):
        pygame.draw.rect(win, (255,255,255), (10*(x+1)+100*x, 10*(y+1)+100*y, 100, 100), 1)

def draw_back_back_squares(win):
    for y in range(6):
        for x in range(5):
            pygame.draw.rect(win, (255,255,255), (10*(x+1)+100*x, 10*(y+1)+100*y, 100, 100), 1)


def draw_letters(win, guesses, uc_guesses,curr_guess):
    for y in range(len(uc_guesses)):
        for x in range(len(uc_guesses[y])):
            text = font.render(uc_guesses[y][x].upper(), True, (255,255,255))
            text_rect = text.get_rect()
            if guesses[y][x].isupper():
                draw_background_Square(win, x, y, (83,141,78), text, text_rect)
            elif guesses[y][x].islower():
                draw_background_Square(win, x, y, (181,159,58), text, text_rect)
            else:
                draw_background_Square(win, x, y, (58,58,58), text, text_rect)
    y = len(uc_guesses)
    for x in range(len(curr_guess)):
        text = font.render(curr_guess[x].upper(), True, (255,255,255))
        text_rect = text.get_rect()
        draw_background_Square(win, x, y, (0,0,0), text, text_rect)



def draw(win,guesses,uc_guesses, curr_guess):
    win.fill((0,0,0))
    draw_back_back_squares(win)
    draw_letters(win,guesses,uc_guesses, curr_guess)
    pygame.display.update()


def game_loop():
    run = True
    row = 0
    guesses = []
    uc_guesses = []
    curr_guess = ""
    word, valid = get_word()
    print(word)
    while run:
        if(len(guesses) >= 6):
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if(checkValid(curr_guess,valid) != None):
                        row += 1
                        uc_guesses.append(curr_guess)
                        guesses.append(returnGuess(curr_guess,word))
                        curr_guess = ""
                    else:
                        curr_guess = ""
                if len(curr_guess) > 0:
                    if event.key == 8:
                        curr_guess = curr_guess[0:len(curr_guess)-1]
                if len(curr_guess) < 5:
                    if event.key == pygame.K_a:
                        curr_guess += "a"
                    if event.key == pygame.K_b:
                        curr_guess += "b"
                    if event.key == pygame.K_c:
                        curr_guess += "c"
                    if event.key == pygame.K_d:
                        curr_guess += "d"
                    if event.key == pygame.K_e:
                        curr_guess += "e"
                    if event.key == pygame.K_f:
                        curr_guess += "f"
                    if event.key == pygame.K_g:
                        curr_guess += "g"
                    if event.key == pygame.K_h:
                        curr_guess += "h"
                    if event.key == pygame.K_i:
                        curr_guess += "i"
                    if event.key == pygame.K_j:
                        curr_guess += "j"
                    if event.key == pygame.K_k:
                        curr_guess += "k"
                    if event.key == pygame.K_l:
                        curr_guess += "l"
                    if event.key == pygame.K_m:
                        curr_guess += "m"
                    if event.key == pygame.K_n:
                        curr_guess += "n"
                    if event.key == pygame.K_o:
                        curr_guess += "o"
                    if event.key == pygame.K_p:
                        curr_guess += "p"
                    if event.key == pygame.K_q:
                        curr_guess += "q"
                    if event.key == pygame.K_r:
                        curr_guess += "r"
                    if event.key == pygame.K_s:
                        curr_guess += "s"
                    if event.key == pygame.K_t:
                        curr_guess += "t"
                    if event.key == pygame.K_u:
                        curr_guess += "u"
                    if event.key == pygame.K_v:
                        curr_guess += "v"
                    if event.key == pygame.K_w:
                        curr_guess += "w"
                    if event.key == pygame.K_x:
                        curr_guess += "x"
                    if event.key == pygame.K_y:
                        curr_guess += "y"
                    if event.key == pygame.K_z:
                        curr_guess += "z"
        draw(window, guesses, uc_guesses, curr_guess)
    pygame.quit()

def get_word():
    words = []
    valid_words = []
    with open("list.txt","r") as f:
        words = f.readlines()
    for word in words:
        if(len(word) == 6):
            valid_words.append(word[:5].lower())
    return valid_words[random.randint(0,len(valid_words)-1)].lower(), valid_words

def checkValid(guess, valid):
    if len(guess) != 5:
        return None
    if guess not in valid:
        return None
    else:
        return guess

def returnGuess(guess, correct):
    guess.lower()
    correct.lower()
    temp = ""
    for i in range(5):
        if(guess[i] == correct[i]):
            temp += guess[i].upper()
        elif guess[i] in correct:
            temp += guess[i].lower()
        else:
            temp += "-"
    return temp

game_loop()




        
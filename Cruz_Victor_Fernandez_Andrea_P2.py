import pygame
import sys
from pygame.locals import *

# to delimit the movement of the frames
FPS = 60
clock = pygame.time.Clock()

# to execute pygame
pygame.init()

# main screen and size
screen1 = pygame.display.set_mode((1000, 650))

# icon and name
pygame.display.set_caption("M A R I O  I N V A S I O N")
icon = pygame.image.load("./images/black_bullet.png")
pygame.display.set_icon(icon)

# to start writing the name(name input)
namebox = ""

#images
mainscreen = ("./images/background.png")

# global for score 
score = 0

def menu():

    global namebox

    # loop that keeps the window active
    while True:

        # to delimit the movement of the frames
        clock.tick(FPS)

        # background
        background = pygame.image.load(mainscreen)
        screen1.blit(background, (0, 0))

        # font and fonts´sizes
        gamefont = pygame.font.Font("./images/mariofont.ttf", 50)
        gamefont2 = pygame.font.Font("./images/mariofont.ttf", 20)

        # caption background
        entryspace = pygame.image.load("./images/entryspace.png").convert_alpha()
        entryspace = pygame.transform.scale(entryspace, (800, 80))
        screen1.blit(entryspace, (95, 77))

        # displaying the name of the game
        gamename = gamefont.render("M A R I O  I N V A S I O N", 0, (255,255,255))
        screen1.blit(gamename, (110, 95))

        # entry space button
        entryspace = pygame.image.load("./images/entryspace.png").convert_alpha()
        entryspace = pygame.transform.scale(entryspace, (500, 5))
        screen1.blit(entryspace, (245, 230))

        # name box
        namebox1 = gamefont2.render(namebox, 0, (255, 255, 255))
        screen1.blit (namebox1, (500 - namebox1.get_width()//2, 210))

        # levels section
        levelsection = gamefont.render("levels", 0, (222, 89, 24))
        screen1.blit(levelsection, (160, 350))

        # about
        about = gamefont.render("about", 0, (222, 89, 24))
        screen1.blit(about, (640, 350))

        # mario image on menu to decorate
        mario = pygame.image.load("./images/right_mario.png").convert_alpha()
        mario = pygame.transform.scale(mario, (50, 50))
        screen1.blit(mario, (350, 330))
        screen1.blit(mario, (190, 480))

        # enemies on top of the menu to decorate
        greenturtle1 = pygame.image.load("./images/green_turtle1.png").convert_alpha()
        greenturtle1 = pygame.transform.scale(greenturtle1, (50, 50))
        screen1.blit(greenturtle1, (538, 10))
        grayturtle1 = pygame.image.load("./images/gray_turtle1.png").convert_alpha()
        grayturtle1 = pygame.transform.scale(grayturtle1, (50, 50))
        screen1.blit(grayturtle1, (418, 10))
        greenwizard = pygame.image.load("./images/green_cloud.png").convert_alpha()
        greenwizard = pygame.transform.scale(greenwizard, (50, 50))
        screen1.blit(greenwizard, (358, 10))
        brownturtle1 = pygame.image.load("./images/brown_turtle1.png").convert_alpha()
        brownturtle1 = pygame.transform.scale(brownturtle1, (50, 50))
        screen1.blit(brownturtle1, (298, 10))
        browncloud = pygame.image.load("./images/brown_cloud.png").convert_alpha()
        browncloud = pygame.transform.scale(browncloud, (50, 50))
        screen1.blit(browncloud, (478, 10))
        graycloud = pygame.image.load("./images/gray_cloud.png").convert_alpha()
        graycloud = pygame.transform.scale(graycloud, (50, 50))
        screen1.blit(graycloud, (598, 10))
        redturtle1 = pygame.image.load("./images/red_turtle1.png").convert_alpha()
        redturtle1 = pygame.transform.scale(redturtle1, (50, 50))
        screen1.blit(redturtle1, (658, 10))
        whitebullet = pygame.image.load("./images/white_bullet.png").convert_alpha()
        whitebullet = pygame.transform.scale(whitebullet, (50, 50))
        screen1.blit(whitebullet, (238, 10))
        cyanbullet = pygame.image.load("./images/cyan_bullet.png").convert_alpha()
        cyanbullet = pygame.transform.scale(cyanbullet, (50, 50))
        screen1.blit(cyanbullet, (718, 10))

        # images of the level buttons
        buttonlevel1 = gamefont2.render("level 1", 0, (255,255,255))
        screen1.blit(buttonlevel1, (100, 400))

        # button level 2
        buttonlevel2 = gamefont2.render("level 2", 0, (255,255,255))
        screen1.blit(buttonlevel2, (250, 400))

        # button level 3
        buttonlevel3 = gamefont2.render("level 3", 0, (255,255,255))
        screen1.blit(buttonlevel3, (400, 400))

        # checks if the player clicks the buttons
        for click in pygame.event.get():
             if click.type == KEYDOWN:
                if click.key == K_BACKSPACE:
                    namebox = namebox[:-1]
                else:
                    namebox += click.unicode
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # to read the click on the level 1 button
                 if mouse_x >= 100 and mouse_x <= 190:
                     if namebox != "":
                         if mouse_y >= 400 and mouse_y <= 470:
                             #first_level.main(namebox)
                             flag = 0

                 # to read the click on the level 2 button
                 if mouse_x >= 250 and mouse_x <= 340:
                     if namebox!="":
                         if mouse_y >= 400 and mouse_y <= 470:
                             #second_level.level2(namebox)
                             flag = 0

                 # to read the click on the level 3 button
                 if mouse_x >= 400 and mouse_x <= 490:
                     if namebox != "":
                         if mouse_y >= 400 and mouse_y <= 470:
                             #third_level.level3(namebox)
                             flag = 0

                 # to read the click on the entry name button
                 if mouse_x >= 320 and mouse_x <= 490:
                     if mouse_y >= 250 and mouse_y <= 300:
                         flag = 0

                # to read the click on the instructions button
                 if mouse_x >= 70 and mouse_x <= 190:
                     if mouse_y >= 546 and mouse_y <= 586:
                         #player_instructions.instruct()
                         flag = 0

                # to read the click on the information botton
                 if mouse_x >= 240 and mouse_x <= 350:
                     if mouse_y >= 550 and mouse_y <= 585:
                         #infoscreen.information()
                         flag = 0

        # entry name button
        buttonentry = gamefont.render("entry name", 0, (255,255,255))
        screen1.blit(buttonentry, (320, 240))

        # info button
        infobutton = gamefont2.render("info", 0, (255,255,255))
        screen1.blit(infobutton, (270, 546))

        # instructions button
        instructionsbutton = gamefont2.render("instructions", 0, (255,255,255))
        screen1.blit(instructionsbutton, (70, 546))

        # leaderboard button
        leaderboard = gamefont2.render("leaderboard", 0, (255,255,255))
        screen1.blit(leaderboard, (400, 546))

        # to make the display surface actually appear on the user’s monitor (changes)
        pygame.display.update()

menu()
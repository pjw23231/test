import pygame
import button

#load button images
def roding_img_button():
    logo_img = pygame.image.load('images/jj_logo.png').convert_alpha()
    return logo_img

# main
def main_img_button():
    start_img = pygame.image.load("images/button_start.png").convert_alpha()
    rules_img = pygame.image.load("images/button_rules.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    start_button = button.Button(420, 450, start_img, 1)
    rules_button = button.Button(420, 550, rules_img, 1)
    quit_button = button.Button(420, 650, quit_img, 1)
    return start_button, rules_button, quit_button

# rule_text
def rule_img_button():
    explain_img = pygame.image.load("images/rule_text.png").convert_alpha()
    rule_img = pygame.image.load("images/rule.png").convert_alpha()

    explain_button = button.Button(240, 170, explain_img, 1)
    rule = button.Button(190, 40, rule_img, 1)
    return explain_button, rule

# category
def category_img_button():
    category1 = pygame.image.load("images/cap1.png").convert_alpha()
    category2 = pygame.image.load("images/bus1.png").convert_alpha()
    category3 = pygame.image.load("images/scholarship1.png").convert_alpha()
    category4 = pygame.image.load('images/school1.png').convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()
    category1_button = button.Button(190, 30, category1, 1)
    category2_button = button.Button(610, 40, category2, 1)
    category3_button = button.Button(190, 370, category3, 1)
    category4_button = button.Button(610, 340, category4, 1)
    back_button = button.Button(460, 650, back_img, 1)

    return category1_button, category2_button, category3_button, category4_button, back_button

# quiz
def quiz_img_button():
    o_img = pygame.image.load("images/oo.png").convert_alpha()
    x_img = pygame.image.load("images/xx.png").convert_alpha()
    board_img = pygame.image.load("images/bb.png").convert_alpha()
    clock_img = pygame.image.load("images/clock.png").convert_alpha()
    heart_img = pygame.image.load('images/heart.png').convert_alpha()
    o_button = button.Button(140, 400, o_img, 1)
    x_button = button.Button(652, 400, x_img, 1)
    return o_button, x_button, board_img, clock_img, heart_img

# false
def false_img_button():
    wrong_answer_img = pygame.image.load("images/wronganswer.png").convert_alpha()
    next_img = pygame.image.load('images/next.png').convert_alpha()
    wrong_answer_button = button.Button(380, 190, wrong_answer_img, 1)
    next_button = button.Button(700, 600, next_img, 1) 
    return wrong_answer_button, next_button

# true
def true_img_button():
    answer_img = pygame.image.load("images/answer.png").convert_alpha()
    answer_button = button.Button(380, 200, answer_img, 1)
    return answer_button

# gameover
def gameover_img_button():
    main_img = pygame.image.load("images/main.png").convert_alpha()
    main_button = button.Button(420,550, main_img, 1)
    return main_button

# gameend
def gameend_img_button():
    end_img = pygame.image.load("images/end.png").convert_alpha()
    main_categories_img = pygame.image.load("images/main.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    main_categories_button = button.Button(40, 650, main_categories_img, 1)
    quit2_button = button.Button(780, 650, quit_img, 1)
    return end_img, main_categories_button, quit2_button

import pygame # 파이게임 라이브러리 호출
import random # 랜덤 라이브러리 호출
import quiz_text  # quiz_text 모듈화
from img import * # img 모듈화
from screen import *  # screen 모듈화
 
pygame.init() # 파이게임 초기화

# 화면 생성
SCREEN_WIDTH = 1024 # 화면 가로길이
SCREEN_HEIGHT = 768 # 화면 세로길이

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 디스플레이 화면 생성

pygame.display.set_caption("JUSIQ") # 창이름 설정

# 게임 변수
game_paused = False # game_paused: 초기화면 값
c = True  # c: 기본 문제 랜덤 호출 조건 변수
c1 = True # c1: 기본 퀴즈 사운드 호출 조건 변수
c2 = True # c2: 기본 베이스 사운드 호출 조건 변수
menu_state = "main" # 기본 메뉴 상태 값
num = 0

# 색깔 정의
TEXT_COL = (255, 255, 255)  
TEXT_Red = (255, 0, 0)      
TEXT_Blue = (0, 0, 255)
TEXT_Black = (0,0,0)

# time
counter = 15    # 기본 시간
time_delay = 1000   # 1초
timer_event = pygame.USEREVENT+1  
pygame.time.set_timer(timer_event, time_delay)  

#define fonts
font = pygame.font.SysFont("arialblack", 35)  # arialblack 폰트
font_1 = pygame.font.SysFont('나눔바른고딕',60,True,True) # 나눔바른고딕 폰트
font_2 = pygame.font.SysFont('나눔바른고딕',120,True,True) 
font_3 = pygame.font.SysFont('arialblack',30,True,True) 

# 텍스트 정의
font_name1 = font_1.render('대학 생활 정보', True,TEXT_COL) 
font_name2 = font_2.render('O',True,TEXT_Blue)  
font_name3 = font_2.render('X',True,TEXT_Red) 
font_name4 = font_1.render('퀴즈!',True,TEXT_COL) 
font_name5 = font_3.render('-jj.university-',True,TEXT_Black)

# 이미지
# 초기화면 
logo_img = roding_img_button()
# main화면 
start_button, rules_button, quit_button = main_img_button()
# rules화면 
explain_button, rule = rule_img_button()
# category화면 
category1_button, category2_button, category3_button, category4_button, back_button = category_img_button()
# quiz화면 
o_button, x_button, board_img, clock_img, heart_img = quiz_img_button()
# false화면
wrong_answer_button, next_button = false_img_button()
# true화면
answer_button = true_img_button()
# gameover화면
main_button = gameover_img_button()
# gameend화면
end_img, main_categories_button, quit2_button = gameend_img_button()

# basic sound
def basic_sound():
  pygame.mixer.music.load( "sounds/basic.mp3" )
  pygame.mixer.music.set_volume(0.7)
  pygame.mixer.music.play(-1)

# quiz sound
def quiz_sound():# (카테고리)
  pygame.mixer.music.load( "sounds/quiz.mp3" )
  pygame.mixer.music.play(-1)

# 정답 소리
def true_sound():
  global c1
  pygame.mixer.music.load("sounds/true.mp3" )
  pygame.mixer.music.play()
  c1 = True

# 오답 소리
def false_sound():
  global c1
  pygame.mixer.music.load("sounds/false.mp3" )
  pygame.mixer.music.play()
  c1 = True

# heart
heart = 3
def life_img(heart_img):
  if heart == 3:
    screen.blit(heart_img,(100, 60))
    screen.blit(heart_img,(160, 60))
    screen.blit(heart_img,(220, 60))
  if heart == 2:
    screen.blit(heart_img,(100, 60))
    screen.blit(heart_img,(160, 60))
  if heart ==1:
    screen.blit(heart_img,(100, 60))

# heart 감소
def minus_heart():
  global heart
  heart -= 1

# draw text on the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

# 글짜 줄 바꿈
def blit_text(surface, text, pos, font, color=pygame.Color('White')):
    words = text.split(' ')  # 문자열을 2차원 리스트에 넣음
    space = font.size(' ')[0]  # 띄어쓰기의 가로 크기
    print(space)
    max_width, max_height = surface.get_size()
    x, y = pos
    for word in words: # 불러온 리스트의 단어
      word_surface = font.render(word, 0, color) # 폰트지정
      word_width, word_height = word_surface.get_size()
      if x + word_width >= max_width: # 글자가 화면크기를 벗어 난다면
          x = pos[0]  # x값 초기화
          y += word_height  # 단어의 세로크기만큼 y값 추가
      surface.blit(word_surface, (x, y))  # 단어 화면에 띄우기
      x += word_width + space   # 띄어쓰기한 만큼의 가로크기를 더하여 글자의 x값 변경

# ox judgment
def ox_judgment(rn, ox, answer):
  if ox[rn][1] == 'o':
    if answer == 'o':
      menu_state = 'true'
      true_sound()
    elif answer == 'x':
      menu_state = 'false'
      false_sound()
  elif ox[rn][1] == 'x':
    if answer == 'x':
      menu_state = 'true'
      true_sound()
    elif answer == 'o':
      menu_state = 'false'
      false_sound()
  else:
    print('정답 :', ox[rn][1])
  return menu_state

# text_number
number = 0
def text_number():
  global number
  number += 1

# 문제 다시출력
def category_code(code):
  global menu_state
  if code == 1:
    menu_state = 'category1'
  if code == 2:
    menu_state = 'category2'
  if code == 3:
    menu_state = 'category3'
  if code == 4:
    menu_state = 'category4'

# 문제 중복 방지
def ox_random(ox):
    al_list=[]     # 뽑은 rn를 넣어 중복 방지해주는 리스트         
    for i in range(len(ox)):  # 문제리스트를 받은 변수를 매개변수에 넣어준다
      rn = random.randint(0, len(ox)-1) 
      while rn in al_list : # al_list안에 rn이 없는 동안 반복
        rn = random.randint(0, len(ox)-1) 
      al_list.append(rn)  # 뽑은 숫자를 리스트에 저장
    print(al_list)
    return al_list

# 카테고리 화면
def category(ox, al_list):
  global menu_state, c, c1, counter, heart, number, num# 전역변수 선언

  # 퀴즈 사운드
  if c1 == True:  
    quiz_sound()  
    c1 = False    

  # 이미지
  category_screen(screen, board_img, clock_img)
  text_life = 'LIFE :'
  draw_text(text_life, pygame.font.SysFont("malgungothic", 25), TEXT_COL, 45, 80)
  # time draw
  draw_text(str(counter), font, (255, 255, 255), 915, 75)
  # text draw
  blit_text(screen, ox[al_list[num]][0], (40, 130), pygame.font.SysFont("malgungothic", 40))
  # 남은 문제
  draw_text(f'남은 문제 : {5-number}', pygame.font.SysFont("malgungothic", 25), TEXT_COL, 400, 80)

  # 시간이 0이 될 때
  if counter == 0:  
    # c = True # 문제 다시 출력하기위한 변수
    counter = 15 # 다시 시간을 15초 줌
    false_sound()
    menu_state = 'false'  # false 화면으로 이동
    
  life_img(heart_img)

  # 하트가 0일 때
  if heart == 0:  # gameover 상황
    number = 0 # 값을 초기화
    heart = 3  # 값을 초기화
    menu_state = 'gameover'

  # 5판 이겼을 때
  if number == 5: # gameend 상황
    number = 0 # 값을 초기화
    heart = 3  # 값을 초기화
    menu_state = 'gameend'

  # o버튼 그림 및 클릭
  if o_button.draw(screen):
    answer = 'o'
    menu_state = ox_judgment(al_list[num], ox, answer)
    counter = 15  # 값을 15로 초기화

  # x버튼 그림 및 클릭
  if x_button.draw(screen):
    answer = 'x'
    menu_state = ox_judgment(al_list[num], ox, answer)
    counter = 15  # 값을 15로 초기화

  return al_list

#game loop
run = True  
while run:
  
  screen.fill((204, 153, 255)) # 화면 배경 색깔 지정

  # game_paused 변수가 True면 반응하도록 설정
  if game_paused == True:
    if c2 == True:
      basic_sound()
      c2 = False

    # 메인 화면 구성
    if menu_state == "main":
      main_screen(screen, font_name1, font_name2, font_name3, font_name4, font_name5)
      #draw pause screen buttons
      if start_button.draw(screen):
        menu_state = "start"
      if rules_button.draw(screen):
        menu_state = "rules"
      if quit_button.draw(screen):
        run = False

    # 스타트 버튼을 눌렀을 때
    if menu_state == 'start':
      # 각 카테고리 4개의 메인 이미지와 텍스트를 스크린에 띄움
      text1 = '학사 제도'
      draw_text(text1, pygame.font.SysFont("malgungothic", 40), TEXT_COL, 220, 251)    
      text2 = '통학 버스'
      draw_text(text2, pygame.font.SysFont("malgungothic", 40), TEXT_COL, 650, 251)
      text3 = '장학 제도'
      draw_text(text3, pygame.font.SysFont("malgungothic", 40), TEXT_COL, 210, 580)
      text4 = '캠퍼스 건물 '
      draw_text(text4, pygame.font.SysFont("malgungothic", 40), TEXT_COL, 620, 580)

      #draw pause screen buttons
      if category1_button.draw(screen): # 학사 제도 카테고리 버튼을 누르면
        menu_state = "category1"        # 학사 제도 카테고리의 퀴즈 문제 화면으로 전환
        num = 0
        ox1 = quiz_text.ox_academic_system_copy() # 값을 초기화
        commentary1 = quiz_text.ox_academic_system_commentary()
        # 퀴즈 랜덤 뽑기
        if c == True:
          al_list = ox_random(ox1)
          c = False
      if category2_button.draw(screen): # 통학 버스 카테고리 버튼을 누르면
        menu_state = "category2"        # 통학 버스 카테고리의 퀴즈 문제 화면으로 전환
        num = 0
        ox2 = quiz_text.ox_school_bus_copy()  # 값을 초기화
        commentary2 = quiz_text.ox_school_bus_commentary()
        # 퀴즈 랜덤 뽑기
        if c == True:
          al_list = ox_random(ox2)
          c = False
      if category3_button.draw(screen): # 장학 제도 카테고리 버튼을 누르면
        menu_state = "category3"        # 장학 제도 카테고리 퀴즈 문제 화면으로 전환
        num = 0
        ox3 = quiz_text.ox_scholarship_on_campus_copy() # 값을 초기화
        commentary3 = quiz_text.ox_scholarship_on_campus_commentary()
        # 퀴즈 랜덤 뽑기
        if c == True:
          al_list = ox_random(ox3)
          c = False
      if category4_button.draw(screen): # 캠퍼스 건물 카테고리 버튼을 누르면
        menu_state = "category4"        # 캠퍼스 건물 카테고리 퀴즈 문제 화면으로 전환
        num = 0   
        ox4 = quiz_text.ox_campus_building_copy() # 값을 초기화
        commentary4 = quiz_text.ox_campus_building_commentary()
        # 퀴즈 랜덤 뽑기
        if c == True:
          al_list = ox_random(ox4)
          c = False
      if back_button.draw(screen):
        menu_state = "main" 

    # 게임오버 화면 
    if menu_state == 'gameover':
      text_game = 'GAME'
      text_game2 = 'OVER'
      draw_text(text_game, pygame.font.SysFont("malgungothic", 100), (255,255,255), 370, 150)
      draw_text(text_game2, pygame.font.SysFont("malgungothic", 150), (255,255,255), 325, 250)
      if main_button.draw(screen):
        c1 = True
        c2 = True
        menu_state = 'main'
      if quit_button.draw(screen):
        run = False
    
    # 게임엔드 화면
    if menu_state == 'gameend':
      screen.blit(end_img,(260,170))
      if main_categories_button.draw(screen):
        c1 = True
        c2 = True
        menu_state = "main"
      if quit2_button.draw(screen):
        run = False

    if menu_state == 'category1':
      code = 1
      al_list = category(ox1, al_list)
    if menu_state == "category2":
      code = 2
      al_list = category(ox2, al_list)
    if menu_state == 'category3':
      code = 3 # 카테고리 코드
      al_list = category(ox3, al_list)
    if menu_state == 'category4':
      code = 4
      al_list = category(ox4, al_list)

    # 정답화면
    if menu_state == 'true':
      answer_button.draw(screen)
      text_true = '정답입니다.'
      draw_text(text_true, pygame.font.SysFont("휴먼모음t", 60), TEXT_COL, 380, 470)
      if counter == 15:
        counter = 3
      if counter == 0: 
        counter = 15 # 값 초기화
        c = True    # 값 초기화
        category_code(code) # 카테고리 코드에 따라 화면 지정
        text_number()
        num += 1    # 랜덤 리스트에서 값을 순서대로 뽑기 위한 값
      draw_text(str(counter), font, (255, 255, 255), 900, 24) # 카운터를 3으로 먼저 바꾸기 위해 나중에 실행

    # 오답화면
    if menu_state == 'false':
      text_false = '오답입니다'
      draw_text(text_false, pygame.font.SysFont("휴먼모음t", 60), TEXT_COL, 380, 470)
      wrong_answer_button.draw(screen)
      if code == 1:
        blit_text(screen, commentary1[al_list[num]][0], (40, 50), pygame.font.SysFont("malgungothic", 30))
      if code == 2:
        blit_text(screen, commentary2[al_list[num]][0], (40, 50), pygame.font.SysFont("malgungothic", 30))
      if code == 3:          
        blit_text(screen, commentary3[al_list[num]][0], (40, 50), pygame.font.SysFont("malgungothic", 30))
      if code == 4:
        blit_text(screen, commentary4[al_list[num]][0], (40, 50), pygame.font.SysFont("malgungothic", 30))

      if next_button.draw(screen):
        minus_heart() # 하트 감소
        c = True      # 값 초기화
        category_code(code) # 카테고리 코드에 따라 화면 지정
        num += 1      # 랜덤 리스트에서 값을 순서대로 뽑기 위한 값

    # 규칙 화면 
    if menu_state == "rules":
      rule.draw(screen)
      explain_button.draw(screen)
      if back_button.draw(screen):
        menu_state = "main"

  # 초기화면
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 260, 550)
    screen.blit(logo_img,(173,60))

  # event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False
    if event.type == timer_event:
      # menu_state의 상태가 category와 같을 때 counter를 -1해줌
      if menu_state == "category1":   
        counter -= 1                  
      if menu_state == "category2":
        counter -= 1
      if menu_state == "category3":
        counter -= 1
      if menu_state == "category4":
        counter -= 1
      # menu_state의 상태가 true 같을 때 counter를 -1해줌
      if menu_state == 'true':
        counter -= 1

  pygame.display.update()

pygame.quit()
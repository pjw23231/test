
def main_screen(screen, font_name1, font_name2, font_name3, font_name4, font_name5):
  screen.blit(font_name1,(350,80))
  screen.blit(font_name2,(370,180))
  screen.blit(font_name3,(470,180))
  screen.blit(font_name4,(600,220))
  screen.blit(font_name5,(385,380))

def category_screen(screen, board_img, clock_img):
  screen.blit(board_img,(13, 50))
  screen.blit(clock_img,(858, 75))
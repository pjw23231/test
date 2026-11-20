import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()	# 이미지 가로길이 얻기
		height = image.get_height()	# 이미지 세로길이 얻기
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))	# 새 크기로 표면 크기 조정 
		self.rect = self.image.get_rect()	# 이미지 표면의 직사각형 너비를 얻음
		self.rect.topleft = (x, y)	
		self.clicked = True	

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#마우스 클릭 반응
		if self.rect.collidepoint(pos):	# 마우스가 이미지 안에 있으면
			surface.blit(self.image, (self.rect.x+5, self.rect.y+5)) # 이미지 위치를 위 아래로 5씩 이동
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == True:	# 마우스 왼쪽 클릭시 이벤트 발생
				for event in pygame.event.get():	
					if event.type == pygame.MOUSEBUTTONUP:	# 마우스 버튼을 땠을 때
						self.clicked = False	
						action = True
	
		if pygame.mouse.get_pressed()[0] == 0:	# 마우스를 안누르고 있으면 
			self.clicked = True

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))	# 마우스가 이미지 안에 없으면 이미지 그리기 

		return action
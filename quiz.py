import pygame
from random import *
#################################################3
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요) 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 안에 튜플

# 화면 타이틀 설정
pygame.display.set_caption("Quiz01") # 게임 이름

# FPS
clock = pygame.time.Clock()
########################################################################################

# 1. 사용자 게임 초기화 ( 배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 화면 설정
background = pygame.image.load("C:\\Users\\USER\\Desktop\\PythonWorkspace\\Practice_Game01\\background.png")

# 게임 캐릭터 설정
character = pygame.image.load("C:\\Users\\USER\\Desktop\\PythonWorkspace\\Practice_Game01\\corgi.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

# 적 설정
enemy = pygame.image.load("C:\\Users\\USER\\Desktop\\PythonWorkspace\\Practice_Game01\\ddong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width-enemy_width)
enemy_y_pos = 0 

# 이동 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6
enemy_speed = 0.3

# 폰트 설정
game_font = pygame.font.Font(None, 40)


running = True
while running:
    dt = clock.tick(30)
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    character_x_pos += to_y * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos != screen_height - character_height:
        character_y_pos = screen_height - character_height

    if enemy_y_pos < screen_height:
        enemy_y_pos += enemy_speed * dt
    elif enemy_y_pos >= screen_height:
        enemy_x_pos = randint(0, screen_width-enemy_width)
        enemy_y_pos = 0 

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("게임 오버")
        running = False
    
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    if running == False:
        fin = game_font.render(str("!GAME OVER!"), True, (255,255,255))
        fin_size = fin.get_rect().size
        fin_width = fin_size[0]
        fin_height = fin_size[1]
        screen.blit(fin, (((screen_width/2)-(fin_width/2)),(screen_height/2-fin_height/2)))
    pygame.display.update() # 게임화면을 다시 그리기, 반드시 계속 호출해야함



# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# pygame 종료
pygame.quit()
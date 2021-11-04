import sys, pygame
from pygame.constants import K_UP
import random
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)





# Set the screen
size = 800, 850
screen = pygame.display.set_mode(size)
road = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Background (1).png")
def background():
    screen.blit(road, (0,0))

# Title and Icon
pygame.display.set_caption('Car Mania')
icon = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\car.png")
pygame.display.set_icon(icon)

# Car
player = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Car\racing-car(100x100).png")
def car(x,y):
    screen.blit(player, (x,y))

# Powerup
powerup_image = pygame.image.load(r'C:\Users\MSII\Desktop\Code\Game\Assets\Images\Effects\bullet_powerup 60x60.png')
bullet_image = pygame.image.load(r'C:\Users\MSII\Desktop\Code\Game\Assets\Images\Effects\bullet.png')
def powerup(x,y):
    screen.blit(powerup_image, (x + 15,y))
def fire(x,y):
    screen.blit(bullet_image, (x + 3,y))

# Explosion
explosion = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Effects\explosion 60x60.png")
def crash(x,y):
    screen.blit(explosion, (x + 20, y - 30))

# Collision
def isCollision(playerX, playerY, list):
    collision = False
    for i in range(len(list)):
        if abs(playerX - list[i][0]) < 50 and abs(playerY - list[i][1]) < 70:
            collision = True
            break
    if collision == True:
        return True
    else: 
        return False
# Game over
gameover_image = pygame.image.load(r'C:\Users\MSII\Desktop\Code\Game\Assets\Images\Effects\GameOver.png')
def gameover_screen():
    screen.blit(gameover_image, (200,200))

# Pause:
pause_button_image = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Effects\pause-button 150x150.png")
def pause_button():
    screen.blit(pause_button_image, (325, 325))

# Obstacles
car_1 = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Obstacles\car1.png")
car_2 = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Obstacles\car2.png")
police_car = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Obstacles\police-car.png")
road_block = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Obstacles\road-barrier.png")
rock = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Obstacles\rocks.png")
music_car = pygame.image.load(r"C:\Users\MSII\Desktop\Code\Game\Assets\Images\Obstacles\music car.png")
obs = [car_1, car_2, police_car, road_block, rock, music_car]
lanes_x = [30, 190, 510, 670]
all_lane = [30, 190, 510, 670]
howtofire = myfont.render('SPACE = FIRE', False, (255, 255, 255))
howtopause = myfont.render('P = PAUSE', False, (255, 255, 255))
again = myfont.render('Y = Play Again                 N = Quit', False, (255, 255, 255))
def Obstacle(image, x, y):
    screen.blit(image, (x + 5,y))


def spawn_obs1():
    # Obstacle 1
    obstacle1 = random.choice(obs)
    obs.remove(obstacle1)
    lane1_x = random.choice(lanes_x)
    lanes_x.remove(lane1_x)
    lane1_y = 0
    globals().update(locals())

def spawn_obs2():
    # Obstacle 2
    obstacle2 = random.choice(obs)
    obs.remove(obstacle2)
    lane2_x = random.choice(lanes_x)
    lanes_x.remove(lane2_x)
    lane2_y = 0
    globals().update(locals())

def spawn_obs3():
    # Obstacle 3
    obstacle3 = random.choice(obs)
    obs.remove(obstacle3)
    lane3_x = random.choice(lanes_x)
    lanes_x.remove(lane3_x)
    lane3_y = 0
    globals().update(locals())

def spawn_obs4():
    # Obstacle 4
    obstacle4 = random.choice(obs)
    obs.remove(obstacle4)
    lane4_x = random.choice(lanes_x)
    lanes_x.remove(lane4_x)
    lane4_y = 0
    globals().update(locals())

def spawn_powerup():
    pow_x = random.choice(all_lane)
    pow_y = 0
    globals().update(locals())



def spawn():
    
    obs = [car_1, car_2, police_car, road_block, rock, music_car]
    lanes_x = [30, 190, 510, 670]

    # Player
    playerX, playerY = 350, 680
    bullet_x, bullet_y = 0, 0
    score = 0
    my_score = myfont.render('', False, (0, 0, 0))
    bullet_num = myfont.render('', False, (0, 0, 0))
    speed = 3  
    num_power = 0
    first_move = False
    pause = False
    bullet = 'ready'
    spawn_obs1()
    spawn_obs2()
    spawn_obs3()
    spawn_obs4()
    spawn_powerup()
    lane1_y = 570
    lane2_y = 330
    lane3_y = 190
    pow_y = 640
    obs_coor = [[lane1_x, lane1_y], [lane2_x, lane2_y], [lane3_x, lane3_y], [lane4_x, lane4_y]]
    lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y]
    current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x]
    globals().update(locals())

def avoid_collision(x, y):
    for i in range(len(current_lanes_x)):
        if x == current_lanes_x[i]:
            if y < lanes_y[i]:
                dy = abs(y-lanes_y[i])
                while dy < 90:
                    y -= (100 - dy)
                    dy = abs(y-lanes_y[i])
    return y
# Game loop
running = True
spawn()
while running:
    

    # Game condition
    lane1_y, lane2_y, lane3_y, lane4_y = [obs_coor[i][1] for i in range(4)]
    lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y]
    current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x]
    obs_coor = [[lane1_x, lane1_y], [lane2_x, lane2_y], [lane3_x, lane3_y], [lane4_x, lane4_y]]
    collision = isCollision(playerX, playerY, (obs_coor))
    isPowerup = isCollision(playerX, playerY, [(pow_x, pow_y)])

    if isPowerup:
        num_power = 1
        bullet_num = myfont.render('Bullet: 1', False, (255, 255, 255))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keyboard Input
        if event.type == pygame.KEYDOWN:
            if not first_move:
                first_move = True
                lanes_x.append(350)
                score = 0
            if not collision:
                if event.key == pygame.K_UP:
                    playerY -= 70
                elif event.key == pygame.K_DOWN:
                    playerY += 70
                elif event.key == pygame.K_LEFT:
                    playerX -= 160
                elif event.key == pygame.K_RIGHT:
                    playerX += 160
            else:
                if event.key == pygame.K_y:
                    collision = False
                    spawn()
                if event.key == pygame.K_n:
                    running = False
            if num_power == 1 and not collision:
                if event.key == pygame.K_SPACE:
                    bullet = 'fire'
                    bullet_x, bullet_y = playerX, playerY
                    num_power = 0
                    bullet_num = myfont.render('Bullet: 0', False, (255, 255, 255))
                    spawn_powerup()
            if event.key == pygame.K_p:
                if pause == False:
                    pause = True
                else: 
                    pause = False
                    
        
    
    # Boundaries
    if playerX > 800:
        playerX = 670
    elif playerX < 0:
        playerX = 30
    elif playerY < 0:
        playerY = 50
    elif playerY > 700:
        playerY = 680

    # Obs limit:
    if lane1_y > 700:
        lanes_x.append(lane1_x)
        obs.append(obstacle1)
        spawn_obs1()
        lane1_y = avoid_collision(lane1_x, lane1_y)
        lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y]
        current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x]
        score += 10

    if lane2_y > 700:
        lanes_x.append(lane2_x)
        obs.append(obstacle2)
        spawn_obs2()
        lane2_y = avoid_collision(lane2_x, lane2_y)
        lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y]
        current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x]
        score += 10

    if lane3_y > 700: 
        lanes_x.append(lane3_x)
        obs.append(obstacle3)
        spawn_obs3()
        lane3_y = avoid_collision(lane3_x, lane3_y)
        lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y]
        current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x]
        score += 10
    
    if lane4_y > 700:
        lanes_x.append(lane4_x)
        obs.append(obstacle4)
        spawn_obs4()
        lane4_y = avoid_collision(lane4_x, lane4_y)
        lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y]
        current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x]
        score += 10
    

    if pow_y > 700:
        spawn_powerup()
        pow_y = avoid_collision(pow_x, pow_y)
        lanes_y = [lane1_y, lane2_y, lane3_y, lane4_y, pow_y] 
        current_lanes_x = [lane1_x, lane2_x, lane3_x, lane4_x, pow_x] 

    obs_coor = [[lane1_x, lane1_y], [lane2_x, lane2_y], [lane3_x, lane3_y], [lane4_x, lane4_y]]

    if bullet_y < 0:
        bullet = 'ready'
    
    # Score
    if first_move:
        my_score = myfont.render('Score: ' + str(score), False, (255, 255, 255))
    

    # Difficulty
    if score <= 200:
        speed = 3
    elif score > 200:
        speed = 5
    elif score >= 500:
        speed = 8
    elif score >= 1000:
        speed = 15
    elif score >= 2000:
        speed = 20
    
    # Screen
    screen.fill((0, 0, 0))
    background()
    obs_list = [obstacle1, obstacle2, obstacle3, obstacle4]
    for i in range(len(obs_coor)):
        if (bullet_x == obs_coor[i][0] and bullet == 'fire' and abs(obs_coor[i][1] - bullet_y) <= 90):
            obs_coor[i][1] = 800
            continue
        else:
            Obstacle(obs_list[i], obs_coor[i][0], obs_coor[i][1])
    
    car(playerX, playerY)
    if num_power == 0:
        powerup(pow_x, pow_y)
    if bullet == 'fire':
        fire(bullet_x, bullet_y)

    screen.blit(my_score, (0, 800))

    if not collision and not pause:
        for i in range(4):
            obs_coor[i][1] += speed
        
        pow_y += speed
        bullet_y -= 8
    if pause:
        pause_button()
    if collision:
        crash(playerX, playerY)
        gameover_screen()
        screen.blit(again, (315, 800))
    else:
        screen.blit(howtofire, (385, 800))
        screen.blit(howtopause, (650, 800))
        screen.blit(bullet_num, (210, 800))

        
        
    pygame.display.update()
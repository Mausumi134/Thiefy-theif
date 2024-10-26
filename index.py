
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_size = 600
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Thiefy Thief")

# Set up the game variables
thief_position = [100, 100]
police_position = [300, 300]
money_bags = [[200, 200], [400, 400], [50, 50], [550, 550], [100, 400], [400, 100]]
obstacles = [[250, 250], [350, 350], [150, 150], [450, 450], [50, 300], [300, 50], [550, 150], [150, 550]]
score = 0

# Load cartoon character icons
cell_size = 40

thief_icon = pygame.image.load('thief.png')
thief_icon = pygame.transform.scale(thief_icon, (cell_size, cell_size))

police_icon = pygame.image.load('police.png')
police_icon = pygame.transform.scale(police_icon, (cell_size, cell_size))

money_bag_icon = pygame.image.load('money_bag.png')
money_bag_icon = pygame.transform.scale(money_bag_icon, (cell_size, cell_size))

obstacle_icon = pygame.image.load('obstacle.png')
obstacle_icon = pygame.transform.scale(obstacle_icon, (cell_size, cell_size))



# Function to draw the game
def draw_game():
    # Draw thief
    window.blit(thief_icon, (thief_position[0], thief_position[1]))
    # Draw police
    window.blit(police_icon, (police_position[0], police_position[1]))
    # Draw money bags
    for money_bag in money_bags:
        window.blit(money_bag_icon, (money_bag[0], money_bag[1]))
    # Draw obstacles
    for obstacle in obstacles:
        window.blit(obstacle_icon, (obstacle[0], obstacle[1]))
    # Draw score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (10, 10))

# Function to move the thief
def move_thief(direction):
    global thief_position
    if direction == "up" and thief_position[1] > 0:
        thief_position[1] -= 20
    elif direction == "down" and thief_position[1] < window_size - 20:
        thief_position[1] += 20
    elif direction == "left" and thief_position[0] > 0:
        thief_position[0] -= 20
    elif direction == "right" and thief_position[0] < window_size - 20:
        thief_position[0] += 20

# Function to move the police
def move_police():
    global police_position
    if police_position[0] < thief_position[0]:
        police_position[0] += 10
    elif police_position[0] > thief_position[0]:
        police_position[0] -= 10
    if police_position[1] < thief_position[1]:
        police_position[1] += 10
    elif police_position[1] > thief_position[1]:
        police_position[1] -= 10

# Function to draw paths
def draw_paths():
    for i in range(0, window_size, 20):
        pygame.draw.line(window, (255, 255, 255), (i, 0), (i, window_size))
        pygame.draw.line(window, (255, 255, 255), (0, i), (window_size, i))

# Function to check collisions
def check_collisions():
    global score
    # Check collision with police
    if thief_position == police_position:
        return True
    # Check collision with money bags
    for money_bag in money_bags:
        if thief_position == money_bag:
            score += 100
            money_bags.remove(money_bag)
    # Check collision with obstacles
    for obstacle in obstacles:
        if thief_position == obstacle:
            return True
    return False

# Function to draw game over screen
def draw_game_over():
    window.fill((0, 0, 0))
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 150, window_size // 2 - 36))
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 50, window_size // 2 + 50))
    # pygame.display.update()
    # pygame.time.delay(2000)
    font = pygame.font.Font(None, 36)
    text = font.render("Press Enter to play again", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 120, window_size // 2 + 100))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    reset_game()
                else:
                    continue

# Function to reset game
def reset_game():
    global thief_position, police_position, money_bags, obstacles, score
    thief_position = [100, 100]
    police_position = [300, 300]
    money_bags = [[200, 200], [400, 400], [50, 50], [550, 550], [100, 400], [400, 100]]
    obstacles = [[250, 250], [350, 350], [150, 150], [450, 450], [50, 300], [300, 50], [550, 150], [150, 550]]
    score = 0
# Front page
background_image = pygame.image.load('background.jpg')

def draw_front_page():
    window.fill((0, 0, 0))
    window.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 72)
    text = font.render("Thiefy Thief", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 150, window_size // 2 - 100))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 100, window_size // 2 + 50))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
draw_front_page()
# Function to draw game over screen
def draw_game_over():
    window.fill((0, 0, 0))
    window.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, (255, 0, 0))
    window.blit(text, (window_size // 2 - 150, window_size // 2 - 36))
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 50, window_size // 2 + 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to play again", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 120, window_size // 2 + 100))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
                reset_game()
                

                main()
# Main game loop
def main():
    global thief_position, police_position, money_bags, obstacles, score
    thief_position = [100, 100]
    police_position = [300, 300]
    money_bags = [[200, 200], [400, 400], [50, 50], [550, 550], [100, 400], [400, 100]]
    obstacles = [[250, 250], [350, 350], [150, 150], [450, 450], [50, 300], [300, 50], [550, 150], [150, 550]]
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_thief("up")
                elif event.key == pygame.K_DOWN:
                    move_thief("down")
                elif event.key == pygame.K_LEFT:
                    move_thief("left")
                elif event.key == pygame.K_RIGHT:
                    move_thief("right")
        
        move_police()
        
        window.fill((0, 0, 0))
        draw_paths()
        draw_game()
        
        if check_collisions():
            draw_game_over()
            break
        elif len(money_bags) == 0:
            draw_win()
            break
        
        pygame.display.update()
        pygame.time.delay(100)

main()

# Function to draw win screen
def draw_win():
    window.fill((0, 0, 0))
    font = pygame.font.Font(None, 72)
    text = font.render("You Win!", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 120, window_size // 2 - 36))
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 50, window_size // 2 + 50))
    pygame.display.update()
    pygame.time.delay(2000)

# Front page
def draw_front_page():
    window.fill((0, 0, 0))
    font = pygame.font.Font(None, 72)
    text = font.render("Thiefy Thief", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 150, window_size // 2 - 100))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    window.blit(text, (window_size // 2 - 100, window_size // 2 + 50))
    pygame.display.update()

# Show front page
draw_front_page()
pygame.time.delay(2000)
# Wait for user to press a key
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            waiting = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_thief("up")
            elif event.key == pygame.K_DOWN:
                move_thief("down")
            elif event.key == pygame.K_LEFT:
                move_thief("left")
            elif event.key == pygame.K_RIGHT:
                move_thief("right")
    
    # Delay police movement
    pygame.time.delay(50)
    
    move_police()
    
    window.fill((0, 0, 0))
    draw_paths()
    draw_game()
    
    if check_collisions():
        draw_game_over()
        break
    elif len(money_bags) == 0:
        draw_win()
        break
    
    pygame.display.update()
    pygame.time.delay(100)


# Import Statements
import pygame
import time
import random

# Initialize Modules
pygame.init()

# Set Up the Game Window
dis_width = 400
dis_height = 300
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake (Python)')

# Initialize the Color Variables
colors = [
    (255,255,255), # White
    (255,0,0),     # Red
    (255,130,0),   # Orange
    (255,233,0),   # Yellow
    (120,190,33),  # Lime Green
    (0,255,0),     # Green
    (0,181,226),   # Light Blue
    (0,0,255),     # Blue
    (155,38,182),  # Violet
    (151,153,155)] # Gray
current_color = 0 # The current index of the selected color
black = (0,0,0)

# Initialize the Timer, Speed, and Size variables
clock = pygame.time.Clock()
snake_speed = 12
snake_block = dis_height / 30

# Set Whether or Not to Automatically Restart on Game Over during Autoplay
looping = False

# Set Whether or Not to Display the "Loop" and "Hide" Prompts during Autoplay
displayLoopText = True

# Set Up the Game Messages
font_style = pygame.font.SysFont('Impact', int(dis_height / 12.5))
finalscore_text = "SCORE: "
reset_text = "PRESS 'R' TO RESET"
quit_text = "[ESC] QUIT"
colors_text = "1-0: CHANGE COLORS"
bored_text = "[P] I'M BORED, PLAY FOR ME"
stop_text = "[P] STOP PLAYING FOR ME"
loop_text = "[L] LOOP"
hide_text = "[H] HIDE/SHOW"
looping_text = "[LOOPING]"
def message(msg,x,y):
    mesg = font_style.render(msg, True, colors[current_color])
    dis.blit(mesg, [x,y])

# Draw the Snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, colors[current_color], [x[0], x[1], snake_block, snake_block])

# Manage the Loop to Run and Reset the Game
def gameLoop():
    #Initialize the Game State Management variables
    game_over = False
    game_close = False

    # Initialize the Movement Variables
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    # Retrieve the global Color variable
    global current_color

    # Initialize the Snake and Score (Score is Used to Measure Snake Length)
    snake_List = []
    score = 0

    # Randomize Food Placement
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    food_placed = True

    while not game_over:
        # Handle the Game Over/Restart State
        while game_close==True:
            # Draw the current Game State
            dis.fill(black)
            pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
            draw_snake(snake_block, snake_List)
            message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
            # Print the Game Over Messages
            message(finalscore_text+str(score),(dis_width/2)-(font_style.size(finalscore_text+str(score))[0]/2), (dis_height/4))
            message(reset_text, (dis_width/2)-(font_style.size(reset_text)[0]/2), (dis_height/4) + font_style.size(reset_text)[1] + 16)
            message(quit_text, dis_width - font_style.size(quit_text)[0] - 8, dis_height - font_style.size(quit_text)[1] - 8)
            message(colors_text, 8, 8)
            message(bored_text, 8, dis_height - font_style.size(bored_text)[1] - 8)
            pygame.display.update()
            for event in pygame.event.get():
                # Quit if the "Close" Button is pressed
                if event.type==pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type==pygame.KEYDOWN:
                    # R: Reset the Game
                    if event.key==pygame.K_r:
                        gameLoop()
                    # P: Start Playing the Game Automatically
                    if event.key==pygame.K_p:
                        gameLoopAuto()
                    # Esc: Quit the Game
                    if event.key==pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    # 1-0: Change the Display Color
                    if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                        current_color = 0
                    if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                        current_color = 1
                    if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                        current_color = 2
                    if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                        current_color = 3
                    if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                        current_color = 4
                    if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                        current_color = 5
                    if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                        current_color = 6
                    if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                        current_color = 7
                    if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                        current_color = 8
                    if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                        current_color = 9
                        
        for event in pygame.event.get():
            # Quit if the "Close" Button is pressed
            if event.type==pygame.QUIT:
                game_over = True
            # Change the Snake's Direction when the Arrows are pressed.
            if event.type==pygame.KEYDOWN:
                # Left/A:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    # If "Right" is the Current Direction, Don't Allow Backwards Movement
                    if x1_change != snake_block:
                        x1_change = -snake_block
                        y1_change = 0
                # Right/D:
                elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    # If "Left" is the Current Direction, Don't Allow Backwards Movement
                    if x1_change != -snake_block:
                        x1_change = snake_block
                        y1_change = 0
                # Up/W:
                elif event.key==pygame.K_UP or event.key==pygame.K_w:
                    # If "Down" is the Current Direction, Don't Allow Backwards Movement
                    if y1_change != snake_block:
                        x1_change = 0
                        y1_change = -snake_block
                # Down/S:
                elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    # If "Up" is the Current Direction, Don't Allow Backwards Movement
                    if y1_change != -snake_block:
                        x1_change = 0
                        y1_change = snake_block
                # 1-0: Change the Display Color
                if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                    current_color = 0
                if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                    current_color = 1
                if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                    current_color = 2
                if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                    current_color = 3
                if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                    current_color = 4
                if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                    current_color = 5
                if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                    current_color = 6
                if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                    current_color = 7
                if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                    current_color = 8
                if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                    current_color = 9
        # If the Snake hits a Wall, Game Over.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Update the Snake's position
        x1 += x1_change
        y1 += y1_change
        # Refresh the Window
        dis.fill(black)
        # Draw the Food
        pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
        # Add Another Block to the Snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # Keep the Snake the Appropriate Length by Removing the First Element
        # The Snake is Essentially Drawn Backward, Relative to its Array Order and Perceived Movement Direction
        if(len(snake_List) > score + 1):
            del snake_List[0]
        # If the Head of the Snake has Collided With its Body Anywhere, Game Over.
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close = True
        # Draw the Snake
        draw_snake(snake_block, snake_List)
        # Draw the Score
        message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
        # Update the Window
        pygame.display.update()
        #If the Snake Collides with the Food, Increase the Score and Reset the Food
        if x1==foodx and y1==foody:
            score += 1
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # Make sure the Food is not under any part of the Snake body.
            food_placed = False
            while not food_placed:
                food_placed = True
                for x in snake_List:
                    if x == [foodx, foody]:
                        food_placed = False
                        # print("Replacing Food...") # Use this to test how often the Food has to be moved.
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        # Refresh "snake_speed" times per second (currently 12)
        clock.tick(snake_speed)

    # Uninitialize Everything
    pygame.quit()
    quit()

# Manage the Loop to Run the Game Automatically
def gameLoopAuto():
    #Initialize the Game State Management variables
    game_over = False
    game_close = False

    # Initialize the Movement Variables
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    # Retrieve the global Color variable
    global current_color

    # Initialize the Snake and Score (Score is Used to Measure Snake Length)
    snake_List = []
    score = 0

    # Randomize Food Placement
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    food_placed = True

    # Set Whether or Not to Automatically Restart on Game Over
    global looping

    # Set Whether or Not to Display the "Loop" and "Hide" Prompts
    global displayLoopText

    while not game_over:
        # Handle the Game Over/Restart State
        while game_close==True:
            # If the Game is Meant to Reset Automatically, Do So.
            if looping==True:
                gameLoopAuto()
            else:
                # Draw the current Game State
                dis.fill(black)
                pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
                draw_snake(snake_block, snake_List)
                message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
                # Print the Game Over Messages
                message(finalscore_text+str(score),(dis_width/2)-(font_style.size(finalscore_text+str(score))[0]/2), (dis_height/4))
                message(reset_text, (dis_width/2)-(font_style.size(reset_text)[0]/2), (dis_height/4) + font_style.size(reset_text)[1] + 16)
                message(quit_text, dis_width - font_style.size(quit_text)[0] - 8, dis_height - font_style.size(quit_text)[1] - 8)
                message(colors_text, 8, 8)
                message(stop_text, 8, dis_height - font_style.size(bored_text)[1] - 8)
                pygame.display.update()
                for event in pygame.event.get():
                # Quit if the "Close" Button is pressed
                    if event.type==pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.type==pygame.KEYDOWN:
                        # R: Reset the Game
                        if event.key==pygame.K_r:
                            gameLoopAuto()
                        # P: Stop Playing the Game Automatically
                        if event.key==pygame.K_p:
                            gameLoop()
                        # Esc: Quit the Game
                        if event.key==pygame.K_ESCAPE:
                            game_over = True
                            game_close = False
                        # 1-0: Change the Display Color
                        if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                            current_color = 0
                        if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                            current_color = 1
                        if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                            current_color = 2
                        if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                            current_color = 3
                        if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                            current_color = 4
                        if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                            current_color = 5
                        if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                            current_color = 6
                        if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                            current_color = 7
                        if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                            current_color = 8
                        if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                            current_color = 9

        #Check for User Input During Autoplay
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type==pygame.KEYDOWN:
                # ESC: Close the Game
                if event.key==pygame.K_ESCAPE:
                    game_over = True
                # L: Toggle the Autoplay Looping
                if event.key==pygame.K_l:
                    looping = not looping
                # H: Toggle Displaying Text Mid-Game
                if event.key==pygame.K_h:
                    displayLoopText = not displayLoopText
                # 1-0: Change the Display Color
                if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                    current_color = 0
                if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                    current_color = 1
                if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                    current_color = 2
                if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                    current_color = 3
                if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                    current_color = 4
                if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                    current_color = 5
                if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                    current_color = 6
                if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                    current_color = 7
                if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                    current_color = 8
                if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                    current_color = 9
        # If the Snake hits a Wall, Game Over.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Determine what direction to move the Snake in.
        # 
        # Refresh the Window
        dis.fill(black)
        # Draw the Food
        pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
        # Add Another Block to the Snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # Keep the Snake the Appropriate Length by Removing the First Element
        # The Snake is Essentially Drawn Backward, Relative to its Array Order and Perceived Movement Direction
        if(len(snake_List) > score + 1):
            del snake_List[0]
        # If the Head of the Snake has Collided With its Body Anywhere, Game Over.
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close = True
        # Draw the Snake
        draw_snake(snake_block, snake_List)
        # Draw the Score
        message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
        # If Not Being Hidden, Draw the "Loop" and "Hide" Prompts
        if displayLoopText==True:
            message(loop_text, 8, dis_height - font_style.size(loop_text)[1] - 8)
            message(hide_text, 24 + font_style.size(loop_text)[0], dis_height - font_style.size(hide_text)[1] - 8)
            # If Looping, Draw the Notification Message
            if looping==True:
                message(looping_text, dis_width - font_style.size(looping_text)[0] - 8, dis_height - font_style.size(looping_text)[1] - 8)
        # Update the Window
        pygame.display.update()
        #If the Snake Collides with the Food, Increase the Score and Reset the Food
        if x1==foodx and y1==foody:
            score += 1
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # Make sure the Food is not under any part of the Snake body.
            food_placed = False
            while not food_placed:
                food_placed = True
                for x in snake_List:
                    if x == [foodx, foody]:
                        food_placed = False
                        # print("Replacing Food...") # Use this to test how often the Food has to be moved.
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        # Refresh "snake_speed" times per second (currently 12)
        clock.tick(snake_speed)

    # Uninitialize Everything
    pygame.quit()
    quit()

# Start Running the Game
gameLoop()
import pygame
import random
import sys

class Pong_Status:
    def __init__(
        self,
        player1_score,
        player2_score,
        player1_hits,
        player2_hits
    ):
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.player1_hits = player1_hits
        self.player2_hits = player2_hits

    def equals(self,other_status) -> bool:
        if (
            self.player1_score == other_status.player1_score
            and
            self.player2_score == other_status.player2_score
            and
            self.player1_hits == other_status.player1_hits
            and
            self.player2_hits == other_status.player2_hits
        ):
            return True
        return False



class Pong:
    def __init__(self):
        # Initialization
        pygame.init()
        self.clock = pygame.time.Clock()

        #Main Window:
        self.screen_width = 1280
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption('Pong-RL')

        # Pong Ball:
        self.ball_size = 30
        self.ball = pygame.Rect(
            self.screen_width/2-self.ball_size/2,
            self.screen_height/2-self.ball_size/2,
            self.ball_size,self.ball_size
        )

        self.player_size_width = 10
        self.player_size_heigth = 140
        self.player1 = pygame.Rect(
            5,
            self.screen_height/2-self.player_size_heigth/2,
            self.player_size_width,
            self.player_size_heigth
        )

        self.player2 = pygame.Rect(
            self.screen_width-15,
            self.screen_height/2-self.player_size_heigth/2,
            self.player_size_width,
            self.player_size_heigth
        )

        self.bg_color = pygame.Color('grey12')

        self.color = (255,255,255)

        # Speed variables:
        self.STEP = 7
        self.ball_speed_x = self.STEP
        self.ball_speed_y = self.STEP
        

        self.player_speed_1 = 0
        self.player_speed_2 = 0
        self.player_speed = 0

        # Score
        self.player1_score = 0
        self.player2_score = 0
        self.font_obj = pygame.font.Font('freesansbold.ttf', 32)
        self.player1_hits = 0
        self.player2_hits = 0

        #Restarts
        self.restarts = 0
        self.reset=False


    def update_score(self):
        if self.ball.left <= 0 :
            self.player2_score += 1
        if self.ball.right >= self.screen_width:
            self.player1_score += 1
        return

    def ball_restart(self):
        # self.ball.center = (
        #     self.screen_width/2-self.ball_size/2+random.randint(-25,25),
        #     self.screen_height/2-self.ball_size/2+random.randint(-25,25))
        self.ball.center = (
            self.screen_width/2-self.ball_size/2+random.randint(-25,25),
            random.randint(self.ball_size,self.screen_height-self.ball_size))
        self.ball_speed_x *= random.choice((1,-1)) 
        self.ball_speed_y *= random.choice((1,-1)) 
        # self.ball_speed_x = random.randint(-25,25)
        # self.ball_speed_y = random.randint(-25,25)
        self.restarts += 1
        self.reset = True
        print("Reset, (X,Y)=({},{})".format(self.ball_speed_x,self.ball_speed_y))
        return 


    def ball_animation(self):
        # Move the ball:
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            if (self.reset):
                self.reset = False
                # self.ball_speed_x = self.STEP
                # self.ball_speed_y = self.STEP

            # Collisions with the sides of the screen:
            if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
                self.ball_speed_y *= -1
            if self.ball.left <= 0  or self.ball.right >= self.screen_width:
                self.update_score()
                self.ball_restart()
            
            if self.ball.colliderect(self.player1):
                self.player1_hits += 1
                self.ball_speed_x *= -1
            
            if self.ball.colliderect(self.player2):
                self.player2_hits += 1
                self.ball_speed_x *= -1
            return 



    def player_animation(self, p, ps):
        if p.bottom >= self.screen_height:
            p.bottom = self.screen_height
        if p.top <= 0:
            p.top = 0

        p.y += ps

    def update_status(self) -> Pong_Status:
        return Pong_Status(
            self.player1_score,
            self.player2_score,
            self.player1_hits,
            self.player2_hits
        )

    def move_player(self,player1:bool,up:bool):
        delta = self.STEP
        if up:
            # delta = self.STEP * -1
            if player1:
                #self.player1.top += delta
                # self.player_speed_1 -= delta
                self.player_animation(self.player1,delta*-1)
            else: 
                self.player_animation(self.player2,delta*-1)
        else:
            if player1:
                self.player_animation(self.player1,delta)
            else: 
                self.player_animation(self.player2,delta)

    def OnePlay(self):


        # self.player_animation(self.player1,self.player_speed_1)
        # self.player_animation(self.player2,self.player_speed_2)

        self.ball_animation()
        

        #Visuals:
        self.screen.fill(self.bg_color) # Clears the screen
        pygame.draw.rect(self.screen,self.color,self.player1) 
        pygame.draw.rect(self.screen,self.color,self.player2) 
        pygame.draw.ellipse(self.screen,self.color,self.ball) # Draws an ellipse inside the rectangle, so it is a ball in this case
        # Draw a line to separate the fields:
        pygame.draw.aaline(self.screen,self.color,(self.screen_width/2,0),(self.screen_width/2,self.screen_height))
        #The score:
        
        pygame.display.flip() # Draw everything in the loop        
        return self.update_status()

    def Play(self):
        previous_status = Pong_Status(0,0,0,0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_speed_2 += 7
                    if event.key == pygame.K_UP:
                        self.player_speed_2 -= 7
                    if event.key == pygame.K_s:
                        self.player_speed_1 += 7
                    if event.key == pygame.K_w:
                        self.player_speed_1 -= 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player_speed_2 -= 7
                    if event.key == pygame.K_UP:
                        self.player_speed_2 += 7
                    if event.key == pygame.K_s:
                        self.player_speed_1 -= 7
                    if event.key == pygame.K_w:
                        self.player_speed_1 += 7
            self.player_animation(self.player1,self.player_speed_1)
            self.player_animation(self.player2,self.player_speed_2)
            status = self.OnePlay()
            if (not status.equals(previous_status)):
                print(
                    "Score: P1:{} P2:{}, Hits: P1:{} P2:{}".format(
                                                status.player1_score,
                                                status.player2_score,
                                                status.player1_hits,
                                                status.player2_hits))
            previous_status = status
            self.clock.tick(60)         
import pygame
import sys
from pong import Pong
from pong import Pong_Status
from .sarsa import Sarsa

class Pong_AI:
    def __init__(self):
        self.game = Pong()
        self.left_paddle = self.game.player1
        self.right_paddle = self.game.player2
        self.ball = self.game.ball

    def test_ai(self):
        clock = pygame.time.Clock()
        previous_status = Pong_Status(0,0,0,0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_player(player1=True,up=True)
            if keys[pygame.K_s]:
                self.game.move_player(player1=True,up=False)
            status = self.game.OnePlay()
            if (not status.equals(previous_status)):
                print(
                    "Score: P1:{} P2:{}, Hits: P1:{} P2:{}".format(
                                                status.player1_score,
                                                status.player2_score,
                                                status.player1_hits,
                                                status.player2_hits))
            previous_status = status
            clock.tick(60)    

    def simple_ai(self):
        if self.game.player2.top > self.game.ball.y: 
            self.game.move_player(player1=False,up=True)
            return
        if self.game.player2.bottom < self.game.ball.y:
            self.game.move_player(player1=False,up=False)
            return

    def test_simple_ai(self):
        clock = pygame.time.Clock()
        previous_status = Pong_Status(0,0,0,0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_player(player1=True,up=True)
            if keys[pygame.K_s]:
                self.game.move_player(player1=True,up=False)
            if keys[pygame.K_UP]:
                self.game.move_player(player1=False,up=True)
            if keys[pygame.K_DOWN]:
                self.game.move_player(player1=False,up=False)
            self.simple_ai()
            status = self.game.OnePlay()
            if (not status.equals(previous_status)):
                print(
                    "Score: P1:{} P2:{}, Hits: P1:{} P2:{}".format(
                                                status.player1_score,
                                                status.player2_score,
                                                status.player1_hits,
                                                status.player2_hits))
            previous_status = status
            clock.tick(60) 


    def train_ai(self):

        pass

pai = Pong_AI()

#pai.test_ai()
pai.test_simple_ai()



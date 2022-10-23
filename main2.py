import pygame
from pong import Pong
from pong import Pong_Status

p = Pong()

p.Play()

# clock = pygame.time.Clock()
# previous_status = Pong_Status(0,0,0,0)
# while True:
#     status = p.OnePlay()
#     if (not status.equals(previous_status)):
#         print(
#             "Score: P1:{} P2:{}, Hits: P1:{} P2:{}".format(
#                                         status.player1_score,
#                                         status.player2_score,
#                                         status.player1_hits,
#                                         status.player2_hits))
#     previous_status = status
#     clock.tick(60)     
from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')

font.init()
f = font.Font(None, 70)
lose1 = f.render("PLAYER 1 LOSE!", 1, (255, 0, 0))
lose2 = f.render("PLAYER 2 LOSE!", 1, (255, 0, 0))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update(self, key1, key2):
        keys_pressed = key.get_pressed()
        if keys_pressed[key1] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[key2] and self.rect.y < 360:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_height)
        self.direction_x = 1
        self.direction_y = 1
    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.y < 1 or self.rect.y > 450:
            self.direction_y *= -1
        if sprite.collide_rect(self, player2):
            self.direction_x *= -1
        if sprite.collide_rect(self, player1):
            self.direction_x *= -1

player1 = Player('racket.png', 50, win_height-350, 5, 39, 136)
player2 = Player('racket.png', 650, win_height-350, 5, 39, 136)

ball = Ball('tenis_ball.png', 350, win_height-350, 2, 50, 50)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill([255, 165, 0])
        player1.reset()
        player2.reset()
        ball.reset()

        player1.update(K_w, K_s)
        player2.update(K_UP, K_DOWN)
        ball.update()

        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True
        if ball.rect.x > 700:
            window.blit(lose2, (200, 200))
            finish = True
        
        display.update()
        clock.tick(FPS)

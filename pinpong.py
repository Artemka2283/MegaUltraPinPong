from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x_player, y_player, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image)
                                     , (65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_player
        self.rect.y = y_player
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        button = key.get_pressed()
        if button[K_LEFT] and self.rect.x > 10:
            self.rect.x -=self.speed
        if button[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x +=self.speed
        if button[K_UP] and self.rect.y > 10:
            self.rect.y -=self.speed
        if button[K_DOWN] and self.rect.y < win_height - 50: 
            self.rect.y +=self.speed
clock = time.Clock()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
back = (1, 4, 88)
window.fill(back)
display.set_caption("Maze")
class Enemy(GameSprite):
    direction = "nalevo"
    def update(self):
        self.rect.y += self.speed
        global proshli
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            self.speed = randint(1,3)
            proshli += 1
game = True
while game:
    for knopka in event.get():
        if knopka.type == QUIT:
            game = False
    display.update()
    clock.tick(120)
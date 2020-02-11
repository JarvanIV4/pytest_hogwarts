# 飞机精灵模块
import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 600)   # 屏幕大小的常量
FRAME_PER_SEC = 60      # 刷新的频率
CREATE_ENEMY_EVENT = pygame.USEREVENT   # 创建敌机的定时器常量
file_path = "./../images/"
HERO_FIRE_EVENT = pygame.USEREVENT + 1  # 英雄发射子弹事件


class GameSprites(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprites):

    def __init__(self, is_alt=False):
        # is_alt 判断是否是另一张图像：True表示另一张图像，在屏幕的正上方,False表示第一张图像，需要与屏幕重合
        super().__init__(file_path + "background.png")  # 调用父类方法实现精灵的创建
        # 判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法调用
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprites):

    def __init__(self):
        super().__init__(file_path + "enemy1.png")      # 调用父类方法创建精灵和精灵组
        self.speed = random.randint(1, 3)       # 设置敌机的初始随机速度1~3
        self.rect.bottom = 0    # 设置敌机的垂直y初始位置
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)  # 设置敌机的水平随机位置

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # 敌机飞出屏幕，需要从精灵组删除敌机
            self.kill()     # 将精灵从所有组中删除，精灵就会被自动销毁

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprites):
    """英雄精灵"""

    def __init__(self):
        super().__init__(file_path + "me1.png")
        self.speed = 0
        self.rect.centerx = SCREEN_RECT.centerx     # 英雄机水平位置
        self.rect.bottom = SCREEN_RECT.bottom - 100  # 英雄机垂直位置
        self.bullet_group = pygame.sprite.Group()    # 创建子弹精灵组

    def update(self):
        self.rect.x += self.speed   # 英雄机水平方向移动

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 发射子弹
        for i in (0, 1, 2):
            bullet = Bullet()  # 创建子弹精灵
            bullet.rect.bottom = self.rect.y - i*20    # 设置子弹精灵初始位置
            bullet.rect.centerx = self.rect.centerx
            self.bullet_group.add(bullet)    # 将精灵添加到精灵组


class Bullet(GameSprites):

    def __init__(self):
        super().__init__(file_path + "bullet1.png", -2)
        self.speed = -1

    def update(self):
        # 调用父类方法，让子弹沿垂直方法飞行
        # 判断子弹是否飞出屏幕
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass



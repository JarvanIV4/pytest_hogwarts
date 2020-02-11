import pygame
from 练习.pygame_test.src.plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)    # 创建游戏的窗口
        self.clock = pygame.time.Clock()    # 创建游戏的时钟
        self.__create_sprites()    # 创建精灵和精灵组
        self.hero_speed = 3     # 英雄机水平移动速度
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 设置定时器创建敌机，每隔1s创建一辆敌机
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)      # 英雄机发射子弹定时器,每隔0.5s发射一颗子弹

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)   # 创建背景图片精灵组
        self.enemy_group = pygame.sprite.Group()        # 创建敌机精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)       # 创建英雄精灵组

    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(FRAME_PER_SEC)  # 设置刷新帧率
            self.__event_handler()      # 事件监听
            self.__check_collide()      # 碰撞检测
            self.__update_sprites()     # 更新/绘制精灵组
            pygame.display.update()     # 更新显示

    def __event_handler(self):
        # 事件监听
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        # 获取键盘按键 - 返回键盘元组
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            print("向右移动")
            self.hero.speed = self.hero_speed
        elif key_pressed[pygame.K_LEFT]:
            print("向左移动")
            self.hero.speed = -self.hero_speed
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 碰撞检测
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)    # 子弹摧毁敌机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)  # 敌机撞毁英雄机
        if len(enemies) > 0:
            # 判断列表是否有内容
            self.hero.kill()  # 将英雄精灵从精灵组删除
            self.__game_over()  # 结束游戏

    def __update_sprites(self):
        # 更新/绘制精灵组
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
import pygame

pygame.init()
file_path = "./../images/"
screen = pygame.display.set_mode((480, 700))    # 绘制窗口
background = pygame.image.load(file_path + "background.png")  # 加载图像数据
screen.blit(background, (0, 0))  # 绘制图像
pygame.display.update()  # 更新屏幕显示

hero = pygame.image.load(file_path + "me1.png")  # 加载英雄飞机
# screen.blit(hero, (180, 500))
pygame.display.update()
click = pygame.time.Clock()
hero_rect = pygame.Rect(150, 500, 102, 126)
while True:

    click.tick(60)      # 设置屏幕刷新帧率
    # # 监听事件
    # for event in pygame.event.get():
    #     #
    #     if event.type == pygame.quit():
    #         print("退出游戏")
    #         pygame.quit()
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    hero_rect.y -= 1
    # 判断飞机的位置 bottom = y + height
    if hero_rect.bottom < 0:
        hero_rect.y = 700
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()
# pygame.quit()
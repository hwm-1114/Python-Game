'''
1. 搭建初始框架，绘制场景
第一步就是搭建一个初始界面，包括
设置界面的size
设置关闭界面事件
设置帧频
页面背景渲染
更新页面
'''
import pygame
import random

# 游戏初始化
pygame.init()

# 游戏窗口大小
window_width = 800
window_height = 600

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 设置游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇')

'''
2.绘制蛇头，食物和蛇身的位置
'''
# 蛇头坐标
snake_x = window_width / 2
snake_y = window_height / 2

# 蛇身列表
snake_body = [[snake_x, snake_y]]

# 食物坐标
food_x = round(random.randrange(0, window_width - 20) / 20) * 20
food_y = round(random.randrange(0, window_height - 20) / 20) * 20






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

'''
3.游戏循环
显示玩家得分
创建字体对象，出现字体颜色
渲染背景表面，分数更新
为文本表面对象创建一个矩形对象，文本在此刷新
不断更新蛇身，以及分数
'''

# 初始分数
score = 0

# 蛇移动速度
snake_speed = 20

# 方向
direction = 'RIGHT'

# 游戏结束标志
game_over = False

# 游戏时钟
clock = pygame.time.Clock()

# 游戏循环
# 原点在左上角，所以y轴的正方向是向下的
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
    
    if direction == 'LEFT':
        snake_x -= snake_speed
    elif direction == 'RIGHT':
        snake_x += snake_speed
    elif direction == 'UP':
        snake_y -= snake_speed
    elif direction == 'DOWN':
        snake_y += snake_speed
    

    # 绘制背景
    window.fill(black)

    # 绘制蛇身
    # pygame.draw.rect是用来绘制矩形的函数
    # window是绘图的目标窗口
    # [segment[0], segment[1], 20, 20]表示矩形的左上角x坐标，y坐标，宽度和高度
    for segment in snake_body:
        pygame.draw.rect(window, green, [segment[0], segment[1], 20, 20])
    
    # 绘制食物
    pygame.draw.rect(window, red, [food_x, food_y, 20, 20])

    # 更新蛇身
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > score + 1:
        del snake_body[0]
    
    # 检测蛇与食物的碰撞
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = round(random.randrange(0, window_width - 20) / 20) * 20
        food_y = round(random.randrange(0, window_height - 20) / 20) * 20
        

    # 检测蛇头与蛇身的碰撞:
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True
    
    # 检测蛇是否超出边界
    if snake_x <= 0 or snake_x >= window_width or snake_y <= 0 or snake_y >= window_height:
        game_over = True
    
    # 刷新游戏窗口
    # 调用该函数可以确保实时更新图像，显示动画和响应用户输入，确保游戏画面的流畅性和即时性
    pygame.display.update()

    # 控制游戏频率
    # 每秒钟执行10帧
    # 限制程序的运行速度，确保每秒钟只执行10次程序代码
    clock.tick(10)

# 游戏结束，退出
pygame.quit()

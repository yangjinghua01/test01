__author__ = 'tzhou'
import sys

from settings import Settings
import pygame
from pygame.sprite import Group
from ship import Ship
import game_functions as gf
from alien import Ailen
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings,screen, "Play")

    # 创建一艘飞船,一个子弹编组和一个外星人编组
    ship=Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets=Group()

    aliens = Group()
    # 创建外星人群
    gf.creat_fleet(ai_settings,screen,ship,aliens)


    #设置背景色
    bg_colar=(230,230,230)
    #开始游戏的主循环

    #创建一个外星人
    #alien=Ailen(ai_settings,screen)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建存储游戏统计信息的实例，并创建计分牌
    sb = Scoreboard(ai_settings, screen, stats)
    while True:
        # 监视键盘和鼠标事件
        # gf.check_events(ship)
        gf.check_events(ai_settings, screen,stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            #让最近绘制的屏幕可见

            bullets.update()
            # 删除已消除的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_alien(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # gf.update_screen(ai_settings,screen,ship,alien,bullets)
            print(len(bullets))
        gf.update_screen(ai_settings,screen, stats, sb, ship,aliens,
                         bullets, play_button)

run_game()
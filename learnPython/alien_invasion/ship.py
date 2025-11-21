import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""
    def __init__(self, ai_game):
        super().__init__()
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += speed
        if self.moving_left and self.rect.left > 0:
            self.x -= speed
        if self.moving_up and self.rect.top > 0:
            self.y -= speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += speed
        self.rect.x = self.x  
        self.rect.y = self.y  
            
                 
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
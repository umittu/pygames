#モジュールのインポート
import pygame
import sys
import math

#色の定義
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GOLD  = (255, 216,   0)
SILVER= (192, 192, 192)
COPPER= (192, 112,  48)

#メイン処理を行う函数
def main():
    #pygameモジュールの初期化
    pygame.init()
    #ウィンドウに表示されるタイトルを指定
    pygame.display.set_caption("初めてのpygame描画")
    #スクリーンの初期化
    screen = pygame.display.set_mode((800,600))
    #clockオブジェクトの作成
    clock = pygame.time.Clock()
    #時間を管理する変数の宣言
    tmr = 0

    #無限ループ
    while True:
        #tmrの値を1増やす
        tmr = tmr + 1
        #pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            #ウィンドウの×ボタンをクリックした時
            if event.type == pygame.QUIT:
                #pygameモジュールの初期化を解除
                pygame.quit()
                #プログラムの終了
                sys.exit()

        #指定した色でスクリーン全体をクリアする
        screen.fill(BLACK)

        #線の描画
        pygame.draw.line(screen,RED,[0,0],[100,200],10)
        pygame.draw.lines(screen,BLUE,False,[[50,300],[150,400],[50,500]])
        #矩形の描画
        pygame.draw.rect(screen,RED,[200,50,120,80])
        pygame.draw.rect(screen,GREEN,[200,200,60,180],5)
        #多角形の描画
        pygame.draw.polygon(screen,BLUE,[[250,400],[200,500],[300,500]],10)
        #円の描画
        pygame.draw.circle(screen,GOLD,[400,100],60)
        #楕円の描画
        pygame.draw.ellipse(screen,SILVER,[400-80,300-40,160,80])
        pygame.draw.ellipse(screen,COPPER,[400-40,500-80,80,160],20)
        #円弧の角度の計算
        ang = math.pi*tmr/36
        #円弧の描画
        pygame.draw.arc(screen,BLUE,[600-100,300-200,200,400],0,math.pi*2)
        pygame.draw.arc(screen,WHITE,[600-100,300-200,200,400],ang,ang+math.pi/2,8)

        #画面を更新する
        pygame.display.update()
        #フレームレートを指定
        clock.tick(10)

#このプログロムが直接実行された時に
if __name__ == '__main__':
    #main()函数を呼び起こす
    main()

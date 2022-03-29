#モジュールのインポート
import pygame
import sys

#色の定義
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#メインの処理を行う函数
def main():
    #pygameモジュールの初期化
    pygame.init()
    #ウィンドウに表示されるタイトルを指定
    pygame.display.set_caption("初めてのpygameキー入力")
    #スクリーンの初期化
    screen = pygame.display.set_mode((800,600))
    #clockオブジェクトの作成
    clock = pygame.time.Clock()
    #フォントオブジェクトの作成
    font = pygame.font.Font(None,60)

    #無限ループ
    while True:
        #pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            #ウィンドウの×ボタンを押した時
            if event.type == pygame.QUIT:
                #pygameモジュールの初期化解除
                pygame.quit()
                #プログラムを終了する
                sys.exit()

        #リストkeyに全てのキーの状態を代入
        key = pygame.key.get_pressed()
        #方向キー上下のリストの値を描いたsurface
        txt1 = font.render("UP"+str(key[pygame.K_UP])+"DOWN"+str(key[pygame.K_DOWN]),True,WHITE,GREEN)
        #方向キーの左右リストの値を描いたsurface
        txt2 = font.render("LEFT"+str(key[pygame.K_LEFT])+"RIGHT"+str(key[pygame.K_RIGHT]),True,WHITE,BLUE)
        #スペースキーとEnterキーのリストの値を描いたsurface
        txt3 = font.render("SPACE"+str(key[pygame.K_SPACE])+"ENTER"+str(key[pygame.K_RETURN]),True,WHITE,RED)

        #指定した色でスクリーン全体をクリアする
        screen.fill(BLACK)
        #文字列を描いたsurfaceをスクリーンに転送
        screen.blit(txt1,[100,100])
        screen.blit(txt2,[100,200])
        screen.blit(txt3,[100,300])
        #画面を更新する
        pygame.display.update()
        #フレームレートを指定
        clock.tick(10)

#このプログラムが直接実行された時に
if __name__ == '__main__':
    #main()函数を呼び出す
    main()

#モジュールのインポート
import pygame
import sys

#色の定義
BLACK = (  0,   0,   0)
LBLUE = (  0, 192, 255)
PINK  = (255,   0, 224)

#メインの処理を行う函数
def main():
    #pygameモジュールの初期化
    pygame.init()
    #ウィンドウに表示されるタイトルを指定
    pygame.display.set_caption("初めてのpygameマウス入力")
    #スクリーンの初期化
    screen = pygame.display.set_mode((800,600))
    #clockオブジェクトの作成
    clock = pygame.time.Clock()
    #フォントオブジェクトを作成
    font = pygame.font.Font(None,60)

    #無限ループ
    while True:
        #pygameのイベントを繰り返し処理
        for event in pygame.event.get():
            #ウィンドウの×ボタンを押した時に
            if event.type == pygame.QUIT:
                #pygameモジュールの初期化
                pygame.quit()
                #プログラムを終了する
                sys.exit()

        #マウスポインタの座標を変数に代入
        mouseX,mouseY = pygame.mouse.get_pos()
        #座標の値を描いたsurface
        txt1 = font.render("{},{}".format(mouseX,mouseY),True,LBLUE)
        #マウスボタンの状態を変数に代入
        mBtn1,mBtn2,mBtn3 = pygame.mouse.get_pressed()
        #マウスボタンの状態を描いたsurface
        txt2 = font.render("{}:{}:{}".format(mBtn1,mBtn2,mBtn3),True,PINK)
        #指定した色でスクリーン全体をクリアする
        screen.fill(BLACK)
        #文字列を描いたsurfaceをスクリーンに転送
        screen.blit(txt1,[100,100])
        screen.blit(txt2,[100,200])
        #画面を更新する
        pygame.display.update()
        #フレームレートを指定
        clock.tick(10)

#このプログラムが直接実行された時
if __name__ == '__main__':
    #main()函数を呼び起こす
    main()
#モジュールのインポート
import pygame
import sys

#色の定義
WHITE = (255,255,255)
BLACK = (0,0,0)

#メイン処理を行う函数
def main():
    #pygameモジュールの初期化
    pygame.init()
    #ウィンドウに表示されるタイトルを指定
    pygame.display.set_caption("初めてのPygame")
    #スクリーンを初期化
    screen =pygame.dispay.set_mode((800,600))
    #clockオブジェクトを作成
    clock = pygame.time.Clock()
    #フォントオブジェクトを作成
    font = pygame.font.Font(None,80)
    #時間を管理する変数の設定
    tmr = 0

    #無限ループ
    while True:
        #tmrの値を1増やす
        tmr = tmr + 1
        #pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            #ウィンドウの×ボタンをクリックした時に
            if event.type == pygame.QUIT:
                #pygameモジュールの初期化を解除
                pygame.quit()
                #プログラムを終了
                sys.exit()

        #surfaceに文字列を描く
        txt = font.render(str(tmr),True,WHITE)
        #指定した色でスクリーン全体をクリアする
        screen.fill(BLACK)
        #文字列を描いたsurfaceをスクリーンに転送
        screen.blit(txt,[300,200])
        #画面の更新
        pygame.display.update()
        #フレームシフトを指定
        clock.tick(10)

#このプログラムが直接実行された時に
if __name__ == '__main__':
    #main()函数を呼び出す
    main()
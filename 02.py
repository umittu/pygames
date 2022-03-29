#モジュールのインポート
import pygame
import sys

#メイン処理を行う函数
def main():
    #pygameモジュールの初期化
    pygame.init()
    #ウィンドウに表示されるタイトルを指定
    pygame.display.set_caption("初めてのpygame画像表示")
    #スクリーンの初期化
    screen=pygame.display.set_mode((640,360))
    #clockオブジェクトを作成
    clock=pygame.time.Clock()
    #背景画像の読み込み
    img_bg=pygame.image.load("pg_bg.png")
    #キャラクター画像の読み込み
    img_chara=[pygame.image.load("pg_chara0.png"),pygame.image.load("pg_chara1.png")]
    #時間を管理する変数の宣言
    tmr=0

    #無限ループ
    while True:
        #tmrの値を増やす
        tmr = tmr + 1
        #pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            #ウィンドウの×ボタンをクリックした時
            if event.type == pygame.QUIT:
                #プログラムを終了する
                sys.exit()
            #キーを押すイベントが発生した時に
            if event.type == pygame.KEYDOWN:
                #F1キーならば
                if event.key == pygame.K_F1:
                    #フルスクリーンモードにする
                    screen = pygame.display.set_mode((640,360),pygame.FULLSCREEN)
                #F2キーかEscキーならば
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    #通常表示に戻す
                    screen = pygame.display.set_mode((640,360))
        #背景スクリーン用の値をtmrから求める
        x = tmr%160
        #繰り返しで横に5枚分の
        for i in range(5):
            #背景画像を描画
            screen.blit(img_bg,[i*160-x,0])
            #キャラクターをアニメーションさせて描画
            screen.blit(img_chara[tmr%2],[224,160])
            #画面を更新する
            pygame.display.update()
            #フレームレートを指定
            clock.tick(5)

#このプログラムが直接実行された時に
if __name__ == '__main__':
    #main()函数を呼び出す
    main()



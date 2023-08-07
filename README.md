#ファイルの説明
-weapon.py
    - main page. 起動したときに開かれるpage. 防具のdataframeをいじるstreamlit
- pages
    - streamlitで別のpageを入れるためのフォルダ．streamlitのファイル名の頭に<01_><02_>とつけることでpageの順番を決められる
    - 中身
        - 01_armor.py
            - 防具のdataframeをいじるstreamlit
        - 02_accessary.py
            - 装飾のdataframeをいじるstreamlit
- ryuon-equipment-38a59fa0f789.json
    - 流用禁止，スプレッドシートにアクセスし，sobiフォルダのcsvを更新するためのもの．今は直接読み取るために使っている
- requirements.txt
    - Streamlit Cloudに公開するために必要なライブラリとバージョンそのバージョンをまとめたファイル
    
以下動作には関係なし
- version.py
    - requirements.txtを書くための結果を出力するもの．動作環境によって書き換えられたくないのでファイルの書き換えではなく，結果の出力のみにしてある
- log.yml
    - 過去のvol03,04での試行をまとめたもの．経緯や制作意図も含めてこのREADMEより詳細なことが書いているので，むしろそちらを確認してほしい
- create_csv.py
    - 今回は不要．sobiフォルダにスプレッドシートをcsvにして出力するためのもの(今はスプレッドシートから直接datafreamにしている)
- sobi 
    - databaseの保管場所(だった)
    - 中身
        - ksr_accesary.csv
        - ksr_weapon.csv
        - ksr_armor.csv
        - ssr_accesary.csv
        - ssr_weapon.csv
        - ssr_armor.csv
        - ability-category.csv #装備を検索するためのカテゴリをまとめたもの
- test.ipynb
    - 私がバグ検証等に使っていた作業ファイル．邪魔なら消してください
    
#streamlitの起動の仕方

'ryuon_sobi_streamlit_vol05'のディレクトリ内で以下のコードを実行するとローカルでStreamlit
が起動します．

'''
streamlit run weapon.py
'''

#バグ内容
1. ステータスとレアリティを同時に処理すると何故かエラーを起こす
2.フィルタ項目をチェックしたまま他のページに行くと以下のようなバグが起きる(流石に今回直そう)
    - 最初からそのチェック項目に沿った出力になってしまう
        - 例: 武器のページでステータスの防御力だけをフィルタしたときに，防具のページに移動すると防御力がフィルタされたDatafreamが出力される
    -　絞らないのチェックが入っているのに，前のフィルタ項目が出力されている
        - 上に関連して初期状態ではラジオボタンが全て絞らないに設定されている．前のページでフィルタをかけた状態で移動するとその項目が出力された状態になっている(ラジオボタンは絞らないになっている)
        - page切り替える時に自動でキャッシュクリアする方法がいい？
            - cache_clearというのがあるらしいが使い方がわからなかった
        


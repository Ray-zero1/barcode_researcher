## 入退室調査の無人化
---------------------------------------------------------------
Raspberry piによりバーコードから誰がバーコードをかざしたかを確認するために作られたリポジトリです。

# Usage
 
 バーコードをかざしていくと、番号が蓄積され、最後に設定したバーコードをかざすとCSVファイルができるようになっています。
 その、CSVファイルをLibreOfficeにて開き、一行目に蓄積されたデータがあるので、それをコピーして、別に作ったExcelファイルに読み込むと、誰がバーコードをかざしたかがわかリマス。
# Note
 
 そのままでは使えません。
 電源を入れたらすぐにプログラムが起動するように設定させてください
 <br>参考：https://qiita.com/karaage0703/items/ed18f318a1775b28eab4
 <br>上記ではなく、こちらを参考にしてください→https://qiita.com/tonosamart/items/f59daa481f90c85a8a99
 <br>desktopの拡張子ファイルは
  ```
  cd .config
  mkdir autostart
  cd autostart
  ```
  この/home/pi/.config/autostartに置くと自動実行できます
  
# 物品例
　３大隊の例
  - ２次元バーコード： https://www.amazon.jp/dp/B084JPWS3X?ref=ppx_pop_mob_ap_share
  - Raspberry pi model3:https://www.amazon.jp/dp/B07K4DN1SJ?ref=ppx_pop_mob_ap_share
  - Raspberry pi用モニター:https://www.amazon.jp/dp/B07RZW9CWP?ref=ppx_pop_mob_ap_share
  - モバイルバッテリー　10000mAぐらいの
  - microSDカード　16G以上
  
# 開発方法　
  1. Rasbbian を　microSDカードにインストールする。
    LibreOfficeのCalcを使うため、ソフトウェアが全部入っているのをダウンロードするのがおすすめ
  2. Githubに入っているlunch.pyのファイルを作成する。
  　場所は、home/piにlunchというフォルダを作成し、その中にlunch.pyを作成する。
   また、Terminalを開いて、lunch.pyがあるフォルダに行き,
    ```
    python3 lunch.py
    ```
    と打ってみて動作するか確認。
 　 ここまでで、プログラムの作成は完了。
    次からは、自動起動させるための操作。
  3. 上記のNoteより自動起動させるためのファイルを作成していく。
  　 参考用にこのリポジトリにもファイルを作成してある。
  4. Lunch-Surveyのエクセルファイルの名簿を書き換えた者を作成し、それをUSB等でラズパイに入れる。
  5. 最後に、再起動させてみてファイルが動作するか確認する。
 
  　
  

 

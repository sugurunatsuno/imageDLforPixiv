#imageDLforPixiv

##Overview
pixivから画像を収集します  

##Discription
pixivのユーザーの投稿したすべての画像を保存するプログラムです。  
以下のパラメータを用意しています。  
--user_id : 対象のユーザーのID、必須  
--path : 保存するディレクトリ、必須  
--userdata_json : pixivにログインするためのID、passwordが書かれたjsonファイル、必須  
jsonファイルには以下のように記述されているものとする  
{"username":"exampleuser", "password":"12345678"}  
--score : 投稿されている画像を保存するときのスコアの整数値の閾値、オプション  
これより下のスコアは保存されない、デフォルトは700　　
##Requirement
python3以降  
pixivpy3 (pip install pixivpy)  

##Usage
以下のように記述  

python pixiv_dl.py --user_id 123456 --path image/ --userdata_json userdata.json

閾値を任意の値に設定  
python pixiv_dl.py --user_id 123456 --path image/ --userdata_json userdata.json --score 2000  

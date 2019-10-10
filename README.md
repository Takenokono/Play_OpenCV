# OpenCVで遊んでみた
本レポジトリは、OpenCVを使って面白おかしい実験を行なっています。随時追加していきます。

## 注意
実行する前に、`pip install -r requirements.txt`を実行して下さい。必要なモジュールがインストールされます。(仮想環境等はご自身でお願いします)

## 1.face_detecter.py
　顔を検知して青色の四角で囲むプログラムです。

## 2.face_mosic.py
　顔を検知してモザイクをかけます。

## 3.face_gaussianBlur.py
　顔の部分に、ガウシアンフィルターによる平滑化を行います。

## 4.BinaryWorld.py
　2値化された動画を出力します。

## 5.images_mosic.py
　コマンドライン引数でImagesディレクトリ内の画像ファイル名を与えて、顔にモザイクを入れたバージョンを保存します。（Imagesディレクトリ内に)

## 6.detect_edge.py
　canny法によるエッジ検出を簡易的に実装しました。
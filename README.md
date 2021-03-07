# Classを活用した簡単なレジシステムの構築
Classを使い、小売店などにあるレジシステムの簡易版を作成します。
難しそうに見えますが、やることは四則演算とfor、ifによる処理のみです。
Classが理解できると、大規模なプログラムをキレイに構築することができるようになります。
ソースコードもプロっぽさが増します＾＾

Classの基本：https://www.tech-teacher.jp/blog/python-class/<br>

# １
オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください

# ２
オーダーをコンソール（ターミナル）から登録できるようにしてください
登録時は商品コードをキーとする

# ３
商品マスタをCSVから登録できるようにしてください

# ４
オーダー登録時に個数も登録できるようにしてください

# ５
オーダー登録した商品の一覧（商品名、価格）を表示し、かつ合計金額、個数を表示できるようにしてください

# ６
お客様からのお預かり金額を入力しお釣りを計算できるようにしてください

# ７
課題５、６の内容を、日付時刻をファイル名としたレシートファイル（テキスト）に出力できるようにしてください



【自分メモ】
2021年3月6日　課題04開始


【参考サイト】
・復習：if __name__ == "__main__":　⇒　https://blog.pyq.jp/entry/Python_kaiketsu_180207

【疑問に思ったこと、理解した内容】
●疑問点（課題1）
item_master.append(Item("001","りんご",100))　というitem_masterへの情報追加において、
それぞれの引数3つの情報が、コード、商品名、金額であることをどこで認識しているか。

●理解した内容
appendの際に、Itemクラスを呼び出しているので、Itemクラスの
def __init__(self,item_code,item_name,price):
の通り、それぞれの情報が紐づけされている。
紐づけられた状態で、mainメソッドのitem_master=[]に格納されているので、
item_master.item_codeで番号を、item_master.item_nameで商品名を呼び出せる。

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝



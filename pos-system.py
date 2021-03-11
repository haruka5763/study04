import csv
import pandas as pd

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price



### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        return (item_code)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
    
    # オーダーの詳細情報取得 Task1
    def order_detail(self, order_code):
        for order in self.item_master:
            if order_code == order.item_code:
                print("商品名：{}".format(order.item_name))
                print("価格：{}".format(order.price))
    
# csvからマスタ情報取得　Task3
def item_master_csv(csv):
    item_master = []
    try:
        df = pd.read_csv(csv, encoding="utf-8_sig")
        print("\n=====マスタ情報一覧=====\n")
        print(df)

        for item_code,item_name,price in zip(list(df["item_code"]), list(df["item_name"]), list(df["price"])):
            item_master.append((Item(item_code,item_name,price))    
        
    except Exception as e:
        print("csvが読み込めませんでした")
        print(e)
        sys.exit()



### メイン処理
def main():
    # マスタ登録
    item_master=item_master_csv("./item_master.csv")

    # オーダー登録 Task2
    order=Order(item_master)
    o =  list(input("オーダー番号を入力して下さい（例　1 2 5）：").split())
    for i in o:
        order.add_item_order(i)

    # オーダー表示 Task1
    print("オーダーが入りました")
    print("************************")

    for i in order.item_order_list:
        print("オーダー番号：{}".format(i))
        order.order_detail(i) 
        print("************************")

    
if __name__ == "__main__":
    main()
    
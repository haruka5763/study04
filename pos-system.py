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

# csvからマスタ情報取得　Task3
def item_master_csv(csv):

    try:
        csv_input = pd.read_csv(csv, encoding="utf-8_sig")
        df = pd.DataFrame(csv_input)
        loopcount =len(df['item_code'])
        for i in range(loopcount):
            item_master = []
            for item_code,item_name,price in zip(
                list(df['item_code']), list(df['item_name']), list(df['price'])
                ):
                item_master.append((item_code,item_name,price))
        return item_master

    except Exception as e:
        print("csvが読み込めませんでした")
        print(e)
        sys.exit()



### オーダークラス
class Order:
    def __init__(self,item_master):
        # 注文内容
        self.item_order_list=[]
        self.item_count_list=[]

        # メニュー一覧
        self.item_master=item_master




    def add_item_order(self, item_code, item_count):
        self.item_order_list.append(item_code)
        self.item_count_list.append(item_count)

    def receive_order(self):
        while True:
            carryon = input("注文しますか？[yse:1 no:0] : ")
            if int(carryon) == 1:
                ord =  input("オーダー番号を入力して下さい：")
                print("受け付けた注文番号は{}です".format(ord))
                count = input("個数を入力してください : ")
                self.add_item_order(ord, count)
            else:
                print("ご注文ありがとうございました!")
            break

    # オーダーの詳細情報取得 Task1
    def order_detail(self):
        print("オーダーが入りました")
        print("************************")
        print(self.item_master)
        itemclass = Item
        for order_code in self.item_order_list:
            for item_code,item_name,price in zip(
            list(itemclass.item_code), list(itemclass.item_name), list(itemclass.price)
            ):
                if order_code == item_code[0]:
                    print("商品名：{}".format(item_name[0]))
                    print("価格：{}".format(price[0]))
                elif order_code == item_code[1]:
                    print("商品名：{}".format(item_name[1]))
                    print("価格：{}".format(price[1]))                    
                elif order_code == item_code[2]:
                    print("商品名：{}".format(item_name[2]))
                    print("価格：{}".format(price[2]))   
                else:
                    print("リストにありません")


### メイン処理
def main():
    # マスタ登録 Task3
    csv = "./item_master.csv"
    item_master=item_master_csv(csv)
    print(item_master)
    # Order classのインスタンス生成
    order = Order(item_master)
    item = Item()
    # order.view_item_list
    # オーダー登録 Task2
    order.receive_order()
    # オーダー表示 Task1
    order.order_detail()



    
if __name__ == "__main__":
    main()
    
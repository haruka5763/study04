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
    
    # オーダーの詳細情報取得
    def order_detail(self, order_code):
        for order in self.item_master:
            if order_code == order.item_code:
                print("商品名：{}".format(order.item_name))
                print("価格：{}".format(order.price))
    
    
### メイン処理
def main():
    # マスタ登録⇒Itemクラスを使用しているので
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    # オーダー登録⇒Orderクラスへ
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    
    # オーダー表示
    print("オーダーが下記の通り入りました")
    print("************************")

    for i in order.item_order_list:
        print("オーダー番号：{}".format(i))
        order.order_detail(i) 
        print("************************")

    
if __name__ == "__main__":
    main()
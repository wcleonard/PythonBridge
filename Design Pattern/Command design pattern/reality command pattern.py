# @Time    : 2019/4/21 22:13
# @Author  : Noah
# @File    : reality command pattern.py
# @Software: PyCharm
# @description: 以证券交易所的例子来演示命令模式的实现

from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")


class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)

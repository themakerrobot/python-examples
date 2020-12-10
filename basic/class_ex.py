class Fruit:
  def __init__(self, name, count=0):
    self.name = name
    self.count = count
    print("{} {}개 초기화".format(self.name, self.count))
  
  def buy(self, count):
    print("{} {}개 구입".format(self.name, count))
    self.count += count
    return self.count

  def eat(self, count):
    print("{} {}개 먹음".format(self.name, count))
    self.count -= count
    return self.count

  def getCount(self):
    return self.count

if __name__ == "__main__":
  apple = Fruit("사과")
  banana = Fruit("바나나", 100)

  apple.buy(50)
  apple.eat(30)
  print("사과 수량:{}".format(apple.getCount()))

  banana.buy(50)
  banana.eat(20)
  print("바나나 수량:{}".format(banana.getCount()))

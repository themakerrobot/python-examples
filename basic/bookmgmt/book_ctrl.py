import csv
import os

class Book_Info:
  def __init__(self, item):
    self.name = item[0]
    self.price = item[1]

  def __str__(self):
    return "Name: {} / Price: {}".format(self.name, self.price)    

  def set(self, item):
    self.name = item[0]
    self.price = item[1]
  
  def get(self):
    return [self.name, self.price]


class Book_Mgmt:
  def __init__(self, filename="test.csv"):
    self.filename = filename
    self.items = []

    if os.path.isfile(self.filename):
      with open(self.filename, 'r', encoding='utf-8') as f:
        for item in csv.reader(f):
          self.items.append(Book_Info(item)) 
    else:
      with open(self.filename, 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerows([item.get() for item in self.items])
 
  def save(self):
    with open(self.filename, 'w', newline='') as f:
      wr = csv.writer(f)
      wr.writerows([item.get() for item in self.items])

  def load(self, filename):
    self.filename = filename
    self.items = []

    if os.path.isfile(self.filename):
      with open(self.filename, 'r', encoding='utf-8') as f:
        for item in csv.reader(f):
          self.items.append(Book_Info(item)) 
    else:
      with open(self.filename, 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerows([item.get() for item in self.items])

  def add(self, name, price):
    for item in self.items:
      if item.get()[0] == name:
        item.set([name, price])
        self.save()
        return

    self.items.append(Book_Info([name, price]))
    self.save()

  def delete(self, name):
    for item in self.items:
      if item.get()[0] == name:
        self.items.remove(item)
    self.save()

  def delete_all(self):
    self.items = []
    self.save()

  def search(self, name):
    result = ""
    for item in self.items:
      if item.get()[0] == name:
        result += str(item) + "\n"
    return result

  def display(self):
    result = ""
    for item in self.items:
      result += str(item) + "\n"
    return result

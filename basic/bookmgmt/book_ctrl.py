import csv
import os

class Book_Mgmt:
  def __init__(self, filename="test.csv"):
    self.filename = filename
    self.items = []

    if os.path.isfile(self.filename):
      with open(self.filename, 'r', encoding='utf-8') as f:
        for item in csv.reader(f):
          self.items.append(item) 
    else:
      with open(self.filename, 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(self.items)
 
  def save(self):
    with open(self.filename, 'w', newline='') as f:
      wr = csv.writer(f)
      wr.writerows(self.items)

  def load(self, filename):
    self.filename = filename
    self.items = []

    if os.path.isfile(self.filename):
      with open(self.filename, 'r', encoding='utf-8') as f:
        for item in csv.reader(f):
          self.items.append(item) 
    else:
      with open(self.filename, 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(self.items)

  def add(self, name, price):
    self.items.append([name, price])

  def delete(self, name):
    for item in self.items:
      if item[0] == name:
        self.items.remove(item)

  def delete_all(self):
    self.items = []

  def search(self, _info):
    for item in self.items:
      if item[0] == name:
        print(item)

  def display(self):
    for item in self.items:
      print(item)


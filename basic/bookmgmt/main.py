import csv
from book_ctrl import Book_Mgmt

if __name__ == "__main__":
  BM = Book_Mgmt()

  print("Book Management")

  while True:
    _type = input("(load|save|add|delete|search|display) > ")
    
    if _type == "load":
      _file = input("filename > ")
      BM.load(_file)

    elif _type == "save":
      BM.save()
    
    elif _type == "add":
      _name = input("name > ")
      _price = input("price > ")
      _confirm = input("y or n > ")
     
      if _confirm.upper() == 'Y':
        BM.add(_name, _price)
 
    elif _type == "delete":
      _name = input("name > ")
      _confirm = input("y or n > ")

      if _confirm.upper() == 'Y':
        BM.delete(_name)
 
    elif _type == "delete_all":
      _confirm = input("y or n > ")

      if _confirm.upper() == 'Y':
        BM.delete_all()

    elif _type == "search":
      _name = input("name > ")
      _confirm = input("y or n > ")

      if _confirm.upper() == 'Y':
        BM.search(_name)

    elif _type == "display":
      BM.display()
 
    elif _type == "quit":
      print("Goodbye")
      break

    else:
      print('no such command')


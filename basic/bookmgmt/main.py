import csv
from book_ctrl import Book_Mgmt

if __name__ == "__main__":
  BM = Book_Mgmt()

  print("## Book Management\n")

  while True:
    sel = input("(load|add|delete|delete_all|search|display|quit) > ")
    
    if sel == "load":
      filename = input("filename > ")
      BM.load(filename)
    
    elif sel == "add":
      name = input("name > ")
      price = input("price > ")
      confirm = input(" y or n > ")
     
      if confirm.upper() == 'Y':
        BM.add(name, price)
 
    elif sel == "delete":
      name = input("name > ")
      confirm = input(" y or n > ")

      if confirm.upper() == 'Y':
        BM.delete(name)
 
    elif sel == "delete_all":
      confirm = input(" y or n > ")

      if confirm.upper() == 'Y':
        BM.delete_all()

    elif sel == "search":
      name = input("name > ")
      confirm = input(" y or n > ")

      if confirm.upper() == 'Y':
        print(BM.search(name))

    elif sel == "display":
      print(BM.display())
 
    elif sel == "quit":
      print("Goodbye")
      break

    else:
      print('no such command')

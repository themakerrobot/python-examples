print('## Python Summary')

""" CH1 변수, 문자열, 사용자 입력(variables, strings, User input)  """
#''' CH1 - START
print('\n\nChapter 1')

print('Hello Python')

msg = 'Hello Python'
print(msg)

msg1 = 'PI'
msg2 = 'is'
msg3 = 3.14
msgs = msg1 + ' ' + msg2 + ' ' + str(msg3)
print(msgs)

lists = ['aaa', 'bbb', 'ccc']
print(lists)

data = input('Input String, Numerical value ... > ')
print(data, type(data))

# CH1 - END'''

""" CH2 리스트 (lists) """
#''' CH2 - START
print('\n\nChapter 2')

items = ['aaa', 'bbb', 'ccc']

item_first = items[0]
item_last = items[-1]
print(item_first, item_last)

for item in items:
  print(item)

colors = []
colors.append('red')
colors.append('green')
colors.append('blue')
print(colors)

numbers = []
for x in range(1, 11):
  numbers.append(x**2)
print(numbers)

numbers = [x**2 for x in range(1, 11)]
print(numbers)

items = ['one', 'two', 'three', 'four']
one_two = items[:2]
print(one_two)

copied_items = items[:]
print(copied_items)

tuple_items = (100, 200)
#tuple_items = (1, 2) # O --> Overwrite an entire tuple
#tuple_items[0] = 200 # X --> Can't change the individual item in a tuple
print(tuple_items)

# CH2 - END'''

""" CH3 딕셔너리 (dictionaries) """
#''' CH3 - START
print('\n\nChapter 3')

tom = {'age': 15, 'gender':'man'}
print(tom['age'], tom['gender'])

tom['glasses'] = "none"
print(tom)

for key, item in tom.items():
  print(key, item)

for key in tom.keys():
  print(key)

for value in tom.values():
  print(value)

# CH3 - END'''

""" CH4 if 조건문과 while 반복문 (if statements and while loops) """
#''' CH4 - START
print('\n\nChapter 4')

x = 10
print('10 == 10 : ', x == 10)
print('10 != 10 : ', x != 10)
print('10 >   5 : ', x  >  5)
print('10 >= 10 : ', x >= 10)
print('10 <   5 : ', x  <  5)
print('10 <= 10 : ', x <= 10)

basket = ['apple', 'banana', 'grape']
print('apple' in basket)
print('melon' in basket)

# CH4 - END'''

""" CH5 함수 (Functions) """
#''' CH5 - START
print('\n\nChapter 5')
# CH5 - END'''

""" CH6 클래스 (Classes) """
#''' CH6 - START
print('\n\nChapter 6')
# CH6 - END'''

""" CH7 파일과 예외처리 (files and exceptions) """
#''' CH7 - START
print('\n\nChapter 7')
# CH7 - END'''


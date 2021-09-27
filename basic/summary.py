print('## Python Summary')

""" CH1 변수, 문자열, 사용자 입력(variables, strings, User input)  """
#''' CH1 - START
print('\n\nChapter 1')

print('[1] Hello Python')

message = '[2] Hello Python'
print(message)

number = '[3]'
message = 'Hello Python'
total_message = number + ' ' + message
print(total_message)

lists = ['aaa', 'bbb', 'ccc']
print('[4] lists: ' + str(lists))

print('[5] User input')
name = input('What is your name? > ')
print('Hi ' + name)

print('[6] User input(numerical input)')
age = input ('How old are you? > ')
print(' ' + age + ', type: ' + str(type(age)))

# CH1 - END'''

""" CH2 리스트 (lists) """
#''' CH2 - START
print('\n\nChapter 2')

devices = ['airplane', 'car', 'robot']

first_device = devices[0]
last_device = devices[-1]
print('[1] first_device: ' + first_device + ' last_device: ' + last_device)

print('[2] display devices')
for dev in devices:
  print(' ' + dev)

colors = []
colors.append('red')
colors.append('green')
colors.append('blue')
print('[3] colors: ' + str(colors))

numbers = []
for x in range(1, 11):
  numbers.append(x**2)
print('[4] numbers: ' + str(numbers))

numbers = [x**2 for x in range(1, 11)]
print('[5] numbers: ' + str(numbers))

items = ['one', 'two', 'three', 'four']
one_two = items[:2]
print('[6] one_two : ' + str(one_two))

copied_items = items[:]
print('[7] copied_items: ' + str(copied_items))

tuple_items = (100, 200)
#tuple_items = (1, 2) # O --> Overwrite an entire tuple
#tuple_items[0] = 200 # X --> Can't change the individual item in a tuple
print('[8] tuple_items: ' + str(tuple_items))

# CH2 - END'''

""" CH3 딕셔너리 (dictionaries) """
#''' CH3 - START
print('\n\nChapter 3')

tom = {'age': 15, 'gender':'man'}
print('[1] Tom\'s age is ' + str(tom['age'])  + ', gender is ' + tom['gender'])

tom['glasses'] = "none"
print('[2] Tom\'s glasses is ' + tom['glasses'])

print('[3] display key and value')
for key, item in tom.items():
  print(' ' + key + ', ' + str(item))

print('[4] display key')
for key in tom.keys():
  print(' ' + key)

print('[5] display values')
for value in tom.values():
  print(' ' + str(value))

# CH3 - END'''


""" CH4 if 조건문과 while 반복문 (if statements and while loops) """
#''' CH4 - START
print('\n\nChapter 4')

print('[1] Conditional Test')
x = 10
print(' == : ' + x == 10)
print(' != : ' + x != 10)
print(' >  : ' + x >  5)
print(' >= : ' + x >= 10)
print(' <  : ' + x < 5)
print(' <= : ' + x <= 10)

print('[2] Conditional Test with lists')
basket = ['apple', 'banana', 'grape']
print(' Q: Is there an apple in lists ? A: ' + 'apple' in basket)
print(' Q: Is there an melon in lists ? A: ' + 'melon' in basket)

print('[3] boolean values')
enable = True



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


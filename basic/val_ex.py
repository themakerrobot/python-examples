'''
1. 변수 이름
  + 가능
    - a-z, A-Z, 0-9, _
  + 불가능
    - 숫자로 시작
    - 예약어
      + False class finally is return None continue for lamda try
      + True def from nonlocal while and del global not with in raise
      + as elif if or yield assert else import pass break except
'''
a = 10
b = "Hello"
print(a, b)
print("{} ===== {}".format(a, b))


'''
2. 연산
  + 더하기,빼기,곱하기,나누기,몫구하기 
  + 우선순위 () 이용
  + 
'''
a = 10
b = 3
print("{} +  {} = {}".format(a,b, a+b))
print("{} -  {} = {}".format(a,b, a-b))
print("{} *  {} = {}".format(a,b, a*b))
print("{} /  {} = {}".format(a,b, a/b))
print("{} // {} = {}".format(a,b, a//b))

a=10
print("(1)[a=1] a={}".format(a))
a+=1
print("(2)[a+=1] a={}".format(a))
a-=1
print("(3)[a-=1] a={}".format(a))
a*=3
print("(4)[a*=3] a={}".format(a))
a/=3
print("(5)[a/=3] a={}".format(a))
a//=3
print("(6)[a//=3] a={}".format(a))


'''
3. 진수
  + bin(10진수) =  2진수 문자열
  + oct(10진수) =  8진수 문자열
  + hex(10진수) = 16진수 문자열
'''
a = 10
print("{}의 2진수:{}({}), 8진수:{}({}), 16진수:{}({}) 입니다.".format(a,\
     bin(a), type(bin(a)),\
     oct(a), type(oct(a)),\
     hex(a), type(hex(a))\
))

print("숫자형으로 변환")
print(int(bin(a), 2))
print(int(oct(a), 8))
print(int(hex(a), 16))


'''
4. 형변환
'''
print("int(True)={}, int(False)={}".format(int(True), int(False)))
print("int('100')={}, int('-15') ={}, int(50.5)={}".format(int('100'), int('-15'), int(50.5)))

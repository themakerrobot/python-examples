# Quiz
+ 책 관리 프로그램 만들기

+ 초기화
  - book.csv 파일을 자동으로 불러오고 없으면 생성합니다.

+ 클래스 명세
  - Book_Info
    + 멤버변수
      - name: 책 이름
      - price: 책 가격
    + 멤버함수
      - set: name과 price를 입력합니다.
      - get: name과 price를 반환합니다.
  - Book_Mgmt
    + 멤버변수
      - filename: 책 정보를 저장하는 csv 파일
      - items: 책 정보를 저장하는 변수
    + 멤버함수
      - save(): csv 파일로 저장합니다.
      - load(): csv 파일을 불러옵니다.
      - add(name, price): 책을 추가합니다.
      - delete(name): 책을 삭제합니다.
      - delete_all(): 책 전체를 삭제합니다.
      - search(name): 저장된 책 중, 특정 책을 반환합니다.
      - display(): 저장된 책을 모두 반환합니다.

+ 데이터 구조
  -  파일 형태: csv
  -  파일 내용: 
     ```
     책1 이름, 책1 가격
     책2 이름, 책2 가격
     책3 이름, 책3 가격
     책4 이름, 책4 가격
     ```
+ 명령어 리스트
  - load
    + 기능: 지정한 파일을 불러오고 없으면 생성합니다.
    + 매개변수: 사용할 파일 이름
  - save
    + 기능: load로 등록한 파일에 현재 값을 저장
  - add
    + 기능: 책을 추가합니다. / 동일한 이름이 있다면, 교체합니다.
    + 매개변수: 추가할 책 이름, 책의 가격
  - delete
    + 기능: 책 1권을 삭제합니다.
    + 매개변수: 삭제할 책 이름
  - delete_all
    + 기능: 모든 자료는 삭제합니다.
  - search
    + 기능: 지정한 책을 조회합니다.
    + 매개변수: 조회할 책 이름
  - display
    + 기능: 저장된 모든 책을 조회합니다.
  - quit
    + 기능: 프로그램을 종료합니다.

+ 실행결과
```
## 프로그램 실행

pi@raspberrypi:~/hw $ python3 main.py
## Book Management

(load|add|delete|delete_all|search|display|quit) > display

# BOOK1 추가
(load|add|delete|delete_all|search|display|quit) > add
name > BOOK1
price > 9900
 y or n > y

# BOOK2 추가
(load|add|delete|delete_all|search|display|quit) > add
name > BOOK2
price > 7500
 y or n > y

# BOOK3 추가
(load|add|delete|delete_all|search|display|quit) > add
name > BOOK3
price > 12000
 y or n > y

# 전체 조회
(load|add|delete|delete_all|search|display|quit) > display
Name: BOOK1 / Price: 9900
Name: BOOK2 / Price: 7500
Name: BOOK3 / Price: 12000

# BOOK2 조회
(load|add|delete|delete_all|search|display|quit) > search
name > BOOK2
 y or n > y 
Name: BOOK2 / Price: 7500

# BOOK2 삭제
(load|add|delete|delete_all|search|display|quit) > delete      
name > BOOK2
 y or n > y
 
# 전체 조회 (BOOK2는 삭제)
(load|add|delete|delete_all|search|display|quit) > display
Name: BOOK1 / Price: 9900
Name: BOOK3 / Price: 12000

# 프로그램 종료
(load|add|delete|delete_all|search|display|quit) > quit
Goodbye

# csv 파일 확인
pi@raspberrypi:~/hw $ cat book.csv 
BOOK1,9900
BOOK3,12000

# 프로그램 재실행
pi@raspberrypi:~/hw $ python3 main.py 
## Book Management

# 정상적으로 book.csv를 불러오는지 확인
(load|add|delete|delete_all|search|display|quit) > display
Name: BOOK1 / Price: 9900
Name: BOOK3 / Price: 12000

# 전체 삭제
(load|add|delete|delete_all|search|display|quit) > delete_all
 y or n > y

# 전체 조회
(load|add|delete|delete_all|search|display|quit) > display

# 프로그램 종료
(load|add|delete|delete_all|search|display|quit) > quit
Goodbye
```

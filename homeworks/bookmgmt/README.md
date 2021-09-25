# Book Management

+ 초기화
  - test.csv 파일을 자동으로 불러오고 없으면 생성합니다.

+ 클래스
  - Book_Info
    + 멤버변수
      - name: 책 이름
      - price: 책 가격
    + 멤버함수
      - set: name과 price를 입력
      - get: name과 price를 반환
  - Book_Mgmt
    + 멤버변수
      - filename: 책 정보를 저장하는 csv 파일
      - items: 책 정보를 저장하는 변수
    + 멤버함수
      - save: csv 파일로 저장
      - load: csv 파일 불러오기
      - add: 책 추가
      - delete: 책 삭제
      - delete_all: 책 전체 삭제
      - search: 책 찾기
      - display: 책 전체 보기

+ Command List
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

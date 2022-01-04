# 개요
  대용량 csv파일의 데이터를 Dataframe으로 바꾸어서 원하는 날짜의 데이터만 출력하는 프로그램이다.

## Git 다운로드
  ```:~ $git clone https://github.com/yugwangsik/python_csv_project.git```


## 실행 전 준비 및 경로 변경
  - csv폴더에서 테스트용 csv파일을 다운로드한다.
  - csv_to_dataframe.py 파일을 다운로드한다.
  - csv_to_dataframe.py 48번 줄에 로컬 경로를 자신의 환경에 맞추어서 변경한다.
    <img src="/img/line.PNG" width="50%" height="50%"></img>
    
  - 로컬 경로 하위에 테스트용 csv파일을 이동시킨다.<br>
    <img src="/img/path.PNG" width="600px" height="200px"></img>

## 실행
  ```:~ $python3 csv_to_dataframe.py```
  
## 날짜 입력
  - csv_to_dataframe.py를 실행 시킨 뒤 시작날짜 종료날짜를 입력한다.
  - 날짜를 입력할 때 형식은 yyyy-mm-dd hh:mm:ss 형식으로 입력한다.<br>
    <img src="/img/test.PNG" width="400px" height="50px"></img>

## 데이터 read 및 변환
  - csv_to_dataframe.py를 실행 시키면 자신의 폴더 및 하위에 있는 csv파일의  경로를 리스트 형태로 저장한다.
  - 저장된 리스트에서 csv파일을 하나씩 dataframe 형태로 읽어와서 리스트에 저장한다.
  - dataframe형태로 저장된 리스트를 dataframe으로 다시 합친다.

## Result
  - 입력한 날짜 범위에 맞는 데이터를 확인 한다.<br>
    <img src="/img/test_result.PNG" width="400px" height="1000px"></img>

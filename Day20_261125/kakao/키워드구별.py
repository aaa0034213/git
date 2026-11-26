# 키워드 구별.py

# 1. primary key
# - 기본 고유값, NULL값 허용 x , 자동으로 index가 잡힘. 

# 2. UNIQUE
# - 중복값 없게하고 NULL 값 허용

# 3. 스트림릿 버튼 안에 key 옵션
# key 설정을 하지 않으면 버튼을 누를때마다 새로고침되서 key 설정을 해야한다.
# session 에 자동으로 값을 찾아가 연동을 한다.
# st.rerun 시 최신 입력값을 읽게 할 수 있다.

# 4. primary key , unique 차이
# - primary key 는 값이 비어있으면 안됨 중복값 허용 (테이블 당 한 개), 
#   UNIQUE NULL 허용 중복값은 안됨 (테이블 당 여러 개 사용 가능)

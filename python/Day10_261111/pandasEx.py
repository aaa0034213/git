# pandasEx.py

import pandas as pd

# 판다스 버전확인, 버전 달라도 상관없음
print(pd.__version__)

#----------------------------------------------------
# 데이터가 비정상적으로 들어올때
# None 데이터 없음
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
#
data = [80,90,80,None,50,600, -10, "ㅓ"]

# 데이터를 하나씩 꺼내서 None 제외시키는 코드
for 데이터 in data:
    if 데이터 == None or 데이터 >100:
        data.remove(None)

print(data)
#합계 = sum(data)
#print(합계 / len(data))

#--------------------------------------------------
data2 = ["12,000", "8,000", "8,000", "5,000"]

#sum() 모든 숫자든 문자든 더하는 기능
# 파이썬에서는 문자 + 문자 = 연결
print(sum(data2))

#------------------------------------------------
# 데이터를 정리하고 쉽게 분석하기 위해서 판다스를 쓴다
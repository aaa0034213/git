#literacy.py

#1.스트림릿 도구 포함하기!
#   파이썬으로 웹 사이트 만들기!
import streamlit as st

#2. 실행 python -m streamlit run literacy.py
st.title("AI 리터러시")
st.header("나의 AI 리터러시 노트")

st.write("리터러시는 글을 읽고 쓰는 능력, 문해력")
st.write("글의시대 문해력 - 글을 읽고 쓰고 뜻을 이해")
st.write("인터넷시대 - 디지털 리터러시 - 검색하고,가짜뉴스 가려내기")
st.write("AI시대 - AI리터리시")
st.write("AI를 이해하고,잘시키고,결과를 평가하고,책임있게쓰기")

st.subheader("1.알기")
st.write("AI를 알고, 무엇을 맡길지 정한다.")

st.subheader("토큰?")
st.write("AI가 글을 처리하는 최소 단위")
st.write("대량의 글과 문장 수집")
st.write("토크나이저가 문장을 작은 토큰으로 분리하고 숫자로 변환")
st.write("반복적으로 글과 문장을 읽어서 자주 나오는 단어 사전")
st.write("다음 토큰 예측하고 오차를 줄이며 패턴 학습 - 딥러닝")
st.write("학습한 패턴이 숫자형태로 반영됨 - 학습된 가중치")

# '딸기우유바나나우유초코우유'에서 '우' 글자는 몇 번 나와?
# 파이썬 글자 수를 세는 기능 count()
# 파이썬에서 문자를 이용해서 자르고,복사, 변경하고 , 대소문자
# 바꾸고 이런 기능들 사용할 수 있다.
print('딸기우유바나나우유초코우유'.count('우'))
# replace(전,후)
# - 뉴스기사,대량 문서들, 게시물들 ,공공데이터
# 특수문자나 공백들을 제거하는데 사용을 많이한다.
print('딸기우유바나나우유초코우유'.replace("우유",","))

st.subheader("컨텍스트 윈도우? - context window")
st.write("AI 한번에 참고할 수있는 정보의 최대 범위")
st.write("토큰: 글을 나눈 조각")
st.write("컨텍스트: 문맥,앞뒤 상황과 관련된 정보")
st.write("윈도우: 한번에 참고 할 수있는 범위")

st.subheader("2.시키기")
st.write("원하는 것을 분명하게 설명한다")
st.subheader("프롬프트 - prompt")
st.write("AI에게 질문,명령,요청 또는 참고 정보준다!")
st.write("AI에게 일을 시키기 위해서 하는 말!")

st.subheader("프롬프트 엔지니어링")
st.write("AI가 원하는 결과를 만들도록 질문과 지시를 설계하고")
st.write("결과를 확인하면서 개선하는 과정")

st.subheader("프롬프트 핵심 4가지")
st.write("1. 무엇을 해 달라고 하나? - 지시사항 ,목적(Goal)")
st.write("2. 나는 누구고 어떤 상황인가? - 맥락 (context)")
st.write("3. 어떤 조건을 지켜야하나? - 제약조건(Constraints)")
st.write("4. 어떤 모양으로 받고 싶나? - 출력형식(format)")

st.subheader("제로샷 Zero-shot")
st.write("예시없이 그냥 질문하기")
st.write("AI는 내가 좋아하는걸 모른다")

st.subheader("원샷 One-shot")
st.write("예시를 한 개만 메뉴의 예시를 보여준다.")

st.subheader("퓨샷 Few-shot")
st.write("예시를 여러 개 내가 좋아하는 메뉴의 공통점을 알려주기")

st.subheader("3.확인하기")
st.write("결과를 따져 보고 검증한다.")
st.subheader("사실확인 - 정말 사실인가? fact-checking")
st.subheader("출처확인 - 어디서 나온 정보인가? source - verification")
st.subheader("결과검증 - 숫자, 조건, 형식이 맞는가? validation")



st.subheader("4.책임지기")
st.write("책임지고, 투명하게 쓴다.")
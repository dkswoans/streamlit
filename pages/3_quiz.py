import streamlit as st


st.write("공기에서 가장 큰 비율을 차지하는 기체는 무엇인가요?")
title = st.text_input("", "")
correct = "질소"

st.write("공기에서 가장 큰 비율을 차지하는 기체는 무엇인가요?")
options = [
    "1. 질소",
    "2. 산소",
    "3. 아르곤",
    "4. 이산화 탄소",
    "5. 일산화 탄소"
]
result=0
correct_answer = "1. 질소"

# 사용자 입력 받기
user_answer = st.radio("답을 선택하세요:", options)

# 제출 버튼 생성 및 결과 처리
if st.button('제출'):
    if user_answer != correct_answer:
        st.error("오답입니다!")
        
    elif title!=correct:
        st.error("오답입니다!")
    else:
        st.success("정답입니다")
        result+=1

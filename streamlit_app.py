import streamlit as st
import pandas as pd
import datetime as dt

st.subheader("오류중학교 정보화 기기 수리 요청 대장")
st.dataframe(pd.DataFrame([['gg','hh'],['zz','fv']], columns=['접수 일시', '수리 요청자']))

if st.checkbox('show/hide'):
  st.text('뭔가 하겠다.')
  st.text(dt.datetime.now())

lang = ['python', 'Java']
select_lang = st.selectbox('언어를 선택하세요.', lang)
st.write('당신이 선택한 언어는 {}입니다.',format(select_lang))

input = st.text_input("message")
st.write(input)

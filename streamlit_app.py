import streamlit as st
import pandas as pd
import datetime as dt

st.subheader("오류중학교 정보화 기기 수리 요청 대장")


colms = st.columns((1, 1, 1, 1, 2, 1,2))
fields = ['만든 날짜', '수리 요청인', '수리 대상물 위치(부서/교실)', '수리 점검 물품(ex.컴퓨터, 노트북)', '고장 상태', '처리 상태', '비고']
for col, field_name in zip(colms, fields):
  col.write(field_name)

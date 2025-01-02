import streamlit as st
import pandas as pd

st.subheader("오류중학교 정보화 기기 수리 요청 대장")
st.dataframe(pd.DataFrame([['gg','hh'],['zz','fv']], columns=['접수 일시', '수리 요청자']))

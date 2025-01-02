import streamlit as st
import pandas as pd
import datetime as dt
from st_aggrid import AgGrid, GridOptionsBuilder

st.markdown("<span style='font-size: 23px;'>오류중학교 정보화 기기 수리 요청 대장</span>", unsafe_allow_html=True)

data = pd.DataFrame([{'make_date': '11', 'people': '김도윤'}])

gb = GridOptionsBuilder()
gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
)
gb.configure_column(field="make_date", header_name="요청 날짜", editable=True, width=80)
gb.configure_column(field="people", header_name="수리 요청인", editable=False, width=80)
go = gb.build()

AgGrid(data, gridOptions=go)

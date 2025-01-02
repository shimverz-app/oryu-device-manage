import streamlit as st
import pandas as pd
import datetime as dt
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode

st.markdown("<span style='font-size: 23px;'>오류중학교 정보화 기기 수리 요청 대장</span>", unsafe_allow_html=True)

data = pd.DataFrame([{'make_date': '11',
                      'people': '김도윤',
                      'place': '교육정보부',
                      'device': '컴퓨터',
                      'happen': '컴퓨터 안켜짐',
                      'tf': True,
                      'noop': ''
                     }])

gb = GridOptionsBuilder()
gb.configure_default_column(
    resizable=False
)
gb.configure_column(field="make_date", header_name="요청 날짜", editable=True, width=90)
gb.configure_column(field="people", header_name="수리 요청인", width=80)
gb.configure_column(field="place", header_name="수리 대상물 위치(부서/교실)", width=80)
gb.configure_column(field="device", header_name="수리 점검 물품(ex.컴퓨터, 노트북)", width=80)
gb.configure_column(field="happen", header_name="고장 상태", width=80)
gb.configure_column(field="tf", header_name="처리 상태", width=80, editable=True)
gb.configure_column(field="noop", header_name="비고", width=80, editable=True)
go = gb.build()

AgGrid(data,
       gridOptions=go,
       columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW)

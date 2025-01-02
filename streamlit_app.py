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
  filterable=False,
  sortable=False,
  groupable=False,
  resizable=True,
  autoSizeColumns=True
)

gb.configure_column(field="make_date", header_name="요청 날짜",  suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="people", header_name="수리 요청인", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="place", header_name="수리 대상물 위치(부서/교실)", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="device", header_name="수리 점검 물품(ex.컴퓨터, 노트북)", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="happen", header_name="고장 상태", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="tf", header_name="처리 상태", editable=True, suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="noop", header_name="비고", editable=True, suppressMenu=True, sortable=False, filter=False)
go = gb.build()
go['suppressMovableColumns'] = True

response = AgGrid(
  data,
  gridOptions=go,
  fit_columns_on_grid_load=False
)

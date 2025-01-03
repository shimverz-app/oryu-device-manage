import streamlit as st
import pandas as pd
import datetime as dt
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
import requests
import json

st.set_page_config(
    page_title="오류중학교 정보화 기기 수리 요청 대장",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

r = requests.post('https://login.microsoftonline.com/4e732c26-acb5-4964-b7fe-cba67063c366/oauth2/v2.0/token', data={
    'grant_type': 'password',
    'scope': 'https://graph.microsoft.com/AllSites.Write',
    'client_id': st.secrets.client_id,
    'username': st.secrets.username,
    'password': st.secrets.password,
    'client_secret': st.secrets.client_secret
})
st.write(r.json())
access_token = r.json()['access_token']

headers = {
    "Authorization": f"Bearer {access_token}"
}

r = requests.get('https://graph.microsoft.com/v1.0/groups/e49eee20-ef81-4f29-93aa-951daa958fca/lists', headers=headers)

st.write(r.text)

st.markdown(
    """
    <style>
    .stAppHeader, ._container_gzau3_1, ._profileContainer_gzau3_53 {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<span style='font-size: 23px;'>오류중학교 정보화 기기 수리 요청 대장</span>", unsafe_allow_html=True)

df = pd.DataFrame([{'make_date': '11',
                      'people': '김도윤',
                      'place': '교육정보부',
                      'device': '컴퓨터',
                      'happen': '컴퓨터 안켜짐',
                      'tf': True,
                      'noop': ''
                     }])

gb = GridOptionsBuilder().from_dataframe(df)
gb.configure_default_column(
  filterable=False,
  sortable=False,
  groupable=False,
  resizable=False,
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
  df,
  gridOptions=go,
  columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
)

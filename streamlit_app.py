import streamlit as st
import pandas as pd
import datetime as dt
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode, JsCode
import requests
import json

st.set_page_config(
    page_title="오류중학교 정보화 기기 수리 요청 대장",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

def token_generate():
    if 'access_token' not in st.session_state:
        st.session_state.createdTime = dt.datetime.now()
        st.session_state.expireTime = dt.timedelta(seconds=0)
        st.session_state.access_token = ''
    if st.session_state.createdTime + st.session_state.expireTime > dt.datetime.now() + dt.timedelta(seconds=10):
        # st.write(st.session_state.createdTime)
        # st.write(st.session_state.expireTime)
        # st.write(st.session_state.access_token)
        return
    else:
        r = requests.post('https://login.microsoftonline.com/4e732c26-acb5-4964-b7fe-cba67063c366/oauth2/v2.0/token', data={
            'grant_type': 'password', 'scope': 'https://graph.microsoft.com/AllSites.Write', 'client_id': st.secrets.client_id,
            'username': st.secrets.username, 'password': st.secrets.password, 'client_secret': st.secrets.client_secret })
        st.session_state.createdTime = dt.datetime.now()
        st.session_state.expireTime = dt.timedelta(seconds=r.json()['expires_in'])
        st.session_state.access_token = r.json()['access_token']
        # st.write(st.session_state.createdTime)
        # st.write(st.session_state.expireTime)
        # st.write(st.session_state.access_token)

token_generate()

headers = {"Authorization": f"Bearer {st.session_state.access_token}"}

r = requests.get('https://graph.microsoft.com/v1.0/groups/e49eee20-ef81-4f29-93aa-951daa958fca/sites/root/lists/7cbc9d8e-f383-46c8-a205-22ac00f3d842/items?' +
                 'expand=' +
                 'fields(select=Created,Title,_x314e__x314e_,_xc218__xb9ac__xc810__xac80__xbb,_xace0__xc7a5__xc0c1__xd0dc__x00,_xcc98__xb9ac__xc0c1__xd0dc_,_xbe44__xace0_)', headers=headers)

flattened_data = [
    {
        key: value for key, value in {
            "id": int(item["id"]),
            **item["fields"]
        }.items() if key != "@odata.etag"
    }
    for item in r.json()['value']
]

for _ in flattened_data:
    _['Created'] = (dt.datetime.strptime(_['Created'], '%Y-%m-%dT%H:%M:%SZ') + dt.timedelta(hours=9)).strftime('%m월 %d일')

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

df = pd.DataFrame(flattened_data).sort_values(by='id', ascending = False)

gb = GridOptionsBuilder().from_dataframe(df)
gb.configure_default_column(
  filterable=False,
  groupable=False,
    sortable=False,
  resizable=False,
  autoSizeColumns=True
)

gb.configure_grid_options(
    getRowStyle=JsCode("""
    function(params) {
        if (params.data._xcc98__xb9ac__xc0c1__xd0dc_ === false) {
            return { background: 'rgba(255, 0, 0, 0.1)' };
        }
    }
    """),

    onCellValueChanged=JsCode(f"""
    function(event) {{
        const updatedData = {{
            '_xcc98__xb9ac__xc0c1__xd0dc_': event.data._xcc98__xb9ac__xc0c1__xd0dc_,
            '_xbe44__xace0_': event.data._xbe44__xace0_
        }};

        // 서버로 요청 전송
        fetch('https://graph.microsoft.com/v1.0/groups/e49eee20-ef81-4f29-93aa-951daa958fca/sites/root/lists/7cbc9d8e-f383-46c8-a205-22ac00f3d842/items/'+event.data.id+'/fields', {{
            method: 'PATCH',
            headers: {{
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {st.session_state.access_token}'
            }},
            body: JSON.stringify(updatedData)
        }})
        .then(response => {{
            if (!response.ok) {{
                throw new Error('서버 오류');  // 에러 발생 시 처리
            }}
            return response.json();
        }})
        .then(data => {{
            console.log('업데이트 성공:', data);
        }})
        .catch(error => {{
            console.error('업데이트 실패:', error);
            // 변경 취소: 이전 상태로 복구
            const transaction = {{
                update: [event.oldData]  // 변경 전 데이터로 되돌리기
            }};
            event.api.applyTransaction(transaction);
        }});
    }}

    """)
)

gb.configure_column(field="id", header_name="id",  suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="Created", header_name="요청 날짜",  suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="Title", header_name="수리 요청인", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="_x314e__x314e_", header_name="수리 대상물 위치(부서/교실)", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="_xc218__xb9ac__xc810__xac80__xbb", header_name="수리 점검 물품(ex.컴퓨터, 노트북)", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="_xace0__xc7a5__xc0c1__xd0dc__x00", header_name="고장 상태", suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="_xcc98__xb9ac__xc0c1__xd0dc_", header_name="처리 상태", editable=True, suppressMenu=True, sortable=False, filter=False)
gb.configure_column(field="_xbe44__xace0_", header_name="비고", editable=True, suppressMenu=True, sortable=False, filter=False)
go = gb.build()

go['suppressMovableColumns'] = True

response = AgGrid(
  df,
  gridOptions=go,
  columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
    allow_unsafe_jscode=True
)

if st.query_params:
    updated_data = st.query_params
    st.write("서버에서 받은 업데이트 요청:", updated_data)

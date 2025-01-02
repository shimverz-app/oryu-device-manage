import streamlit as st
import pandas as pd
import datetime as dt

def change_label_style(label, font_size='12px', font_color='black', font_family='sans-serif'):
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
        elem.style.fontFamily = '{font_family}';
    </script>
    """
    st.components.v1.html(html)

st.markdown("<span style='font-size: 23px;'>오류중학교 정보화 기기 수리 요청 대장</span>", unsafe_allow_html=True)


colms = st.columns((0.5, 1, 1, 1, 1, 1, 1))
fields = ['만든 날짜', '수리 요청인', '수리 대상물 위치(부서/교실)', '수리 점검 물품(ex.컴퓨터, 노트북)', '고장 상태', '처리 상태', '비고']
for col, field_name in zip(colms, fields):
  col.write(field_name)
  change_label_style(fields, '5px')

import streamlit as st
from streamlit.components.v1 import html
st.markdown("<canvas style='width: 700px; height: 100px' id='myCanvas'>안녕하세여.</canvas><p>안녕하세요.</p> <script> const canvas = document.getElementById('myCanvas'); const ctx = canvas.getContext('2d'); ctx.fillText('오류중학교 정보화 기기 수리 요청 대장', 10, 10); </script>", unsafe_allow_html=True)

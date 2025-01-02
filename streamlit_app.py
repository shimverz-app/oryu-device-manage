import streamlit as st
from streamlit.components.v1 import html
st.html("<canvas style='width: 100%; height: 100px' id='myCanvas'>안녕하세여.</canvas><p>안녕하세요.</p>")

html("<script> const canvas = document.getElementById('myCanvas'); const ctx = canvas.getContext('2d'); ctx.fillText('오류중학교 정보화 기기 수리 요청 대장', 10, 10); </script>")

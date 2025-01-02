import streamlit as st

st.html("<canvas id='myCanvas' width='100%' height='100px'>안녕하세여.</canvas>")

st.html("<script> const canvas = document.getElementById('myCanvas'); const ctx = canvas.getContext('2d'); ctx.fillText('오류중학교 정보화 기기 수리 요청 대장', 10, 10); </script>")

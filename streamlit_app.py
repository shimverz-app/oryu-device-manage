import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

# 샘플 데이터
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
})

# GridOptionsBuilder 설정
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(sortable=True)
gb.configure_grid_options(sortModel=[{"colId": "score", "sort": "desc"}])
grid_options = gb.build()

# AgGrid 렌더링
AgGrid(df, gridOptions=grid_options, height=300, theme="streamlit")


import streamlit as st
import datetime
import pandas as pd
import numpy as np


termo_type = st.sidebar.selectbox('REGIUNEA', ('Centru', 'Buiucani', 'Ciocana', 'Riscani', 'Botanica'))
termo_count = st.sidebar.slider("Diapazon", 1, 10, 2)




st.write('"TABEL SINOPTIC"')
d = st.date_input("Calendar", datetime.date(2024, 8, 23))
chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)
st.write(termo_type)
if st.sidebar.button("Apasa butonul"):
    st.write("🔞🔞🔞🔞🔞💥☢💥☢💥☢💥☢💥☢")

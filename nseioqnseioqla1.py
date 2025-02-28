import datetime
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  st.header("Cadastre seu aluno:")

with col2:
  st.text_input("Nome:")
  st.date_input("Insira sua data de nascimento:")

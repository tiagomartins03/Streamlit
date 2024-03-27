import streamlit as st
import pandas as pd


def set_image(path):
    st.image(image=path, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



set_image("images\passosmagicos.png")


st.write("# Verificar próxima etapas para os alunos")
st.write("### Insira seu arquivo Excel Aqui")


uploaded_file = st.file_uploader("Choose a .xlsx file", type="xlsx")


if uploaded_file is not None:
    if uploaded_file.name.endswith('.xlsx'):
        fileDF = pd.read_excel(uploaded_file)
    else:
        st.write("Por favor, selecione um arquivo com extensão .xlsx.")
else:
    fileDF = pd.DataFrame()  


def showdataframe(fileDF):
    try:
        if fileDF.empty:
            st.write("Por favor, insira um arquivo Excel")
        else:
            st.write(fileDF)
    except NameError:
        st.write("DataFrame is not defined. Please upload a valid Excel file.")



showdataframe(fileDF)

st.button("Enviar")
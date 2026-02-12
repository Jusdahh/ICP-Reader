import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ICP-Reader",
    page_icon="📊",  # opcional
    layout="wide"    # opcional
)

st.title("Leitor de Dados do Módulo ICP")

arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if arquivo is not None:
    df = pd.read_csv(arquivo)

    st.success("Arquivo carregado com sucesso!")

    st.subheader("Pré-visualização")
    st.dataframe(df)

    st.subheader("Informações gerais")
    st.write(f"Linhas: {df.shape[0]}")
    st.write(f"Colunas: {df.shape[1]}")

    coluna = st.selectbox("Escolha a coluna para plotar", df.columns)

    st.subheader("Gráfico")
    st.line_chart(df[coluna])
    
    colunas = df.columns.tolist()
    col1, col2 = st.columns(2)

    with col1:
        eixo_x = st.selectbox("Eixo X", colunas)

    with col2:
        # Remove a coluna escolhida no X
        colunas_y = [c for c in colunas if c != eixo_x]
        eixo_y = st.selectbox("Eixo Y", colunas_y)

    st.line_chart(df.set_index(eixo_x)[eixo_y])
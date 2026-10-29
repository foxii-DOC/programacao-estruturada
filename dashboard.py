import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Dashboard de Análise de Dados")

df = pd.DataFrame({
    "setor": ["Bancos", "Energia", "Varejo", "Saúde"],
    "roe": [0.18, 0.12, 0.08, 0.14],
})

setores = st.multiselect(
    "Selecione os setores",
    df["setor"].unique(),
    default=list(df["setor"].unique()),
)
filtrado = df[df["setor"].isin(setores)]

st.dataframe(filtrado)

fig, ax = plt.subplots()
sns.barplot(data=filtrado, x="setor", y="roe", ax=ax)
st.pyplot(fig)
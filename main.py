import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Titulli i aplikacionit
st.title("Vizualizimi dhe shfaqja e te dhenave me Streanlit")

# Shembull: Te dhenat te thjeshta
data = {
    'Emri': ['Leon','Eron','Jona'],
    'Mosha': [15,19,17],
    'Qyteti': ['Prishtine','Prishtine','Prishtine'],
    'Shteti': ['Kosov','Kosov','Kosov']
}
df_simple = pd.DataFrame(data)

st.subheader("Tabela me te dhena te thjeshta")
st.dataframe(df_simple)

# Ngarko datasetin nga Seaborn
df = sns.load_dataset('iris')
st.subheader("Dataseti Iris")
st.write(df.head())

# Vizualim me Seaborn
st.subheader("Grafiku me Seaborn")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", ax=ax1)
st.pyplot(fig1)

# Vizualizim me Plotly
st.subheader("Grafiku me Plotly")
fig2 = px.scatter(df, x="sepal_length", y="sepal_width", color="species", title="Scatterplot i Iris")
st.plotly_chart(fig2)

# Grafik Bar me Plotly
st.subheader("Grafik Bar: Gjatësia mesatare e sepalëve")
avg_sepal = df.groupby("species")["sepal_length"].mean().reset_index()
fig3 = px.bar(avg_sepal, x="species", y="sepal_length", color="species", title="Gjatësia mesatare e sepalëve sipas specieve")
st.plotly_chart(fig3)
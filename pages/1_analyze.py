import streamlit as st
import pandas as pd
import plotly.express as px


if "form_submitted" not in st.session_state or not st.session_state["form_submitted"]:
    st.warning("please submit the fomr on the home page first")
    st.page_link("home.py", label="Go to home page")
    st.stop()

@st.cache_data
def read_date():
    data = pd.read_parquet("shnik_mini.parquet")
    return data


def get_statistics(data, anun, azaganun=None, haeranun=None):
    new_data =  data[data["anun"] == anun]
    if azaganun:
        new_data = new_data[new_data["azaganun"] == azaganun]
    if haeranun:
        new_data = new_data[new_data["haeranun"] == haeranun]
    return new_data

def get_plots(new_data):
    d = new_data.groupby(["marz"])["anun"].count().reset_index()
    d=d.sort_values(by="anun",ascending=True)
    plot_bar = px.bar(y=d["marz"].tolist(),x=d["anun"].tolist(),orientation='h')
    plot_bar=plot_bar.update_layout(xaxis_title="count",yaxis_title="marz")

    d=new_data.groupby(["tari"])["anun"].count()
    plot_bar2 = px.bar(x=d.index,y=d.values)
    plot_bar2 = plot_bar2.update_layout(xaxis_title="Year born",yaxis_title="count")
    return plot_bar, plot_bar2


data = read_date()

anun = st.session_state["anun"]
azaganun = st.session_state["azaganun"]
haeranun = st.session_state["haeranun"]

new_data = get_statistics(data, anun, azaganun, haeranun)

col1, col2 = st.columns([0.3, 0.7])

if new_data.empty:
    st.write("No data found fot the given citeria.")
    st.page_link("home.py", label="Go to home page")    
else:
    st.write(new_data.head(10))
    # col1, col2 = st.columns([0.3, 0.7])
    plot1, plot2 = get_plots(new_data)
    with col1:
        st.plotly_chart(plot1)
    with col2:
        st.plotly_chart(plot2)
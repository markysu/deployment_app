import streamlit as st

st.set_page_config(
    page_title= "Homee",
    page_icon="🏠",
    layout="wide",
)


form = st.form(key="my_form")
anun = form.text_input("anun","")
azaganun = form.text_input("azaganun","")
haeranun = form.text_input("haeranun","")
submit_button = form.form_submit_button(label="submit")


if submit_button:
    st.session_state["form_submitted"] = True
    st.markdown("### Data is being analyzed, go to analyze page to see the results")
    st.page_link("pages/1_analyze.py", label="analyze")    
    st.page_link("pages/2_contacts.py", label="contacts")
    st.session_state["anun"]=anun
    st.session_state["azaganun"]=azaganun
    st.session_state["haeranun"]=haeranun

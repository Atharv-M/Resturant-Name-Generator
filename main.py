import streamlit as st
import langchain_helper
st.title(" Restaurant Name Genreator")
cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","American","Mexican","Arabic","Italian","Chinese"))

if cuisine:
    response=langchain_helper.generate_resturant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_tems=response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_tems:
        st.write("-",item)
import streamlit as st
import pandas as pd


def show():

    df = pd.read_csv("desktop_streamlit.csv")

    st.title('Download demo set 3')

    st.subheader('Download Button without an output file name')

    with st.echo():
        st.download_button(
            label='Download DF',
            data=df.to_csv().encode('utf-8'),
            mime="text/csv"
        )
    st.markdown('---')

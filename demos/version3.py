import streamlit as st
import pandas as pd


def show():
    st.write(
        """
        ## Version 3
        Covers use cases from 3nd iteration
        """
    )
    df = pd.read_csv("desktop_streamlit.csv")

    st.subheader('Download Button without an output file name')

    with st.echo():
        st.download_button(
            label='Download DF',
            data=df.to_csv().encode('utf-8'),
            mime="text/csv"
        )
    st.markdown('---')
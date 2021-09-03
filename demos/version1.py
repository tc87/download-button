import streamlit as st
import pandas as pd
import numpy as np


def show():
    st.write(
        """
        ## Demo Set 1
        """
    )
    df = pd.read_csv("desktop_streamlit.csv")

    st.title('Download Button')

    st.subheader('Download a Text File')
    with st.echo():
        st.download_button(
            "DOWNLOAD!",
            "trees",
            "string.txt",
            "text/plain"
        )
    st.markdown('---')

    st.subheader('Download a CSV file')
    with st.echo():
        text_contents = '''
        Foo, Bar
        123, 456
        789, 000
        '''
        st.download_button('Download CSV', text_contents, 'aaa.csv', 'text/csv')
    st.markdown('---')

    st.subheader('Download from a File Pointer')
    with st.echo():
        with open("bird.png", "rb") as fp:
            btn = st.download_button(
                "Download IMAGE",
                fp,
                "just-bird.png",
                "image/png"
            )
    st.markdown('---')

    st.subheader('Download as Encoded String')

    with st.echo():
        st.write(df)

        st.download_button(
            "Click to download",
            df.to_csv().encode('utf-8'),
            "name_a.csv",
            "text/csv"
        )
    st.markdown('---')

    st.subheader('Download as Binary File')

    with st.echo():
        binary_contents = b'whatever'

        # Defaults to 'application/octet-stream'
        st.download_button('Download binary file', binary_contents)

    st.markdown('---')

    st.subheader('Callbacks w/ Download Button')

    with st.echo():
        def callback():
            st.success('Inside download button callback')

        st.download_button(
            "Press to Download",
            df.to_csv().encode('utf-8'),
            "name_a.csv",
            "text/csv",
            on_click=callback,
            key='callback'
        )

    st.markdown('---')

    st.subheader('Large DataFrames')

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    with st.echo():
        if 'df' not in st.session_state:
            st.session_state.df = pd.DataFrame(np.random.randint(0, 120, size=(5000, 5000)))
        csv = convert_df(st.session_state.df)
        st.download_button(
            "Press to Download",
            csv,
            "name_a.csv",
            "text/csv",
            key='large'
        )

    st.markdown('---')

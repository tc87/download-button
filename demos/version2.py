import streamlit as st
import pandas as pd
import numpy as np


def show():
    df = pd.read_csv("desktop_streamlit.csv")

    st.title('Download demo set 2')

    st.subheader('Unicode characters in file names')
    with st.echo():
        st.download_button(
            "DOWNLOAD!",
            "trees",
            "Gürzenichstraße.txt",
            "text/plain"
        )
    st.markdown('---')

    st.subheader('Download on Streamlit Sharing')
    with st.echo():
        text_contents = '''
        Foo, Bar
        123, 456
        789, 000
        '''
        st.download_button('Download CSV', text_contents, 'aaa.csv', 'text/csv')
    st.markdown('---')


    st.subheader('Download button and Forms')
    st.write('Adding a download button inside a form throws an exception')
    with st.echo():
        if st.checkbox('Show Exception', key='form-checkbox'):
            with st.form(key='my_form'):
                text = st.text_input('Enter some text')
                st.download_button(
                    'Label',
                    df.to_csv().encode('utf-8'),
                    "name_a.csv",
                    "text/csv",
                    key='form-download'
                )
                submit = st.form_submit_button('Submit')

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

    st.subheader('Exception: Setting the value of download button via State API')

    with st.echo():
        if st.checkbox('Show Exception'):
            st.session_state.my_key = 'blah'

            st.download_button(
                "Press to Download",
                df.to_csv().encode('utf-8'),
                "name_a.csv",
                "text/csv",
                on_click=callback,
                key='my_key'
            )

    st.markdown('---')

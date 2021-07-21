import streamlit as st
import pandas as pd

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

st.subheader('Exceptions')

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

st.subheader('Download button and Forms')

with st.echo():
    with st.form(key='my_form'):
        text = st.text_input('Enter some text')
        st.download_button(
            "Press to Download",
            df.to_csv().encode('utf-8'),
            "name_a.csv",
            "text/csv",
            key='form-download'
        )
        submit = st.form_submit_button('Submit')
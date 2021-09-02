import streamlit as st
from . import version1
from . import version2
from . import version3



def show_version1():

    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    version1.show()


def show_version2():

    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    version2.show()


def show_version3():

    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    version3.show()


if __name__ == "__main__":
    pass
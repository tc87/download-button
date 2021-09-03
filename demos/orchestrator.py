import streamlit as st
from . import version1
from . import version2
from . import version3



def show_version1():

    st.write(
            """
        # Download Demo Set 1
        """
    )

    st.write("---")
    version1.show()


def show_version2():

    st.write(
        """
        # Download Demo Set 2
        """
    )

    st.write("---")
    version2.show()


def show_version3():

    st.write(
       """
        # Download Demo Set 3
        """
    )

    st.write("---")
    version3.show()


if __name__ == "__main__":
    pass

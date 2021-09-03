import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

import streamlit as st

VERSION = ".".join(st.__version__.split(".")[:2])

from demos import orchestrator

demo_pages = {
    "Version1": orchestrator.show_version1,
    "Version2": orchestrator.show_version2,
    "Version3": orchestrator.show_version3,
}



contributors = []

intro = f"""
Launch release for Download Button
"""

release_notes = f"""
---
**Key Features**
- Download large files
- Filenames can contain unicode symbols
- Files downloaded with correct filenames on Streamlit Cloud

**Error Scenarios**
- Raise exception when download button used inside form

"""
# End release updates


def draw_main_page():
    st.write(
        f"""
        # Prototype based off Streamlit v{VERSION}!
        """
    )

    st.write(intro)

    st.write(release_notes)


# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    pages.insert(0, "Release Notes")
    st.sidebar.title(f"State Demos")
    query_params = st.experimental_get_query_params()
    # TODO: This doesn't work yet. Locally it actually works, but on Streamlit Sharing
    #   it doesn't somehow. The query params are actually read and parsed correctly,
    #   but it doesn't manage to set the index based on it. Seems to be a weird
    #   interaction between the widget value in session state and value given in arg.
    #   See if this is fixed in final session state version.
    if "page" in query_params and query_params["page"][0] == "headliner":
        index = 1
    else:
        index = 0
    selected_demo = st.sidebar.radio("", pages, index, key="pages")
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()

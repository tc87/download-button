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
This release launches download button as well as bug fixes and improvements.
"""

release_notes = f"""
---
# ✨ Release Highlight

## ⬇️ Download Button

- Previous to this release, there had been hack ways to use download functionality within Streamlit, but none of these were great for general use - notably most didn't play well with the [Streamlit Cloud platform](https://streamlit.io/cloud). With `st.download_button` you can now seamlessly use download functionality both locally and with on our cloud platform. 

Want to play with some samples? Check out the radio buttons in the sidebar and check out [the docs](https://docs.streamlit.io/en/stable/api.html?highlight=download%20button#streamlit.download_button) for more info!

## 🧩 Other notable updates

Below are some other notable updates on this release:

- 🛑 We made changes to improve the redacted exception experience on Streamlit Cloud. When `client.showErrorDetails=true`  exceptions display the Error Type and the Traceback, but redact the actual error text to prevent data leaks. [[3713](https://github.com/streamlit/streamlit/pull/3713)]
- 🖥️ Since Macs are set to verify SSL in Python, if certificates aren't installed, a `SSL: CERTIFICATE_VERIFY_FAILED` error propagates. We removed HTTPS in order to solve this issue. [[3744](https://github.com/streamlit/streamlit/pull/3744)]
- 🔑 Integers can now also be used as keys in widget declarations. This helps community members who use integers for keys. This change updates type annotations to allow it, and ensures integer keys are converted to strings. [[3697](https://github.com/streamlit/streamlit/pull/3697)]

[Click here](https://github.com/streamlit/streamlit/compare/0.87.0...0.88.0) to check out all updates. As always, thank you to all [our contributors](https://github.com/streamlit/streamlit/graphs/contributors) who help make Streamlit awesome!

"""

Connect With Us
We can be found at https://streamlit.io and https://twitter.com/streamlit
Come by the forums if you'd like to ask questions, post awesome apps, or just say hi!


# End release updates


def draw_main_page():
    st.write(
        f"""
        # Welcome to Streamlit 0.88! 👋
        """
    )

    st.write(intro)

    st.write(release_notes)


# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    pages.insert(0, "Release Notes")
    st.sidebar.title(f"Streamlit v0.88")
    query_params = st.experimental_get_query_params()
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

import streamlit as st
from streamlit_option_menu import option_menu
from apps import mainpage, secondpage, thirdpage, fourthpage, enkripsi


apps = [
    {"func": mainpage.app, "title": "Pembobolan Data", "icon": "house"},
    {"func": secondpage.app, "title": "Kasus Pembobolan Data", "icon": "map"},
    {"func": thirdpage.app, "title": "Terjadinya Breach", "icon": "book"},
    {"func": fourthpage.app, "title": "Penanggulangan", "icon": "easel"},
    {"func": enkripsi.app, "title": "Kriptografi", "icon": "boombox"},
]
titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
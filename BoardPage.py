import streamlit as st
from streamlit_option_menu import option_menu
import UserPage
import ChatPage

def GoChatPage():
    ChatPage.chat() #chat 기능 구현 함수 실행
def GoUserPage():
    UserPage.user() #user 기능 구현 함수 실행


def board():
    with st.sidebar: #사이드바 디자인
        choice = option_menu("Menu", ["Chat Page", "User Page"],
                             icons=['bi bi-robot', 'kanban'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    })
    
    if choice == "Chat Page":
        GoChatPage()
    elif choice == "User Page":
        GoUserPage()



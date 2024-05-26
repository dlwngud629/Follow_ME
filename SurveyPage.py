import streamlit as st
import BoardPage
st.set_page_config(layout="wide") #streamlit은 가로 레이아웃 제한이 있어서 화면을 넓게 사용하기 위한 코드


def survey():
    left, center, right = st.columns([1, 2, 1]) #st.set_page_config(layout="wide")를 사용해서 왼쪽 정렬을 가운데 정렬로 바꿈

    with center:
        st.title("따라와")
        st.write("이 페이지에는 설문조사 기능을 구현할 겁니다.")

        if st.button("Go to Chat Page"):
            st.session_state['page'] = 'chat'
            st.experimental_rerun()

#페이지 제어 코드
if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state['page'] = 'survey'

if st.session_state['page'] == 'survey':
    survey()
elif st.session_state['page'] == 'chat':
    BoardPage.board()

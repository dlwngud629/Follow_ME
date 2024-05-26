import streamlit as st
import folium
from streamlit_folium import st_folium

def chat():
    st.header("챗봇과 지도 기능 구현 페이지")
    
    map_col, chat_col = st.columns([1, 2])

    # Folium으로 지도 생성
    location = [35.846816, 127.129920]  # 주어진 위도, 경도
    zoom_start = 14  # 줌 레벨
    folium_map = folium.Map(location=location, zoom_start=zoom_start)

    with map_col: #지도에 관한 구현
        st_folium(folium_map, height=500)  

    with chat_col:  #챗봇에 관한 구현
        st.write("여기에 챗봇 기능을 구현하세요.")

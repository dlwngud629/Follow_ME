import streamlit as st
import folium
from streamlit_folium import st_folium
from GptLoad import openapi

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
        restaurants = ["현대옥", "해이루", "덕천식당"]
        st.write("전주 " + str(restaurants[0]) + " 만족하시나요 ?")
        st.write(openapi(restaurants[0]))
        
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Yes"):
                st.write("Yes를 선택하셨습니다.")
                
        with col2:
            if st.button("No"):
                st.write("No를 선택하셨습니다.")
                st.write(openapi(restaurants[1]))


    


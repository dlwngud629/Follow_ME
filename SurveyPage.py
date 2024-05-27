import streamlit as st
import BoardPage
import sqlite3
st.set_page_config(layout="wide") #streamlit은 가로 레이아웃 제한이 있어서 화면을 넓게 사용하기 위한 코드


def survey():
    left, center, right = st.columns([1, 2, 1]) #st.set_page_config(layout="wide")를 사용해서 왼쪽 정렬을 가운데 정렬로 바꿈

    with center:
        st.title("따라와")
        st.write("이 페이지에는 설문조사 기능을 구현할 겁니다.")

        #카페 설문조사
        cafeSlider0 = st.slider(
            label="Cafe Component 0: 커피 맛을 중요하게 생각하시나요?", 
            min_value=1,        
            max_value=10,            
            value=6               
        )
        cafeSlider1 = st.slider(
            label="Cafe Component 1: 디저트를 중요하게 생각하시나요?", 
            min_value=1,        
            max_value=10,            
            value=6                    
        )
        cafeSlider2 = st.slider(
            label="Cafe Component 2: 이색 카페는 어떠신가요?",  
            min_value=1,        
            max_value=10,            
            value=6                 
        )

        #식당 설문조사
        restaurantSlider0 = st.slider(
            label="restaurant Component 0: 맛을 중요하게 생각하시나요?", 
            min_value=1,        
            max_value=10,            
            value=6         
        )
        restaurantSlider1 = st.slider(
            label="restaurant Component 1: 가게가 친절한 것을 중요하게 생각하시나요?", 
            min_value=1,        
            max_value=10,            
            value=6               
        )
        restaurantSlider2 = st.slider(
            label="restaurant Component 2: 가성비를 중요하게 생각하시나요?",  
            min_value=1,        
            max_value=10,            
            value=6                   
        )

        #관광지 설문조사
        attractionSlider0 = st.slider(
            label="attraction Component 0: 인스타를 하시나요?", 
            min_value=1,        
            max_value=10,            
            value=6             
        )
        attractionSlider1 = st.slider(
            label="attraction Component 1: 체험이 많았으면 좋겠나요?", 
            min_value=1,        
            max_value=10,            
            value=6              
        )
        attractionSlider2 = st.slider(
            label="attraction Component 2: 볼거리가 많은건 어떠신가요?",  
            min_value=1,        
            max_value=10,            
            value=6                
        )

        


        if st.button("Go to Chat Page"):
            updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2)
            st.session_state['page'] = 'chat'
            st.experimental_rerun()



def updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2):
    conn = sqlite3.connect('location.db')  # Connect to SQLite Database
    cursor = conn.cursor()

    # 새로운 설문마다 이전 점수를 삭제하기 위한 코드
    cursor.execute('DROP TABLE IF EXISTS cafescore')
    cursor.execute('DROP TABLE IF EXISTS restaurantscore')
    cursor.execute('DROP TABLE IF EXISTS attractionscore')

    #테이블 생성
    cursor.execute('''
    CREATE TABLE cafescore (
        name TEXT,
        score REAL DEFAULT 0.0
    )
    ''')
    cursor.execute('''
    CREATE TABLE restaurantscore (
        name TEXT,
        score REAL DEFAULT 0.0
    )
    ''')
    cursor.execute('''
    CREATE TABLE attractionscore (
        name TEXT,
        score REAL DEFAULT 0.0
    )
    ''')

    #각 테이블에 장소 삽입
    cursor.execute('''
    INSERT INTO cafescore (name)
    SELECT DISTINCT name FROM cafe
    ''')
    cursor.execute('''
    INSERT INTO restaurantscore (name)
    SELECT DISTINCT name FROM restaurant
    ''')
    cursor.execute('''
    INSERT INTO attractionscore (name)
    SELECT DISTINCT name FROM attraction
    ''')

    #각 테이블에 점수 반영
    cursor.execute('''
    UPDATE cafescore
    SET score = (
        SELECT SUM(
            CASE WHEN cafe.feature = 'Component0' THEN cafe.value * ? 
                 WHEN cafe.feature = 'Component1' THEN cafe.value * ? 
                 WHEN cafe.feature = 'Component2' THEN cafe.value * ? 
            END
        )
        FROM cafe
        WHERE cafe.name = cafescore.name
    )
    ''', (cafeSlider0, cafeSlider1, cafeSlider2))
    cursor.execute('''
    UPDATE restaurantscore
    SET score = (
        SELECT SUM(
            CASE WHEN restaurant.feature = 'Component0' THEN restaurant.value * ? 
                 WHEN restaurant.feature = 'Component1' THEN restaurant.value * ? 
                 WHEN restaurant.feature = 'Component2' THEN restaurant.value * ? 
            END
        )
        FROM restaurant
        WHERE restaurant.name = restaurantscore.name
    )
    ''', (restaurantSlider0, restaurantSlider1, restaurantSlider2))
    cursor.execute('''
    UPDATE attractionscore
    SET score = (
        SELECT SUM(
            CASE WHEN attraction.feature = 'Component0' THEN attraction.value * ? 
                 WHEN attraction.feature = 'Component1' THEN attraction.value * ? 
                 WHEN attraction.feature = 'Component2' THEN attraction.value * ? 
            END
        )
        FROM attraction
        WHERE attraction.name = attractionscore.name
    )
    ''', (attractionSlider0, attractionSlider1, attractionSlider2))

    conn.commit()  
    conn.close()  



#페이지 제어 코드
if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state['page'] = 'survey'

if st.session_state['page'] == 'survey':
    survey()
elif st.session_state['page'] == 'chat':
    BoardPage.board()

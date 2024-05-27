import streamlit as st
import sqlite3

def user():
    st.write("각 장소에 대한 평점 조절 기능 구현 페이지")

    dbFile = 'location.db'

    conn = None
    conn = sqlite3.connect(dbFile)
    st.write("본 페이지는 설문조사에 의한 사용자의 관광지 만족도를 예상한 점수를 보여줍니다.")
    st.write("저희의 예상치가 마음에 들지 않다면 세부적으로 조절하실 수 있습니다")
    if conn is not None: #관광지, 카페, 레스토랑 중 선택
        placeName = st.selectbox(
            "조절하고 싶은 장소 유형을 선택하세요:",
            ["관광지", "카페", "레스토랑"],
            index=0  # 기본 선택 옵션
        )

        # 선택된 카테고리에 해당하는 테이블 이름
        tableDict = {"관광지": "attractionscore", "카페": "cafescore", "레스토랑": "restaurantscore"}
        table = tableDict[placeName]

        st.subheader(f"{placeName}에서 흥미로운 장소가 보인다면 높은 점수를 주세요!")
        
        # 데이터베이스에서 현재 점수를 조회
        cur = conn.cursor()
        cur.execute(f"SELECT name, score FROM {table}")
        rows = cur.fetchall()

        # 각 장소에 대한 슬라이더 생성 및 점수 조절
        for name, score in rows:
            newScore = st.slider(f"{name}", 0, 10, int(score), 1, key=f"{table}_{name}")
            # 슬라이더 값이 변경되면 데이터베이스 업데이트
            if newScore != score:
                cur.execute(f"UPDATE {table} SET score = ? WHERE name = ?", (round(newScore, 1), name))
                conn.commit()

        conn.close()

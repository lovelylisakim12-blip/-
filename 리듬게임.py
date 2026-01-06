import streamlit as st
import random
import time

# ================== 페이지 설정 ==================
st.set_page_config(
    page_title="NEON RHYTHM",
    page_icon="🎵",
    layout="centered"
)

# ================== CSS (다크 + 형광 스타일) ==================
st.markdown("""
<style>
body {
    background-color: #0b0f1a;
}
.game-box {
    background: #0b0f1a;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}
.arrow {
    font-size: 100px;
    font-weight: bold;
    text-shadow:
        0 0 10px #00f6ff,
        0 0 20px #00f6ff,
        0 0 40px #00f6ff;
    color: #00f6ff;
}
.score {
    color: #ffffff;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# ================== 세션 상태 ==================
if "score" not in st.session_state:
    st.session_state.score = 0
if "arrow" not in st.session_state:
    st.session_state.arrow = random.choice(["⬆", "⬇", "⬅", "➡"])
if "time_limit" not in st.session_state:
    st.session_state.time_limit = 3.0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# ================== 타이틀 ==================
st.markdown("<h1 style='color:#00f6ff; text-align:center;'>🎵 NEON RHYTHM 🎵</h1>", unsafe_allow_html=True)

# ================== 게임 오버 ==================
if st.session_state.game_over:
    st.error("💥 GAME OVER")
    st.write(f"### 최종 점수: {st.session_state.score}")
    if st.button("🔁 다시 시작"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()

else:
    # ================== 시간 초과 체크 ==================
    if time.time() - st.session_state.start_time > st.session_state.time_limit:
        st.session_state.game_over = True
        st.experimental_rerun()

    # ================== 게임 화면 ==================
    st.markdown("<div class='game-box'>", unsafe_allow_html=True)
    st.markdown(f"<div class='arrow'>{st.session_state.arrow}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score'>점수: {st.session_state.score}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ================== 입력 버튼 ==================
    col1, col2, col3, col4 = st.columns(4)
    buttons = {
        "⬆": col2.button("⬆"),
        "⬇": col3.button("⬇"),
        "⬅": col1.button("⬅"),
        "➡": col4.button("➡")
    }

    for key, pressed in buttons.items():
        if pressed:
            if key == st.session_state.arrow:
                st.session_state.score += 1
                st.session_state.arrow = random.choice(["⬆", "⬇", "⬅", "➡"])
                st.session_state.start_time = time.time()

                # 난이도 상승
                if st.session_state.time_limit > 0.7:
                    st.session_state.time_limit -= 0.1
            else:
                st.session_state.game_over = True
            st.experimental_rerun()
        

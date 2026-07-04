import streamlit as st
import random

st.set_page_config(
    page_title="가위바위보 게임",
    page_icon="🎮",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Do+Hyeon&display=swap');

[data-testid="stAppViewContainer"]{
    background:#ffd6eb;
}

.block-container{
    max-width:650px;
    padding-top:50px;
}

h1{
    font-family:'Press Start 2P', cursive;
    text-align:center;
    color:#ff2f7d;
    font-size:36px;
}

.game{
    text-align:center;
    font-family:'Do Hyeon',sans-serif;
}

.score{
    display:inline-block;
    background:white;
    padding:8px 18px;
    border-radius:15px;
    font-size:22px;
    font-weight:bold;
    color:#ff2f7d;
    box-shadow:0 3px 10px rgba(0,0,0,.15);
}

.result{
    background:white;
    border-radius:20px;
    padding:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    box-shadow:0 5px 15px rgba(0,0,0,.15);
    margin-top:25px;
}

.stButton > button{
    height:140px;
    border-radius:25px;
    font-size:70px;
    background:white;
    border:4px solid #ff6fae;
    transition:0.2s;
}

.stButton > button:hover{
    transform:scale(1.08);
    background:#ffe7f2;
}
</style>
""", unsafe_allow_html=True)

# ---------------- session ----------------
if "user" not in st.session_state:
    st.session_state.user = 0

if "computer" not in st.session_state:
    st.session_state.computer = 0

if "result" not in st.session_state:
    st.session_state.result = ""

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""

emoji = {
    "가위":"✌️",
    "바위":"✊",
    "보":"✋"
}

# ---------------- 상단 ----------------


left, right = st.columns([5,2])

with left:
    score_placeholder = st.empty()

with right:
    if st.button("🏠 처음으로"):
        st.session_state.user = 0
        st.session_state.computer = 0
        st.session_state.result = ""
        st.session_state.user_choice = ""
        st.session_state.computer_choice = ""
        st.rerun()

score_placeholder.markdown(
    f"""
    <div class='score'>
    👤 {st.session_state.user}
    &nbsp;&nbsp;:&nbsp;&nbsp;
    {st.session_state.computer} 💻
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- 제목 ----------------
st.title("🎮 가위바위보")

st.markdown(
"<div class='game'><h3>컴퓨터를 이겨보세요!</h3></div>",
unsafe_allow_html=True
)

st.markdown(
"""
<div style="text-align:center;font-size:90px;">
✌️ ✊ ✋
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- 게임 함수 ----------------

def play(user):

    computer=random.choice(["가위","바위","보"])

    st.session_state.user_choice=user
    st.session_state.computer_choice=computer

    if user==computer:
        st.session_state.result="😄 무승부!"

    elif (
        (user=="가위" and computer=="보") or
        (user=="바위" and computer=="가위") or
        (user=="보" and computer=="바위")
    ):
        st.session_state.result="🎉 승리!"
        st.session_state.user+=1

    else:
        st.session_state.result="😭 패배!"
        st.session_state.computer+=1

# ---------------- 버튼 ----------------

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("✌️", use_container_width=True):
        play("가위")

with c2:
    if st.button("✊", use_container_width=True):
        play("바위")

with c3:
    if st.button("✋", use_container_width=True):
        play("보")

# 버튼을 누른 후 다시 점수판 갱신
score_placeholder.markdown(
f"""
<div class='score'>
👤 {st.session_state.user}
&nbsp;&nbsp;:&nbsp;&nbsp;
{st.session_state.computer} 💻
</div>
""",
unsafe_allow_html=True
)

# ---------------- 결과 ----------------

if st.session_state.result:

    st.markdown(
    f"""
    <div class="result">

    <div style="font-size:65px;">
    {emoji[st.session_state.user_choice]}
    &nbsp;&nbsp;VS&nbsp;&nbsp;
    {emoji[st.session_state.computer_choice]}
    </div>

    <br>

    👤 사용자 :
    <b>{st.session_state.user_choice}</b>

    <br><br>

    💻 컴퓨터 :
    <b>{st.session_state.computer_choice}</b>

    <hr>

    <span style="color:#ff2f7d;">
    {st.session_state.result}
    </span>

    </div>
    """,
    unsafe_allow_html=True
)

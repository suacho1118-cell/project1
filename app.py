import streamlit as st
import random

st.set_page_config(
    page_title="🎮 가위바위보 게임",
    page_icon="🎮",
    layout="centered"
)

# ------------------- CSS -------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Do+Hyeon&display=swap');

html, body, [data-testid="stAppViewContainer"]{
    background:#ffd6eb;
}

.main{
    display:flex;
    justify-content:center;
}

.block-container{
    max-width:650px;
    text-align:center;
    padding-top:30px;
}

h1{
    font-family:'Press Start 2P', cursive;
    color:#ff2f7d;
    text-align:center;
}

.gamefont{
    font-family:'Do Hyeon', sans-serif;
    font-size:28px;
}

.score{
    background:white;
    border-radius:18px;
    padding:18px;
    font-size:30px;
    font-weight:bold;
    color:#ff2f7d;
    box-shadow:0 5px 15px rgba(0,0,0,0.15);
}

.result{
    background:white;
    border-radius:18px;
    padding:18px;
    margin-top:20px;
    font-size:28px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    height:70px;
    border-radius:18px;
    font-size:26px;
    font-weight:bold;
    background:#ff6fae;
    color:white;
}

.stButton>button:hover{
    background:#ff4c96;
}

</style>
""", unsafe_allow_html=True)

# ------------------- 점수 -------------------
if "user" not in st.session_state:
    st.session_state.user = 0

if "computer" not in st.session_state:
    st.session_state.computer = 0

if "result" not in st.session_state:
    st.session_state.result = ""

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

# ------------------- 함수 -------------------
choices = {
    "가위":"✌️",
    "바위":"✊",
    "보":"✋"
}

def play(user):

    computer = random.choice(list(choices.keys()))

    st.session_state.user_choice = user
    st.session_state.computer_choice = computer

    if user == computer:
        st.session_state.result = "😆 무승부!"

    elif (
        (user=="가위" and computer=="보") or
        (user=="바위" and computer=="가위") or
        (user=="보" and computer=="바위")
    ):
        st.session_state.result="🎉 승리!"
        st.session_state.user +=1

    else:
        st.session_state.result="😭 패배!"
        st.session_state.computer +=1

# ------------------- 제목 -------------------
st.title("🎮 가위바위보 게임")

st.markdown("<div class='gamefont'>컴퓨터를 이겨보세요!</div>",
unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

# ------------------- 이미지 -------------------
st.markdown(
"""
<div style="font-size:90px;text-align:center;">
✌️ ✊ ✋
</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>",unsafe_allow_html=True)

# ------------------- 점수 -------------------
st.markdown(
f"""
<div class="score">
💻 컴퓨터 : 👤 사용자 <br><br>
{st.session_state.computer} : {st.session_state.user}
</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>",unsafe_allow_html=True)

# ------------------- 버튼 -------------------
c1,c2,c3 = st.columns(3)

with c1:
    if st.button("✌️ 가위"):
        play("가위")

with c2:
    if st.button("✊ 바위"):
        play("바위")

with c3:
    if st.button("✋ 보"):
        play("보")

# ------------------- 결과 -------------------
if st.session_state.result != "":

    st.markdown(
    f"""
    <div class="result">

    👤 사용자 : {choices[st.session_state.user_choice]}
    ({st.session_state.user_choice})

    <br><br>

    💻 컴퓨터 : {choices[st.session_state.computer_choice]}
    ({st.session_state.computer_choice})

    <hr>

    {st.session_state.result}

    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown("<br>",unsafe_allow_html=True)

# ------------------- 초기화 -------------------
if st.button("🔄 처음으로 돌아가기"):
    st.session_state.user=0
    st.session_state.computer=0
    st.session_state.result=""
    st.session_state.user_choice=""
    st.session_state.computer_choice=""
    st.rerun()

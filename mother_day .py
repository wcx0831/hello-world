import streamlit as st
import time

# -------------------------- 页面基础配置 --------------------------
st.set_page_config(
    page_title="母亲节快乐贺卡",
    page_icon="💐",
    layout="centered"
)

# -------------------------- 粉色主题背景与样式 --------------------------
page_style = """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffd6e0, #ffb6c1, #ffe4ec);
        background-size: 400% 400%;
        animation: gradientBg 12s ease infinite;
    }

    @keyframes gradientBg {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .card-box {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 25px;
        padding: 40px 30px;
        margin-top: 30px;
        box-shadow: 0 8px 30px rgba(255, 105, 180, 0.3);
        text-align: center;
    }

    .fall-item {
        position: fixed;
        top: -50px;
        font-size: 25px;
        animation: fall 10s linear infinite;
        z-index: 9999;
    }

    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# -------------------------- 动态飘落花朵/爱心 --------------------------
fall_emojis = ["💐", "🌸", "💖", "💕", "🌹", "✨", "🌷", "💝"]
fall_html = ""
for i in range(20):
    delay = i * 0.5
    left = i * 5
    fall_html += f'<div class="fall-item" style="left:{left}%;animation-delay:{delay}s;">{fall_emojis[i % len(fall_emojis)]}</div>'
st.markdown(fall_html, unsafe_allow_html=True)

# -------------------------- 贺卡主体内容 --------------------------
st.markdown("""
<div class="card-box">
    <h1 style="color:#d63384; font-family:SimHei;">💐 母亲节快乐 💐</h1>
    <br>
    <h3 style="color:#c2185b;">致最美的妈妈</h3>
    <p style="font-size:18px; color:#666; line-height:1.8;">
    您辛苦了一辈子<br>
    温柔了岁月，温暖了时光<br>
    愿往后余生<br>
    平安喜乐，永远安康<br>
    永远做最幸福的自己 ❤️
    </p>
    <br>
    <p style="font-size:20px; color:#d63384; font-weight:bold;">爱你的孩子</p>
</div>
""", unsafe_allow_html=True)

# -------------------------- 缓慢文字加载动画 --------------------------
with st.empty():
    for text in ["💖 愿天下所有妈妈 节日快乐 💖", "💐 被温柔以待，被岁月偏爱 💐"]:
        st.markdown(f"<h3 style='text-align:center;color:#c2185b;'>{text}</h3>", unsafe_allow_html=True)
        time.sleep(1.2)

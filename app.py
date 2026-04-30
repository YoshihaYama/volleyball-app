import streamlit as st
import pandas as pd

PASSWORD = "20050419"

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("ログイン")
    pw = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if pw == PASSWORD:
            st.session_state.auth = True
            st.success("ログイン成功")
        else:
            st.error("パスワードが違います")
    st.stop()

st.title("バレーボール分析アプリ")
st.write("ログイン済みです")

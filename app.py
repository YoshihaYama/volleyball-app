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
st.header("サーブ")

if "serve_by_player" not in st.session_state:
    st.session_state.serve_by_player = {i: [] for i in range(1, 13)}

player = st.selectbox("背番号を選んでください（1〜12）", list(range(1, 13)))

serve = st.selectbox(
    "サーブ結果を選んでください",
    ["S（サービスエース）", "A（くずし）", "B（ノーマル）", "M（ミス）"]
)

if st.button("記録する"):
    st.session_state.serve_by_player[player].append(serve)
    st.success(f"背番号 {player} に {serve} を記録しました")

# 集計表示
st.subheader("選手別サーブ集計")

for p in range(1, 13):
    results = st.session_state.serve_by_player[p]
    if len(results) == 0:
        continue

    st.write(f"### 背番号 {p}")

    df = pd.DataFrame(results, columns=["result"])
    summary = df["result"].value_counts()

    st.write(summary)

    total = len(df)
    ace = summary.get("S（サービスエース）", 0)
    miss = summary.get("M（ミス）", 0)

    st.write(f"- 総サーブ数：{total}")
    st.write(f"- サービスエース率：{ace / total * 100:.1f}%")
    st.write(f"- ミス率：{miss / total * 100:.1f}%")
    st.write("---")



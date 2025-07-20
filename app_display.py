import streamlit as st

# --- 頁面設定 ---
st.set_page_config(
    page_title="EVA：你的AI智能生活助理",
    page_icon="🤖", # 可以在這裡放可愛的機器人或助手圖標
    layout="centered"
)

# --- 標題與簡介 ---
st.title("🤖 EVA：你的AI智能生活助理")
st.write("---") # 分隔線
st.markdown("""
🎉 厭倦了被生活瑣事綁架嗎？《EVA》就是你的最佳解決方案！
我們打造的 AI 智能助理，能直接在 LINE 上，用你最習慣的自然語言，**一句話搞定大小事**。
不再手忙腳亂，讓你把時間留給更重要的事！
""")
st.write("---")

# --- 如何使用 EVA (核心功能展示) ---
st.header("✨ EVA 如何貼近你的生活？")

# 功能區塊 1: 請假
st.subheader("1. 救急！幫你神來一筆的「請假理由」")
st.write("突然需要請假，卻苦惱該怎麼開口？EVA 不只幫你寫請假信，還能提供「合理」理由。")
st.markdown("---") # 小分隔線
st.markdown("**➡️ 你只要說：** `EVA，幫我寫一封請假信給老闆，就說我這兩天身體不舒服，語氣要誠懇。`")
st.markdown("**✅ EVA 自動幫你：** 立即生成格式完整、禮貌的請假信草稿，並提供建議理由。確認後，還能直接幫你發送到老闆 Email 信箱！")
st.markdown("---")


# 功能區塊 2: 記帳
st.subheader("2. 懶人「輕鬆記帳」，掌握收支不費力")
st.write("錢都去哪了？讓 EVA 幫你把每筆開銷都記得清清楚楚！")
st.markdown("---")
st.markdown("**➡️ 你只要說：** `EVA，我今天午餐花了 180 元買便當，記帳一下。`")
st.markdown("**✅ EVA 自動幫你：** 將支出自動記錄到你綁定的 Google 試算表或其他工具中，讓你對財務狀況一目了然。")
st.markdown("---")

# 更多功能簡述
st.subheader("💡 更多便利功能！")
st.write("EVA 還能幫你：**自動安排行程、輕鬆發送郵件、即時查詢**等。")
st.markdown("""
**《EVA》的目標就是讓你動動口，生活大小事就能輕鬆搞定！**
它是你最貼心、最懂你的生活夥伴。
""")

st.write("---")

# --- LINE Bot 連結區塊 ---
st.header("🚀 立即體驗 EVA！")
st.write("掃描下方 QR Code，將 EVA 加入 LINE 好友，開始你的智能生活！")

# 這裡可以放你的 LINE Bot QR Code 圖片，請替換 'your_line_qr_code.png'
# 你需要將你的 LINE Bot QR Code 圖片檔案（例如從 LINE Developers 下載）放到與 app_display.py 相同的資料夾
# st.image("your_line_qr_code.png", caption="掃描加入 EVA 好友", width=200)

# 如果沒有圖片，可以提供文字連結
st.markdown("[點此加入 EVA LINE 好友](你的LINE Bot的加入好友連結)")
st.markdown("---")

# --- 隱私權政策 (重要！) ---
st.header("🔒 隱私權政策")
st.markdown("""
本服務會收集您的 LINE User ID 及您發送的訊息內容，以提供排程、記帳、信件生成等服務。
所有資料僅用於 Bot 功能運作，不會用於商業用途。
您的資料可能會透過 Google API (日曆、試算表、Gmail) 進行處理，以執行您的指令。
我們不會主動將您的資料分享給第三方（除了必要的服務提供商，例如 AI 模型）。
如果您有任何隱私問題，請聯繫：[raison8120@outlook.com]
""")
st.write("---")

st.info("© 2025 EVA AI Assistant. All Rights Reserved.")

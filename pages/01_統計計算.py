import streamlit as st
import statistics

st.title("統計計算")

numbers_input = st.text_area(
    "数値を入力してください（カンマまたは改行で区切る）",
    placeholder="1, 2, 3, 4, 5"
)

if numbers_input:
    try:
        # 入力を数値のリストに変換
        numbers = []
        for item in numbers_input.replace('\n', ',').split(','):
            item = item.strip()
            if item:
                numbers.append(float(item))

        if len(numbers) > 0:
            st.subheader("計算結果")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("個数", len(numbers))
                st.metric("合計", sum(numbers))

            with col2:
                st.metric("平均", f"{statistics.mean(numbers):.2f}")
                st.metric("最小値", min(numbers))

            with col3:
                st.metric("最大値", max(numbers))
                if len(numbers) > 1:
                    st.metric("標準偏差", f"{statistics.stdev(numbers):.2f}")
                else:
                    st.metric("標準偏差", "N/A")

    except ValueError:
        st.error("数値の入力形式が正しくありません")

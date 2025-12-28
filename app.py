import streamlit as st

st.title("四則演算計算機")

col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("最初の数値", value=0.0)

with col2:
    operation = st.selectbox(
        "演算を選択",
        ["+", "-", "×", "÷"]
    )

with col3:
    num2 = st.number_input("次の数値", value=0.0)

if st.button("計算", use_container_width=True):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "×":
        result = num1 * num2
    elif operation == "÷":
        if num2 == 0:
            st.error("ゼロで割ることはできません")
            st.stop()
        result = num1 / num2

    st.success(f"結果: {num1} {operation} {num2} = {result}")

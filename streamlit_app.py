# 3
import streamlit as st
import random as rd
import string

# 4
st.title("Awesome Password Generator")

# 5
st.header("The Best App For Generating Secure Passwords!", divider='rainbow')

# 6
def gen_pass(chars, length):
    return "".join(rd.choices(chars, k=length))


# 7
name = st.text_input("Please enter your name:")

if name:
    st.write(f"Hello, {name}! Please define your desired password:")

    # 8
    options = ["Option1", "Option 2", "Option 3"]
    st.selectbox("Why do you need a password?", options)

    # 9
    chars = ""
    if st.checkbox("Upper Case letters"):
        chars += string.ascii_uppercase
    if st.checkbox("Lower Case letters"):
        chars += string.ascii_lowercase
    if st.checkbox("Digits"):
        chars += string.digits
    if st.checkbox("Special Characters"):
        chars += string.punctuation

    # 10
    length = st.number_input(
        "Select the length of your password:", min_value=5, max_value=30, step=1
    )

    # 11
    check = st.checkbox("I Agree To Awesome Generator's Terms")
    if check:
        # 12
        btn = st.button("Generate Password")
        if btn:
            if not chars:
                st.error("You have to check at least one character set")
            else:
                st.success("Password Generated Successfully!")
                st.header(gen_pass(chars, length))

                # 13
                st.balloons()

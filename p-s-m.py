import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Criteria Checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Increase password length to at least 8 characters.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟠 Include at least one lowercase letter.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🟡 Include at least one uppercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟢 Include at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔵 Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def get_strength_label(score):
    if score <= 2:
        return "🔴 Weak", "#ff4d4d"
    elif score <= 4:
        return "🟠 Moderate", "#ffa500"
    else:
        return "🟢 Strong", "#32cd32"

# Set Page Theme
st.markdown("""
    <style>
        body { background-color: #f4f4f4; }
        .stTextInput>div>div>input {
            background-color: #fff;
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Meter")
st.subheader("💡 Check Your Password's Strength Securely")

password = st.text_input("🔑 Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    strength_label, color = get_strength_label(score)
    
    st.markdown(f"### Password Strength: <span style='color:{color}; font-weight:bold;'>{strength_label}</span>", unsafe_allow_html=True)
    
    if score < 5:
        st.warning("🚀 Improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")
    else:
        st.success("🎉 Your password is strong!")

st.markdown("<h4 style='color:purple; text-align:center;'>🚀 Created with ❤️ by Ammara</h4>", unsafe_allow_html=True)

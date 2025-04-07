import re
import random
import string
import streamlit as st
import base64

# 🌟 Created by Ammara Dawood

# ❌ Common weak passwords to reject
blacklist = ['password123', '123456', 'qwerty', 'admin', 'letmein']

# 🎯 Function to evaluate password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        return 1, ["❌ This password is too common. Please choose a more secure one."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Your password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one uppercase letter (A-Z).")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one lowercase letter (a-z).")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one digit (0-9).")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one special character (!@#$%^&*).")

    return score, feedback

# 🔐 Generate a strong random password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# 🌄 Function to set background image
def set_background(image_file):
    try:
        with open(image_file, "rb") as image:
            encoded_image = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_image}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"Error: The file '{image_file}' was not found. Please check the file path.")

# 🌐 Streamlit GUI
def main():
    # Set background image
    set_background("image.png")  # Ensure the image file is in the correct directory

    st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
    st.markdown("✅ <i>Created by Ammara Dawood</i>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2889/2889676.png", width=100)

    password = st.text_input("🔑 Enter your password:", type="password")

    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔍 Password Analysis")
        if score <= 2:
            st.error("🔴 Strength: Weak ❌")
            for tip in feedback:
                st.warning(tip)
        elif score <= 4:
            st.warning("🟡 Strength: Moderate ⚠️")
            for tip in feedback:
                st.info(tip)
        else:
            st.success("🟢 Strength: Strong ✅ Great job!")

    if st.button("🎲 Generate a Strong Password"):
        new_password = generate_strong_password()
        st.text_input("🔐 Your Strong Password:", value=new_password)

    # ✅ Watermark at the very end
    st.markdown(
        "<hr style='margin-top: 40px;'>"
        "<p style='text-align: center; font-size: 14px; color: #00FFFF;'>"
        "🔧 This app was created by <b>Ammara Dawood</b>"
        "</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()





# import re
# import random
# import string
# import streamlit as st
# import base64

# # 🌟 Created by Ammara Dawood

# # ❌ Common weak passwords to reject
# blacklist = ['password123', '123456', 'qwerty', 'admin', 'letmein']

# # 🎯 Function to evaluate password strength
# def check_password_strength(password):
#     score = 0
#     feedback = []

#     if password.lower() in blacklist:
#         return 1, ["❌ This password is too common. Please choose a more secure one."]

#     if len(password) >= 8:
#         score += 1
#     else:
#         feedback.append("🔸 Your password should be at least 8 characters long.")

#     if re.search(r'[A-Z]', password):
#         score += 1
#     else:
#         feedback.append("🔸 Add at least one uppercase letter (A-Z).")

#     if re.search(r'[a-z]', password):
#         score += 1
#     else:
#         feedback.append("🔸 Add at least one lowercase letter (a-z).")

#     if re.search(r'\d', password):
#         score += 1
#     else:
#         feedback.append("🔸 Add at least one digit (0-9).")

#     if re.search(r'[!@#$%^&*]', password):
#         score += 1
#     else:
#         feedback.append("🔸 Add at least one special character (!@#$%^&*).")

#     return score, feedback

# # 🔐 Generate a strong random password
# def generate_strong_password(length=12):
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(length))

# # 🌄 Function to set background image
# def set_background(image_file):
#     try:
#         with open(image_file, "rb") as image:
#             encoded_image = base64.b64encode(image.read()).decode()
#         st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background-image: url("data:image/png;base64,{encoded_image}");
#                 background-size: cover;
#                 background-position: center;
#                 background-attachment: fixed;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
#     except FileNotFoundError:
#         st.error(f"Error: The file '{image_file}' was not found. Please check the file path.")

# # 🌐 Streamlit GUI
# def main():
#     # Set background image
#     set_background("image.png")  # Ensure the image file is in the correct directory

#     # Apply custom CSS for text colors to match the theme
#     st.markdown(
#         """
#         <style>
#         h1, h2, h3, p, label {
#             color: #E0FFFF !important;  /* Light cyan for headers and labels */
#         }
#         .stTextInput > div > div > input {
#             color: #FFFFFF !important;  /* White text for input fields */
#             background-color: rgba(0, 0, 0, 0.5) !important;  /* Semi-transparent black background for input */
#         }
#         .stButton > button {
#             background-color: #00B7EB !important;  /* Electric blue for buttons */
#             color: #FFFFFF !important;  /* White text for buttons */
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
#     st.markdown("✅ <i>Created by Ammara Dawood</i>", unsafe_allow_html=True)
#     st.image("https://cdn-icons-png.flaticon.com/512/2889/2889676.png", width=100)

#     password = st.text_input("🔑 Enter your password:", type="password")

#     if password:
#         score, feedback = check_password_strength(password)

#         st.subheader("🔍 Password Analysis")
#         if score <= 2:
#             st.error("🔴 Strength: Weak ❌")
#             for tip in feedback:
#                 st.warning(tip)
#         elif score <= 4:
#             st.warning("🟡 Strength: Moderate ⚠️")
#             for tip in feedback:
#                 st.info(tip)
#         else:
#             st.success("🟢 Strength: Strong ✅ Great job!")

#     if st.button("🎲 Generate a Strong Password"):
#         new_password = generate_strong_password()
#         st.text_input("🔐 Your Strong Password:", value=new_password)

#     # ✅ Watermark at the very end with the same cyan color
#     st.markdown(
#         "<hr style='margin-top: 40px;'>"
#         "<p style='text-align: center; font-size: 14px; color: #00FFFF;'>"
#         "🔧 This app was created by <b>Ammara Dawood</b>"
#         "</p>",
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()
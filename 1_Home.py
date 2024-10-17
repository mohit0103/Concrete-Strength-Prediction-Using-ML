import streamlit as st

st.set_page_config(
    page_title = "Concrete Strength Prediction"
)

st.write("<h1 style='text-align: center;'>Concrete Strength Prediction using Machine Learning</h1>", unsafe_allow_html=True)

st.markdown("---")

st.write("<p style='text-align: center; font-size: 20px; font-style: italic;'>Estimate concrete strength quickly and accurately by using the power of machine learning and data science.</p>", unsafe_allow_html=True)

image = "https://t4.ftcdn.net/jpg/02/01/96/59/240_F_201965916_Sywvqm6bcX9Mv9lo10gHlBlaBpkLti1B.jpg"
st.markdown(f"<div style='text-align: center;'><img src='{image}' style='width: 60%;'></div>", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

st.write("<h1 style='text-align: center;'>Why us?</h1>", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Image 1 and text 1
with col1:
    st.image("https://as2.ftcdn.net/v2/jpg/04/20/69/83/1000_F_420698353_jD43dbCS2exl7qs2vRpFzgPuz2VSWYV5.jpg", use_column_width=True)
    st.markdown("<h4><i>No more traditional waiting periods</i></h4>", unsafe_allow_html=True)

# Image 2 and text 2
with col2:
    st.image("https://as1.ftcdn.net/v2/jpg/03/46/88/50/1000_F_346885013_DH15ROsXEomPiKlnln2j1OJ1CYtumm9q.jpg", use_column_width=True)
    st.markdown("<h4><i>Facilitate quicker Decision-making</i></h4>", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)


col3, col4 = st.columns(2)

# Image 1 and text 1
with col3:
    st.image("https://www.giatecscientific.com/wp-content/uploads/2020/07/ConcreteCubeTest-1024x575.png", use_column_width=True)
    st.markdown("<h4><i>Save resource cost</i></h4>", unsafe_allow_html=True)

# Image 2 and text 2
with col4:
    st.image("https://as1.ftcdn.net/v2/jpg/07/14/76/20/1000_F_714762077_b6WToArp70yM8iJSvz6SfEpe417tNvLM.jpg", use_column_width=True)
    st.markdown("<h4><i>Accurate and Precise results</i></h4>", unsafe_allow_html=True)









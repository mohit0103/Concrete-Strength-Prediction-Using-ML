import streamlit as st
import base64
import os

st.write("<h1 style='text-align: center;'>About Us</h1>", unsafe_allow_html=True)
st.divider()
st.write("<h3 style='text-align: center;'>MEET THE TEAM!</h3>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

developer1 = st.container()
with developer1:
    column1, column2 = st.columns(2)
    with column1:
        st.image("images/dev2.png", use_column_width = True)
    with column2:
        st.markdown("#### Mohit Bhaisare")
        st.markdown("##### Data Science Engineer")
        st.markdown('''
                    ###### Responsibilities:
                    - Design and implement the Streamlit web application.
                    - Develop and train the Random forest regression model.
                    - Optimize model performance and conduct experiments.
                    ''')
        st.markdown(''' <a href = "https://www.linkedin.com/in/mohit-bhaisare-a56933182"><img src = "data:image/png;base64, {}"> </a> '''.format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()), unsafe_allow_html = True)
        st.divider()

developer2 = st.container()
with developer2:
    column1, column2 = st.columns(2)
    with column2:
        st.image("images/dev1.png", use_column_width = True)
    with column1:
        st.markdown("#### Azad Gunjal")
        st.markdown("##### Machine Learning Engineer")
        st.markdown('''
                    ###### Responsibilities:
                    - Develop and train the Random forest regression model.
                    - Integrate the ML model with the web app for concrete strength prediction.
                    ''')
        st.markdown(''' <a href = "https://www.linkedin.com/in/azad-gunjal/">
                        <img src = "data:image/png;base64, {}"> </a>
                    '''.format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()), unsafe_allow_html = True)
        st.divider()

developer3 = st.container()
with developer3:
    column1, column2 = st.columns(2)
    with column1:
        st.image("images/dev3.jpg", use_column_width = True)
    with column2:
        st.markdown("#### Samarth Khilare")
        st.markdown("##### Software Development Engineer")
        st.markdown('''
                    ###### Responsibilities:
                    - Hyperparameter tuning and model optimization.
                    - Review and edit the implemented web application.
                    ''')
        st.markdown(''' <a href = "https://www.linkedin.com/in/samarth-khilare">
                        <img src = "data:image/png;base64, {}"> </a>
                    '''.format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()),unsafe_allow_html = True)
        st.divider()

# developer4 = st.container()
# with developer4:
#     column1, column2 = st.columns(2)
#     with column2:
#         st.image("images/dev2.png", use_column_width = True)
#     with column1:
#         st.markdown("#### Harsh Kalingan")
#         st.markdown("##### ")
#         st.markdown('''
#                     ###### Responsibilities:
#                     - 
#                     - 
#                     ''')
#         st.markdown(''' <a href = "https://www.linkedin.com/in/azad-gunjal/"><img src = "data:image/png;base64, {}"> </a> '''.format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()), unsafe_allow_html = True)
#         st.divider()
        
        
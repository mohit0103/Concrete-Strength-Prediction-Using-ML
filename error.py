import streamlit as st

def main():
    page = st.sidebar.selectbox("Navigation", ["Home", "Predictor"])

    if page == "Home":
        show_home()
    elif page == "Predictor":
        show_predictor()

def show_home():
    st.title("Home Page")
    st.write("This is the home page.")
    if st.button("Let's get started"):
        # Redirect to the Predictor page
        show_predictor()

def show_predictor():
    st.title("Predictor Page")
    st.write("This is the predictor page.")
    # Your Predictor code goes here

if __name__ == "__main__":
    main()

import streamlit as st 
import numpy as np
import pickle
import base64
# from streamlit.report_thread import get_report_ctx
# from streamlit.server.server import Server

# Loading the saved model
loaded_model = pickle.load(open('trainedModel.sav', 'rb'))

# Function for compressive strength prediction

def comp_strength(input_data):
    
    specific_features = np.array(input_data)
    specific_features = specific_features.reshape(1, -1)
    predicted_strength = loaded_model.predict(specific_features)

    # print(f"Predicted Concrete Strength: {predicted_strength[0]}")
    return predicted_strength


def main():
    
    # Title
    st.write("<h1 style='text-align: center;'>Concrete Strength Predictor</h1>", unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)
    
    # Input data from user
    Cement = st.number_input('Cement (kg/m3) : ')
    Blast_Furnace = st.number_input('Blast Furnace Slag (kg/m3) : ')
    Fly_Ash = st.number_input('Fly Ash (kg/m3) : ')
    Water = st.number_input('Water (kg/m3) : ')
    Superplasticizer = st.number_input('Superplasticizer (kg/m3) : ')
    Coarse_Aggregate = st.number_input('Coarse Aggregate (kg/m3) : ')
    Fine_Aggregate = st.number_input('Fine Aggregate (kg/m3) : ')
    Age = st.number_input('Age (in days) : ')
    
    # global var
    global strength
    strength = comp_strength([Cement, Blast_Furnace, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age])

    # Button for prediction
    if st.button('Calculate the Compressive Strength'):
        # strength = comp_strength([Cement, Blast_Furnace, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age])
        st.success(f'Compressive Strength of given Concrete Mixture is {strength[0].round(2)} MPa.')
        
        if strength >= 40:
            st.markdown("## It is a High Strength Concrete")
            st.write("High Compressive concrete is generally used in following applications: ")
            st.write("<br>", unsafe_allow_html=True)

            # create columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("https://st3.depositphotos.com/1008154/18504/i/600/depositphotos_185047652-stock-photo-view-dubai-downtown-skyline-sunset.jpg", use_column_width=True)
                st.markdown("<i>High-rise buildings</i>", unsafe_allow_html=True)
            with col2:
                st.image("https://st3.depositphotos.com/1350793/18440/i/600/depositphotos_184406452-stock-photo-aerial-view-of-a-highway.jpg", use_column_width=True)
                st.markdown("<i>Bridges & Infrastructures</i>", unsafe_allow_html=True)
            with col3:
                st.image("https://st.depositphotos.com/1927453/3374/i/600/depositphotos_33749387-stock-photo-nuclear-power-plant.jpg", use_column_width=True)
                st.markdown("<i>Nuclear power plants</i>", unsafe_allow_html=True)
            

            # Additional Information
            # if st.button('Know more about your mixture'):
            #     if 38 <= strength <= 42:
            #         st.markdown("Your concrete mixture is close to M40 Grade Concrete. M40 grade concrete has a characteristic compressive strength of 40 N/mm² at 28 days. Suitable for prestressed structures, dams, and heavy-duty industrial facilities.", unsafe_allow_html=True)
            #     elif 43 <= strength <= 47:
            #         st.markdown("Your concrete mixture is close to M45 Grade Concrete. M45 grade concrete has a characteristic compressive strength of 45 N/mm² at 28 days. Used in bridges, marine structures, and nuclear power plants for enhanced durability.")
            #     elif 48 <= strength <= 52:
            #         st.markdown("Your concrete mixture is close to M50 Grade Concrete. M50 grade concrete has a characteristic compressive strength of 50 N/mm² at 28 days. Ultra-high-strength mix for high-rise buildings, long-span bridges, and special infrastructure projects.")
            #     elif 53 <= strength:
            #         st.markdown("Concrete mixture having grades M55, M60, M65, M70, and Higher Grades represent ultra-high-strength concrete mixes with strengths ranging from 55 N/mm² to 70 N/mm² and beyond. Used in offshore platforms, tall towers, precast elements, and projects requiring exceptional strength and durability.")

             
        elif strength <= 20:
            st.markdown("## It is a Low Strength Concrete")
            st.write("Low Compressive concrete is generally used for following applications: ")
            st.write("<br>", unsafe_allow_html=True)
            # create columns
            col4, col5, col6 = st.columns(3)
            with col4:
                st.image("https://st2.depositphotos.com/1192060/7017/i/600/depositphotos_70171637-stock-photo-builder-putting-up-a-suspended.jpg", use_column_width=True)
                st.markdown("<i>Non-structural Elements</i>", unsafe_allow_html=True)
            with col5:
                st.image("https://st3.depositphotos.com/2454953/17367/i/600/depositphotos_173672326-stock-photo-construction-workers-laying-paving-stones.jpg", use_column_width=True)
                st.markdown("<i>Pavements & Footpath</i>", unsafe_allow_html=True)
            with col6:
                st.image("https://st2.depositphotos.com/1140262/5902/i/600/depositphotos_59022353-stock-photo-man-laying-thermal-insulation-layer.jpg", use_column_width=True)
                st.markdown("<i>Thermal insulation</i>", unsafe_allow_html=True)

        else:
            st.markdown("## It is a Moderate Strength Concrete")
            st.write("Moderate Compressive concrete is generally used for following applications: ")
            st.write("<br>", unsafe_allow_html=True)
            #  Create columns
            col7, col8, col9 = st.columns(3)
            with col7:
                st.image("https://st.depositphotos.com/1987395/3285/i/600/depositphotos_32856403-stock-photo-big-modern-house.jpg", use_column_width=True)
                st.markdown("<i>General construction</i>", unsafe_allow_html=True)
            with col8:
                st.image("https://st4.depositphotos.com/36580916/37956/i/600/depositphotos_379563140-stock-photo-new-settlement-vienna-seestadt-aspern.jpg", use_column_width=True)
                st.markdown("<i>Residential buildings</i>", unsafe_allow_html=True)
            with col9:
                st.image("https://st.depositphotos.com/1001925/2541/i/600/depositphotos_25414503-stock-photo-underside-wide-angled-and-perspective.jpg", use_column_width=True)
                st.markdown("<i>Industrial floors</i>", unsafe_allow_html=True)
    
    # # Additional Information
    # if st.button('Know more about your mixture'):
    #     if 38 <= strength <= 42:
    #         st.markdown("Your concrete mixture is close to M40 Grade Concrete. M40 grade concrete has a characteristic compressive strength of 40 N/mm² at 28 days. Suitable for prestressed structures, dams, and heavy-duty industrial facilities.", unsafe_allow_html=True)
    #     elif 43 <= strength <= 47:
    #         st.markdown("Your concrete mixture is close to M45 Grade Concrete. M45 grade concrete has a characteristic compressive strength of 45 N/mm² at 28 days. Used in bridges, marine structures, and nuclear power plants for enhanced durability.")
    #     elif 48 <= strength <= 52:
    #         st.markdown("Your concrete mixture is close to M50 Grade Concrete. M50 grade concrete has a characteristic compressive strength of 50 N/mm² at 28 days. Ultra-high-strength mix for high-rise buildings, long-span bridges, and special infrastructure projects.")
    #     elif 53 <= strength:
    #         st.markdown("Concrete mixture having grades M55, M60, M65, M70, and Higher Grades represent ultra-high-strength concrete mixes with strengths ranging from 55 N/mm² to 70 N/mm² and beyond. Used in offshore platforms, tall towers, precast elements, and projects requiring exceptional strength and durability.")
    

                      

if __name__ == '__main__':
    main()

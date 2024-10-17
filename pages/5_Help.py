import streamlit as st

st.set_page_config(
    page_title = "Help"
)

st.write("<h1 style='text-align: center;'>Help</h1>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("#### Frequently Asked Questions")

st.markdown("Q1. What is the significance of cement in predicting the compressive strength of concrete?")
st.markdown("Cement is the binder in concrete and plays a crucial role in determining its strength. Higher cement content generally leads to higher compressive strength, but excessive cement can also cause issues like shrinkage and cracking.")

st.markdown("Q2. What is Blast Furnace Slag?")
st.markdown("Blast furnace slag is a byproduct of iron production and is often used as a supplementary cementitious material. It can improve the strength and durability of concrete when used in appropriate proportions.")

st.markdown("Q3. Why is Fly Ash used in concrete?")
st.markdown("Fly ash is another supplementary cementitious material that can improve concrete strength and durability. It reacts with calcium hydroxide in the presence of moisture to form additional cementitious compounds.")

st.markdown("Q4. What amount of water should be used in concrete to obtain good strength mixture?")
st.markdown("The water-cement ratio is critical in determining concrete strength. A lower water-cement ratio generally results in higher strength, as it leads to better hydration of cement particles. However, too low a ratio can make the concrete difficult to work with.")

st.markdown("Q5. Why are Superplasticizers used in Concrete mixture?")
st.markdown("Superplasticizers are used to improve the workability of concrete without increasing the water content. They can help achieve higher strength by allowing for a lower water-cement ratio.")

st.markdown("Q6. What is the significance of Coarse and Fine aggregate in preparation of concrete mixtures and how can they affect it's Compressive Strength?")
st.markdown("The type and quality of coarse aggregate can affect concrete strength. Well-graded, strong aggregates can improve strength, while weak or poorly graded aggregates can reduce it.")
st.markdown("Like coarse aggregate, fine aggregate (sand) quality and grading can impact concrete strength. Properly graded sand can improve the strength and workability of concrete.")

st.markdown("Q7. Why does the age of mixture matter when predicting or calculating the concrete strength?")
st.markdown("Concrete strength typically increases with age as hydration of cement continues. However, the rate of strength gain depends on various factors, including curing conditions and the type of cement used.")



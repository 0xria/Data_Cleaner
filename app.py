import streamlit as st
from recommend_engine import recommend_hotels

#UI/UX with Streamlit
st.set_page_config(page_title="Hotel Booking Recommendation Model", page_icon="🏨")
st.title("🏨 Hotel Booking Recommendation Model")
st.markdown("---")

#sidebar
with st.sidebar:
    st.header("Choice")
    h_type = st.selectbox("Hotel Type", ["City Hotel", "Resort Hotel"])
    guests = st.number_input("Total Guests", min_value=1, max_value=20, value=2)
    
if st.button("Create Recommendation"):
    with st.spinner('Analyzing historical booking patterns...'):
        data = recommend_hotels(h_type, guests)

        st.subheader("Top Recommended Stay Period")
        st.dataframe(data, use_container_width=True)

        st.success("Analysis Completed!")
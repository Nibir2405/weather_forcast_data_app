import streamlit as st
import plotly.express as px
from backend import get_data

#Add title, text input, slider and subheader

st.header("Weather Forcast For The Next Days")
place = st.text_input("Place:")

days = st.slider("Forcast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted day")
option = st.selectbox("Select data to view",("Temperature","Sky"))

try:
    if place:
        st.subheader(f"{option} for the next {days} days in {place}")
        #Get the temperature/sky data
        filtered_data = get_data(place=place, forcast_days=days)
        #Create temperature plot
        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y= temperature, labels={"x":"Date", "y":"Temperature(C)"})
            st.plotly_chart(figure)

        #Create Sky Plot
        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=105)
except KeyError:
    st.warning("That place doesn't exist")
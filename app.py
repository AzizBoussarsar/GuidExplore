import folium
import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components


def main():
    # Create a map centered around Tunisia
    map_center = [34.0, 9.0]
    m = folium.Map(location=map_center, zoom_start=7)
    # Add a title to your Streamlit app
    st.title("Explore Tunisia: Local Tourism Promotion")

    # Load data about attractions (replace with your own data)
    attractions_data = load_attractions_data()

    # Add markers to the map
    for idx, location in enumerate(attractions_data):
        folium.Marker(
            location=[location["latitude"], location["longitude"]],
            popup=location["description"],
            tooltip=location["name"],
            ).add_to(m)

    st.markdown("## Carte avec des emplacements épinglés")
    folium_static(m)
    # Display attractions information
    display_attractions(attractions_data)
    st.title("Virtual Tour with Google Maps")

    # Define the locations and their corresponding coordinates
    locations = [
        {"name": "Location 1", "latitude": 34.123, "longitude": 9.456},
        {"name": "Location 2", "latitude": 34.789, "longitude": 9.012},
        {"name": "Location 3", "latitude": 34.567, "longitude": 9.321},
    ]

    # Create a sidebar with location selection
    selected_location = st.sidebar.selectbox("Select a location", [location["name"] for location in locations])

    # Find the selected location and display the Google Maps component
    for location in locations:
        if location["name"] == selected_location:
            google_map_html = create_google_map(location["latitude"], location["longitude"])
            components.html(google_map_html, height=500)
            break


def load_attractions_data():
    # Load your attraction data from a file or database
    # Replace this with your own data loading code
    attractions_data = [
        {"name": "Site A", "latitude": 34.123, "longitude": 9.456, "description": "Description du site A.",
         "image": "images/jem.jpg"},
        {"name": "Site B", "latitude": 34.789, "longitude": 9.012, "description": "Description du site B.",
         "image": "images/jem.jpg"},
        {"name": "Site C", "latitude": 34.567, "longitude": 9.321, "description": "Description du site C.",
         "image": "images/jem.jpg"}
    ]
    # Add more attractions
    return attractions_data


def display_attractions(attractions_data):
    st.sidebar.title("Descriptions des sites")
    selected_location = st.sidebar.selectbox("Sélectionnez un site", [location["name"] for location in attractions_data])

    # Find the selected location and display its description
    for attraction in attractions_data:
        if attraction["name"] == selected_location:
            st.sidebar.subheader(attraction["name"])
            st.sidebar.image(attraction["image"])
            st.sidebar.write(attraction["description"])

            # Get the selected marker's popup information
            selected_marker = attraction
            selected_marker_description = selected_marker["description"]
            selected_marker_name = selected_marker["name"]

            # Update the sidebar content based on the selected marker
            if selected_marker_description is not None:
                st.sidebar.subheader(selected_marker_name)
                st.sidebar.write(selected_marker_description)
                

def create_google_map(latitude, longitude):
    google_map_html = """
        <iframe
            width="100%"
            height="100%"
            frameborder="0"
            scrolling="no"
            marginheight="0"
            marginwidth="0"
            src="https://www.google.com/maps/embed/v1/view?key=YOUR_API_KEY&center={lat},{lon}&zoom=15"
        ></iframe>
    """.format(lat=latitude, lon=longitude)

    return google_map_html

if __name__ == "__main__":
    main()
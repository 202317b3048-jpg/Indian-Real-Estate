import streamlit as st

# ---------- SESSION STATE INITIALIZATION ----------
def init_session_state():
    if "view" not in st.session_state:
        st.session_state.view = "india"

    if "selected_state" not in st.session_state:
        st.session_state.selected_state = None

    if "selected_city" not in st.session_state:
        st.session_state.selected_city = None


# ---------- NAVIGATION HANDLER ----------
def manage_navigation(state_df, city_df):
    init_session_state()

    # Navigation header
    st.sidebar.title("🧭 Dashboard Navigation")

    # Back button logic
    if st.session_state.view != "india":
        if st.sidebar.button("⬅ Back"):
            if st.session_state.view == "city":
                st.session_state.view = "state"
                st.session_state.selected_city = None
            elif st.session_state.view == "state":
                st.session_state.view = "india"
                st.session_state.selected_state = None

    # Page routing
    if st.session_state.view == "india":
        show_india_view(state_df)

    elif st.session_state.view == "state":
        show_state_view(state_df, city_df)

    elif st.session_state.view == "city":
        show_city_view(city_df)
        show_state_city_comparison(state_df, city_df)


# ---------- STATE CHANGE HELPERS ----------
def go_to_state_view(selected_state):
    st.session_state.selected_state = selected_state
    st.session_state.view = "state"


def go_to_city_view(selected_city):
    st.session_state.selected_city = selected_city
    st.session_state.view = "city"

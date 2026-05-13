import streamlit as st
import pickle
import pandas as pd
import requests

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

header {
    background: rgba(0,0,0,0);
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

.block-container {
    padding-bottom: 1rem !important;
}

section.main > div {
    padding-bottom: 0rem !important;
}

/* Main Background */
.stApp {
    background: linear-gradient(to bottom right, #000000, #0f172a);
    color: white;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 70px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
    animation: fadeIn 1.5s ease-in;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 40px;
}

/* Movie title */
.movie-title {
    text-align: center !important;

    color: white !important;

    font-size: 24px !important;

    font-weight: 700 !important;

    margin-top: 18px !important;

    margin-bottom: 45px !important;

    line-height: 1.5 !important;

    padding: 0px 10px !important;

    min-height: 80px !important;
}

/* Recommendation Button */
div.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px rgba(255, 81, 47, 0.7);
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
}

/* Fade Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.select-box {
    width: 95%;
    margin: auto;
}

.poster-container {
    overflow: hidden;
    border-radius: 20px;
}

.movie-poster {
    width: 100%;
    border-radius: 20px;

    transition: transform 0.4s ease,
                box-shadow 0.4s ease;
}

.movie-poster:hover {
    transform: scale(1.06);

    box-shadow:
        0px 0px 25px rgba(255, 75, 75, 0.6);

    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)

# ---------------- FETCH POSTER ---------------- #
def fetch_poster(movie_id):
    try:
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=c97c933150d5547fae997e27aae957fa&language=en-US'.format(movie_id)
        )

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# ---------------- RECOMMEND FUNCTION ---------------- #
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- LOAD DATA ---------------- #
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# ---------------- HEADER ---------------- #
st.markdown('<div class="main-title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)

st.markdown(
    '<div class=\"subtitle\">Discover movies similar to your favourites instantly ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;color:#ef4444;'>Unlimited Movie Discoveries 🍿</h3>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- MOVIE SELECT ---------------- #
st.markdown("<div class='select-box'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,4,1])

with col2:
    selected_movie_name = st.selectbox(
        'Choose Your Favourite Movie',
        movies['title'].values
    )
st.markdown("</div>", unsafe_allow_html=True)


# ---------------- RECOMMEND BUTTON ---------------- #
st.markdown("<div style='margin-top:50px;'></div>", unsafe_allow_html=True)

left, center, right = st.columns([5.5,1.8,5.5])

with center:
    recommend_clicked = st.button("Recommend")
st.markdown("<br><br>", unsafe_allow_html=True)

if recommend_clicked:

    st.markdown("""
        <script>
        window.scrollTo({
            top: 1000,
            behavior: 'smooth'
        });
        </script>
        """, unsafe_allow_html=True)

    with st.spinner('Finding awesome recommendations for you... 🍿'):

        names, posters = recommend(selected_movie_name)

    st.markdown("""
    <div style='margin-top:100px;'></div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style='text-align:center;
    color:white;
    margin-bottom:50px;
    font-size:42px;'>
    🍿 Recommended Movies
    </h2>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div class="poster-container">
                <img src="{posters[idx]}" class="movie-poster">
            </div>

            <p class="movie-title">{names[idx]}</p>
            """, unsafe_allow_html=True)
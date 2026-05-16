# 🎬 Movie Recommendation System

A Machine Learning based Movie Recommendation System built using **Python**, **Streamlit**, and **TMDB API** that recommends similar movies instantly with posters.

---

## 🚀 Live Demo

🔗 https://movie-recommendation-system-sam.streamlit.app/

---

## 📌 Features

- 🎥 Movie recommendation based on similarity
- 🖼️ Fetches movie posters using TMDB API
- ⚡ Fast and interactive Streamlit UI
- 🌙 Modern dark themed interface
- 📚 Machine Learning recommendation engine

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TMDB API
- Git & GitHub

---

## 📂 Project Structure

```bash
movie-recommendation-system/
│
├── main.py
├── requirements.txt
├── movie_dict.pkl
├── similarity.pkl
├── .gitignore
├── .gitattributes
└── README.md
```
---

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/Harshiya-Sameera/movie-recommendation-system.git
2️⃣ Move to Project Folder
cd movie-recommendation-system
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add TMDB API Key
Create folder:
.streamlit
Inside it create file:
secrets.toml
Add:
TMDB_API_KEY="your_api_key_here"
5️⃣ Run Project
streamlit run main.py

---

📖 How It Works

-This project uses a content-based recommendation system.
-Movies are converted into vectors
-Cosine similarity is calculated
-Similar movies are recommended based on similarity scores

---

👩‍💻 Author

Harshiya Sameera Shaik
GitHub: https://github.com/Harshiya-Sameera

---

⭐ If you liked this project
Give it a ⭐ on GitHub!

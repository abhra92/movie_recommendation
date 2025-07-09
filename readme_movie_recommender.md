# 🎬 Movie Recommendation System

A dual-approach movie recommendation system that combines content-based filtering and collaborative filtering to provide personalized movie suggestions.

## 🚀 Features

- **Content-Based Filtering**: Recommends movies based on title similarity using TF-IDF vectorization
- **Collaborative Filtering**: Suggests movies based on user preferences and ratings patterns
- **Interactive Web Interface**: Clean, modern Streamlit UI with real-time recommendations
- **Dual Recommendation Display**: Compare both approaches side-by-side
- **Dataset Statistics**: View comprehensive stats about movies and ratings

## 📊 Demo

![App Demo](screenshots/app_demo.png)

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download MovieLens Dataset:**
```bash
# Download from https://files.grouplens.org/datasets/movielens/ml-25m.zip
# Extract movies.csv and ratings.csv to the project directory
```

## 🎯 Usage

### Basic App (Content-Based Only)
```bash
streamlit run app.py
```

### Enhanced App (Both Methods)
```bash
streamlit run enhanced_app.py
```

### Jupyter Notebook
```bash
jupyter lab movie_recommendations.ipynb
```

## 📁 Data Requirements

The app expects these CSV files:

### Required:
- **movies.csv**: Contains `movieId`, `title`, `genres`

### Optional:
- **ratings.csv**: Contains `movieId`, `userId`, `rating` (enables collaborative filtering)

## 🔧 How It Works

### Content-Based Filtering
1. Cleans movie titles by removing special characters
2. Creates TF-IDF vectors from cleaned titles
3. Calculates cosine similarity between input and all movies
4. Returns top N most similar movies

### Collaborative Filtering
1. Finds users who rated the input movie highly (>4 stars)
2. Identifies other movies these users liked
3. Calculates recommendation score based on preference overlap
4. Returns movies with highest recommendation scores

## 📈 Technical Details

- **Text Processing**: TF-IDF with n-gram range (1,2)
- **Similarity Metric**: Cosine similarity
- **Recommendation Score**: `(Similar User Preference) / (All User Preference)`
- **Threshold**: Movies must be liked by >10% of similar users

## 🎨 App Structure

```
movie-recommender/
├── app.py                    # Basic Streamlit app
├── enhanced_app.py          # Advanced dual-method app
├── movie_recommendations.ipynb  # Jupyter notebook with analysis
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔄 API Usage

The `DualMovieRecommender` class can be used programmatically:

```python
from enhanced_app import DualMovieRecommender

# Initialize recommender
recommender = DualMovieRecommender()

# Content-based recommendations
content_recs = recommender.content_based_search("Toy Story", n_results=5)

# Collaborative filtering
movie_id = 1  # Toy Story
collab_recs = recommender.collaborative_filtering(movie_id)
```

## 📊 Dataset Information

This project uses the [MovieLens](https://grouplens.org/datasets/movielens/) dataset:
- **25M Dataset**: 25 million ratings from 162,000 users on 62,000 movies
- **Movies**: Title, genres, release year
- **Ratings**: User ratings on 1-5 scale

## 🚧 Future Enhancements

- [ ] Add movie posters and descriptions
- [ ] Implement matrix factorization (SVD/NMF)
- [ ] Add user profile creation
- [ ] Include movie metadata (cast, director, etc.)
- [ ] Add genre-based filtering
- [ ] Implement deep learning models
- [ ] Add API endpoints for mobile apps

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MovieLens](https://grouplens.org/datasets/movielens/) for providing the dataset
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [scikit-learn](https://scikit-learn.org/) for machine learning tools

## 📧 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/movie-recommender](https://github.com/yourusername/movie-recommender)

---

⭐ **Star this repository if you found it helpful!**
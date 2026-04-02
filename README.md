# House Price Prediction App

An interactive web application that uses **Machine Learning** to estimate the price of a house based on user-provided features. Users can fill out a simple form with details about their house plan (such as location, size, number of rooms, amenities, etc.) and instantly receive a predicted housing price.

This was a **collaborative group project** developed as part of our Machine Learning and Web Development learning journey.

## ✨ Features

- **User-friendly Interface**: Clean and intuitive form built with Streamlit
- **Real-time Prediction**: Get an estimated house price instantly as you adjust inputs
- **Machine Learning Powered**: Trained regression model (e.g., Random Forest, XGBoost, or Linear Regression)
- **Input Validation**: Handles various house attributes intelligently
- **Responsive Design**: Works well on both desktop and mobile

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — For building the interactive web app
- **Scikit-learn** / **XGBoost** / **Pandas** / **NumPy** — Machine Learning and data processing
- **HTML/CSS** — Custom styling and layout enhancements
- **Git & GitHub** — Version control and collaboration

## 📊 Project Workflow

1. **Data Collection & Exploration** — Analyzed the trained dataset
2. **Data Preprocessing** — Handled missing values, feature engineering, and encoding
3. **Model Training** — Built and evaluated multiple regression models
4. **Model Deployment** — Saved the best-performing model and integrated it into Streamlit
5. **Frontend Development** — Created an easy-to-use input form with beautiful UI

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8 or higher
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Motaluko/ml-group.git
   cd house-price-prediction

Create and activate a virtual environment (recommended)Bashpython -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
Install dependencies: Bash pip install -r requirements.txt
Run the Streamlit app: Bash streamlit run app.py

The app will open automatically in your browser.
📁 Project Structure
texthouse-price-prediction/
├── app.py                  # Main Streamlit application
├── house_price_model.pkl               # Trained machine learning model
├── requirements.txt        # Python dependencies
├── data/                   # Dataset used for training (if included)
├── notebooks/              # Jupyter notebooks for EDA and modeling
├── utils.py                # Helper functions (optional)
├── README.md
└── .gitignore

👥 Team Members
Motunrayo
Timilehin
Jessica
Paul
Bade
Adeoba
Israel
Augustine

We successfully collaborated using Git for version control, ensuring smooth teamwork and code integration.
🎯 Future Improvements

Add feature importance visualization
Include price confidence interval
Deploy to Streamlit Community Cloud / Heroku / AWS
Add multiple model comparison
User authentication and history of predictions

📄 License
This project is open for learning. Feel free to explore the code!

Built with ❤️ by the team using Python, Machine Learning & Streamlit

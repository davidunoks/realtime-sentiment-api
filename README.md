# 🚀 Real-Time Tweet Sentiment Analysis API

This is an end-to-end Machine Learning project that demonstrates the skills required for an ML Engineer role. The system fetches live tweets based on a search term, performs sentiment analysis using a Hugging Face Transformer model, and serves the results via a REST API built with FastAPI.

## Project Status: In Progress

* [x] **Phase 0: Foundation** - Project setup, virtual environment, and Git repository.
* [x] **Phase 1: Data Acquisition** - Connected to the X (Twitter) API v2.
* [x] **Phase 2: ML Model** - Integrated a pre-trained Hugging Face Transformer model (`roberta-base-sentiment`) for sentiment analysis.
* [ ] **Phase 3: API Development** - Building API endpoints with FastAPI.
* [ ] **Phase 4: Containerization** - Packaging the app with Docker.
* [ ] **Phase 5: Deployment** - Deploying to a public cloud service.

---

## ## Tech Stack

* **Python 3.10+**
* **Virtual Environment:** `venv`
* **ML/NLP:** Hugging Face `transformers` (using `cardiffnlp/twitter-roberta-base-sentiment-latest`)
* **ML Framework:** `torch` (PyTorch)
* **API Framework:** FastAPI
* **Data Source:** `tweepy` for X (Twitter) API v2
* **Credentials:** `python-dotenv` for secret management
* **Containerization:** Docker
* **Deployment:** (TBD, e.g., Google Cloud Run or AWS)

---

## ## How to Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/realtime-sentiment-api.git
    cd realtime-sentiment-api
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Mac/Linux
    # .\venv\Scripts\activate    # On Windows
    ```

3.  **Set up your environment variables:**
    * This project requires an X (Twitter) API v2 **Bearer Token**.
    * Create a file named `.env` in the root of the project.
    * Add your key to this file. **This file is git-ignored and will not be uploaded.**
    ```
    TWITTER_BEARER_TOKEN="YOUR_SECRET_BEARER_TOKEN_GOES_HERE"
    ```

4.  **Install dependencies:**
    * With your virtual environment active, install all required libraries:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the script:**
    ```bash
    python main.py
    ```
# Realtime-sentiment-api
End-to-end ML project to analyze real-time tweet sentiment using Transformers, FastAPI, and Docker

# Real-Time Tweet Sentiment Analysis API

This is an end-to-end Machine Learning project that demonstrates the skills required for an ML Engineer role. The system fetches live tweets based on a search term, performs sentiment analysis using a Hugging Face Transformer model, and serves the results via a REST API built with FastAPI.

## Project Status: In Progress

* [x] **Phase 0: Foundation** - Project setup, virtual environment, and Git repository.
* [ ] **Phase 1: Data Acquisition** - Connecting to the X (Twitter) API.
* [ ] **Phase 2: ML Model** - Loading and testing the sentiment analysis model.
* [ ] **Phase 3: API Development** - Building API endpoints with FastAPI.
* [ ] **Phase 4: Containerization** - Packaging the app with Docker.
* [ ] **Phase 5: Deployment** - Deploying to a public cloud service.

---

## ## Tech Stack

* **Python 3.10+**
* **Virtual Environment:** `venv`
* **API Framework:** FastAPI
* **ML/NLP:** Hugging Face `transformers` (DistilBERT-base-uncased)
* **Data Source:** X (Twitter) API v2
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

3.  **Install dependencies:**
    *(This file will be created in a future step)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    *(Instructions TBD)*
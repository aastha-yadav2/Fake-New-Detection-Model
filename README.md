# 📰 Fake News Detection Model

This project is a machine learning-based system that detects fake news using Natural Language Processing (NLP) techniques. It classifies news articles as **Fake (1)** or **Real (0)** using a simple yet effective **Logistic Regression** model.

> 📍 **Google Colab Notebook:**  
> [Fake News Detection - Colab](https://colab.research.google.com/drive/1YJUUtC0WRhW0XMQaAiLgh9zC1SBhUFgb?usp=sharing)
🚀 **Live Demo:** [Click here to try the Fake News Detection App](https://fake-new-detection-model-fwvqcskvmpnswpsmoxqzxz.streamlit.app/)

---

## 📚 Dataset

The dataset is sourced from Kaggle:

🔗 [Fake and Real News Dataset – Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

It contains the following columns:
- `id`: Unique ID for the news article
- `title`: Title of the article
- `author`: Author of the article
- `text`: Full text of the news article
- `label`: Classification label  
  - `1`: Fake  
  - `0`: Real

---

## 🔧 Features

- Uploads dataset via Colab
- Handles missing values
- Preprocesses text (lowercasing, removing punctuation, etc.)
- Vectorizes news using **TF-IDF Vectorizer**
- Trains a **Logistic Regression model** for binary classification
- Evaluates using accuracy score, confusion matrix, and classification report

---

## 🤖 Model Used

We used **Logistic Regression**, which is:
- Simple to implement
- Fast to train
- Easy to interpret
- Well-suited for binary classification tasks like detecting fake vs. real news

---

## ⚙️ Technologies Used

- Python
- Google Colab
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Matplotlib / Seaborn (optional for visualization)

---
## 📄 Case Study Document

I have also created a **Word document** as a case study on the Fake News Detection Model.  
It includes detailed explanations of the dataset, preprocessing steps, model used, and evaluation results.

📘 You can find and read the document in this repository.
---
## 🚀 How to Use

1. **Open the Colab Notebook:**
   [Launch Notebook](https://colab.research.google.com/drive/1YJUUtC0WRhW0XMQaAiLgh9zC1SBhUFgb?usp=sharing)

2. **Upload the Dataset:**
   Download the dataset from [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news)  
   Upload it in the notebook:
   ```python
   from google.colab import files
   uploaded = files.upload()

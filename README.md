# 🎭 Shakespeare Paragraph Generator ✍️

This is a simple web application that generates Shakespeare-style text based on a given character count and temperature value using a trained LSTM model. The backend is deployed on Render, and the frontend is hosted using GitHub Pages.

---

## 📚 Project Overview

- 🔥 Users can input:
  - Number of characters to generate
  - Temperature value to control creativity (higher values = more randomness)

- 📡 The frontend sends a request to the backend API, which returns generated text using a trained LSTM model on Shakespeare’s works.

- 🌐 **Frontend** is deployed on **GitHub Pages**, and **backend API** is deployed via **Render**.

---

## 🚀 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Machine Learning:** TensorFlow / Keras LSTM
- **Deployment:** 
  - Backend → [Render](https://render.com)
  - Frontend → [GitHub Pages](https://pages.github.com)

---

## 📦 Folder Structure

shakespeare-gen/
├── app.py
├── train_model.py
├── textgenerator.keras
├── requirements.txt
├── frontend/
    └── home.html
    └── script.js
    └── style.css
    └── assets

---

## 🌐 API Endpoint

The frontend interacts with the following backend endpoint:

POST https://shakespeare-lkrt.onrender.com/generate


**Request body:**
```json
{
  "length": 500,
  "temperature": 0.5
}
```

**Response:**
```json
{
  "output": "Generated Shakespeare-style paragraph..."
}
```

## 📑 How It Works
User enters desired text length and temperature.

Clicks the Generate button.

JavaScript sends a POST request to the backend API.

Backend returns generated text.

Text is displayed on the frontend.

## 📌 License
This project is open-source and available under the MIT License.

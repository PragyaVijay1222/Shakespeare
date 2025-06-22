import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initializing Flask app
app = Flask(__name__)
CORS(app)

# Loading the text corpus
filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()
text = text[300000:800000]

# Creating character mappings
characters = sorted(set(text))
char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))
SEQ_LENGTH = 40

# Loading pre-trained model
model = tf.keras.models.load_model('textgenerator.keras')

# Sampling function
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-8) / temperature  # Added epsilon to avoid log(0)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# Text generation function
def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated = sentence

    for _ in range(length):
        x_pred = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_to_index[char]] = 1

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = index_to_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

    return generated

# Routing to handle generation requests
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        length = int(data.get("length", 500))
        temperature = float(data.get("temperature", 1.0))

        generated_text = generate_text(length, temperature)
        return jsonify({"output": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Runing the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

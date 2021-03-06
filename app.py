import spacy
from flask import Flask, jsonify, request

from settings import NER_PATH, APP_PORT, APP_HOST

nlp_loaded = spacy.load(NER_PATH)
app = Flask(__name__)


@app.route('/get_entities', methods=['POST'])
def get_entities():
    message = request.get_json()
    message_text = message["text"]
    doc = nlp_loaded(message_text)
    result = [(str(x), x.label_) for x in doc.ents]
    return jsonify(dict(result)), 200


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)

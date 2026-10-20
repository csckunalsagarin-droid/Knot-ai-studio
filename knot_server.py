import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# .env file se configuration load karein
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Yahan AI ka response generate ho raha hai
    ai_reply = f"Aapne kaha: '{user_message}'. Knot AI Studio taiyar hai!"
    
    return jsonify({'response': ai_reply})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('DEBUG', 'True').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
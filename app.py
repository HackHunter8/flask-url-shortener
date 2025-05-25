from flask import Flask, request, redirect
import string, random
import redis
import os 

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, db=0, decode_responses=True) 

def generate_short_id(num_of_chars: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

@app.route('/')
def home():
    return "Hello, David!"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        original_url = request.form.get('url') or request.json.get('url')
        if not original_url:
            return "Missing URL", 400
        short_id = generate_short_id(6)
        r.set(short_id, original_url)
        return f"Shortened URL: http://localhost:5001/{short_id}"
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/<short_id>')
def redirect_url(short_id):
    original_url = r.get(short_id)
    return redirect(original_url) if original_url else "Invalid URL", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 

from flask import Flask, request, redirect, jsonify
import redis
import hashlib

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400# Create a short code using MD5 hashing
    short_code = hashlib.md5(original_url.encode()).hexdigest()[:6]
    print(short_code)

    # Store the short code and original URL in Redis
    r.set(short_code, original_url)

    return jsonify({'short_url': f'http://localhost:5000/{short_code}'})

@app.route('/<short_code>')
def redirect_url(short_code):
    # Retrieve the original URL from Redis
    original_url = r.get(short_code)

    if original_url:
        # Redirect to the original URL
        return redirect(original_url.decode('utf-8'))
    else:
        return jsonify({'error': 'URL not found'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)

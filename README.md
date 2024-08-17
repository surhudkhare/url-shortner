# URL Shortener

A simple URL shortener application built with Flask and Redis. This project demonstrates how to create a basic URL shortening service using Python.

## Installation  

1. Clone the repository

    ```bash
    git clone https://github.com/yourusername/url_shortener.git
    cd url_shortener
    ```

2. Set up a virtual environment and activate it:

    ```bash
    conda create -n url_shortener python=3.8
    conda activate url_shortener
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

1. Shorten a URL
   - Endpoint: `POST /shorten`  
   - Body:  

     ```json
     {
       "url": "https://www.example.com"
     }
     ```

   - Response:

        ```json
        {
          "short_url": "http://localhost:5000/<short_code>"
        }
        ```

2. Redirect to Original URL:  
   - Endpoint: `GET /<short_code>`  
   - Response: Redirects to the original URL.

## License

MIT License

Copyright (c) 2024 Surhud Khare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

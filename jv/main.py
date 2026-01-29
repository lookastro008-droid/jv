from flask import Flask, render_template
import threading
import webview
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def run_flask():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    # Create images folder if not exists
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
        print("📁 Created static/images folder")
    
    # Start Flask in background thread
    server_thread = threading.Thread(target=run_flask, daemon=True)
    server_thread.start()
    
    # Create WebView window
    window = webview.create_window(
        'ജ്യോതിഷമഞ്ജരി',
        'http://127.0.0.1:5000',
        width=400,
        height=750,
        resizable=True,
        fullscreen=False,
        easy_drag=False
    )
    
    webview.start()

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Dışarıdan gelen PORT değişkenini kullanarak uygulamayı çalıştır
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)


# Bu kod, "hello world" çıktısı veren bir Python web uygulamasıdır.

# Import gerekli modüller
from flask import Flask, render_template

# Flask uygulamasını başlat
app = Flask(__name__)

# Ana rotayı tanımla
@app.route("/")
def index():
    return render_template("index.html")

# HTML şablonunu tanımla
@app.route("/index.html")
def index_html():
    return """
    <html>
        <head>
            <title>Hello World from Burak</title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """

# Uygulamayı çalıştır
if __name__ == "__main__":
    app.run(debug=True)


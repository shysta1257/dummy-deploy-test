from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>Dummy Deploy Test</title></head>
      <body style="font-family: sans-serif; text-align: center; margin-top: 100px;">
        <h1>It's live!</h1>
        <p>If you're seeing this on a real URL (not localhost), your deployment worked.</p>
        <p>I just found out how deployment actually works.</p>
        <p>This is a simple Flask app for testing deployments.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

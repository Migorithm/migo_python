from flask import Flask
import asyncio

app = Flask(__name__)

@app.route("/")
async def index():
    await asyncio.sleep(0.25)
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
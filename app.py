from flask import Flask, request, jsonify, render_template
from gradio_client import Client

app = Flask(__name__)

# Connect to the external chatbot API
client = Client("ballet-ux/Healthbot")

def generate_response(user_message):
    try:
        result = client.predict(
            message=user_message,
            system_message="You are a friendly Chatbot.",
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        return result
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "")
    response = generate_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)


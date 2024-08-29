from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient

app = Flask(__name__)

# Initialize Hugging Face Inference Client
client = InferenceClient(
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    token="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"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if user_message:
        # Predefined responses
        if user_message.lower() in ["who made you", "who is your owner", "who is your boss"]:
            reply = "I was created by Sikandar. How can I assist you today?"
        else:
            # Get response from Hugging Face API
            response = client.chat_completion(
                messages=[{"role": "user", "content": user_message}],
                max_tokens=500
            )
            reply = response.choices[0].message['content']
        return jsonify({"reply": reply})
    return jsonify({"reply": "Sorry, I couldn't understand your message."})

if __name__ == '__main__':
    app.run(debug=True)

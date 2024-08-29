from flask import Flask, request, jsonify
from huggingface_hub import InferenceClient

app = Flask(__name__)

# Initialize Hugging Face InferenceClient
client = InferenceClient(
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    token="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"
)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        response = client.chat_completion(
            messages=[{"role": "user", "content": user_message}],
            max_tokens=500,
            stream=True
        )
        result = "".join([msg.choices[0].delta.content for msg in response])
        
        # Handle special cases
        if user_message.lower() in ["who created you", "who is your owner", "who is your boss"]:
            result = "I was created by Sikandar, a dedicated developer."
        
        return jsonify({'response': result})
    return jsonify({'error': 'No message provided'})

if __name__ == '__main__':
    app.run(debug=True)

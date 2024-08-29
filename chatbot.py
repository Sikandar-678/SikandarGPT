import tkinter as tk
from tkinter import scrolledtext
from huggingface_hub import InferenceClient

# Initialize Hugging Face Inference Client
client = InferenceClient(
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    token="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"
)

def get_response(user_message):
    # Predefined responses
    if user_message.lower() in ["who made you", "who is your owner", "who is your boss"]:
        return "I was created by Sikandar. How can I assist you today?"

    # Get response from Hugging Face API
    response = client.chat_completion(
        messages=[{"role": "user", "content": user_message}],
        max_tokens=500
    )
    return response.choices[0].message['content']

def send_message():
    user_message = user_input.get()
    if user_message.strip():
        chat_display.insert(tk.END, f"You: {user_message}\n")
        response = get_response(user_message)
        chat_display.insert(tk.END, f"Bot: {response}\n")
        chat_display.yview(tk.END)
        user_input.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("SikandarGPT Chatbot")

# Create and configure widgets
header = tk.Label(root, text="SikandarGPT", font=("Times New Roman", 16), bg="#333", fg="white", padx=10, pady=5)
header.pack(fill=tk.X)

chat_display = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, height=20, width=60)
chat_display.pack(padx=10, pady=10)

user_input = tk.Entry(root, width=80)
user_input.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the application
root.mainloop()

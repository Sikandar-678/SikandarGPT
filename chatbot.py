from tkinter import Tk, Label, Button, Text, Scrollbar, END, Y, RIGHT, LEFT
import requests

def send_message():
    message = user_input.get("1.0", END).strip()
    if message:
        try:
            response = requests.post('http://127.0.0.1:5000/chat', json={'message': message})
            response_data = response.json()
            if 'response' in response_data:
                chat_box.insert(END, f"Bot: {response_data['response']}\n")
            else:
                chat_box.insert(END, "Bot: No response from server.\n")
        except Exception as e:
            chat_box.insert(END, f"Bot: Error: {str(e)}\n")
        user_input.delete("1.0", END)

# Create the main window
root = Tk()
root.title("Chatbot")

# Create and place widgets
chat_box = Text(root, wrap='word', height=20, width=50)
chat_box.pack(side=LEFT, fill=Y)

scrollbar = Scrollbar(root, command=chat_box.yview)
scrollbar.pack(side=RIGHT, fill=Y)
chat_box.config(yscrollcommand=scrollbar.set)

user_input = Text(root, wrap='word', height=2, width=50)
user_input.pack(side=LEFT, fill=Y)

send_button = Button(root, text="Send", command=send_message)
send_button.pack(side=LEFT)

root.mainloop()

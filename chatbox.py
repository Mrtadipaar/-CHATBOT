import tkinter as tk
from tkinter import scrolledtext
import re
def get_response(user_input):
    user_input = re.sub(r'[^\w\s]', '', user_input).lower()
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a program, so I don't have feelings, but thanks for asking! How are you?"
    elif re.search(r'\bwhat is your name\b', user_input):
        return "I'm a simple chatbot created to assist you. You can call me Chatbot!"
    elif re.search(r'\bhelp\b|\bassist\b', user_input):
        return "Sure! What do you need help with?"
    elif re.search(r'\bbye\b|\bexit\b', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm having trouble understanding. Can you try explaining it differently?"

def send_message(event=None):
    user_input = user_entry.get()
    if user_input.lower() == "exit":
        window.quit()
    else:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
        response = get_response(user_input)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n\n", "chatbot")
        chat_log.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)
        chat_log.yview(tk.END)

window = tk.Tk()
window.title("Chatbot")
window.geometry("800x600")
window.configure(bg="#FFA500")

chat_log = scrolledtext.ScrolledText(window, state=tk.DISABLED, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 14))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


chat_log.tag_config("user", foreground="#1a73e8", font=("Arial", 14, "bold"))
chat_log.tag_config("chatbot", foreground="#34a853", font=("Arial", 14))

chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Chatbot: Hello!, How can I Help you Today?\n\n", "chatbot")
chat_log.config(state=tk.DISABLED)

user_entry = tk.Entry(window, font=("Arial", 16), bg="#FFFF00", fg="#000000")
user_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
user_entry.bind("<Return>", send_message)

send_button = tk.Button(window, text="Send", font=("Arial", 14, "bold"), command=send_message, bg="#4caf50", fg="#ffffff", activebackground="#45a049", activeforeground="#ffffff")
send_button.pack(padx=10, pady=(0, 10))

window.mainloop()

from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define chat patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you ?", ["I'm good, thank you!", "I'm doing well, thanks for asking."]],
    [r"what is your name ?", ["You can call me MRBot.", "I'm MRBot, nice to meet you!"]],
    [r"bye|goodbye", ["Bye! Have a good day.", "Bye! Take care."]],
    [r"who created you ?", ["I was created by Prajwal."]],
     [r"when were you created ?", ["I was created in the year 2024."]],
    [r"(.*)", ["Let me search that for you."]]
]

# Store chat history
chat_history = []

# Creating the Chatbot Instance
mr_bot = Chat(pairs, reflections)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    chat_history.append(user_input)
    response = mr_bot.respond(user_input)
    if response == "Let me search that for you.":
        chatgpt_url = f"https://chat.openai.com/chat?q={user_input}"
        return jsonify({"redirect": chatgpt_url, "top_result": f"Top result from ChatGPT: {chatgpt_url}"})
    chat_history.append(response)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
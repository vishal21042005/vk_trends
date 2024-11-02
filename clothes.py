from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route("/product.html")
def product():
    # Render the template that contains both "Hello World" and chatbot
    return render_template("product.html")


# Simple chatbot logic
def get_bot_response(user_input):
    response = {
        "hello": "Hello! How can I help you?",
        "how are you?": "I'm a bot, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "do you have dresses?": "Yes, we do",
        "what colors are available?": "we have red,blue,black, and more",
        "are there any discount?": "yes, up to 40% off",
    }
    return response.get(user_input.lower(), "I'm sorry, I didn't understand that.")

@app.route("/chat.html")
def chat():
    # Render the template that contains both "Hello World" and chatbot
    return render_template("chat.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("message")
    if not user_input:
        return jsonify({"response": "Please enter a message."})
    
    bot_response = get_bot_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True,port=5001)
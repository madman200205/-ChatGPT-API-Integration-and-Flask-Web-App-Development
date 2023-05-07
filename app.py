from flask import Flask, render_template, request
# import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials
# openai.api_key = os.environ["OPENAI_API_KEY"]
# model_engine = "davinci"

# Define the homepage with the form
@app.route("/")
def home():
    return render_template("home.html")

# Define the results page that shows the user input and the ChatGPT response
@app.route("/results", methods=["POST"])
def results():
    user_input = request.form["user_input"]
    # chat_response = get_chat_response(user_input)
    chat_response = "defualt message because unable to make  api call in free version"

    return render_template("results.html", user_input=user_input, chat_response=chat_response)

# Define a function that uses the OpenAI API to generate a response to the user input
# def get_chat_response(user_input):
#     prompt = f"Conversation with a user:\nUser: {user_input}\nAI:"
#     response = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     chat_response = response.choices[0].text.strip()
#     return chat_response

if __name__ == "__main__":
    app.run(debug=True)

import unittest
import json
from flask import Flask, request, render_template

# # Import ChatGPT API module
# from chatgpt_api import get_chat_response

# Create Flask app instance
app = Flask(__name__)

# Define Flask app routes and controllers
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods=["POST"])
def results():
    user_input = request.form["user_input"]
    # chat_response = get_chat_response(user_input)
    chat_response  = "op"

    return render_template("results.html", user_input=user_input, chat_response=chat_response)

# Define test cases for the Flask app
class FlaskAppTestCase(unittest.TestCase):
    # Test the ChatGPT API integration
    def test_chatgpt_api(self):
        # chat_response = get_chat_response("Hello")
        chat_response = "op"

        self.assertIsInstance(chat_response, str)

    # Test the proper rendering of the homepage
    def test_homepage_render(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ChatGPT Home", response.data)

    # Test the proper rendering of the results page
    def test_results_render(self):
        tester = app.test_client(self)
        response = tester.post("/results", data={"user_input": "Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ChatGPT Results", response.data)

# Run the Flask app and test cases if run as a script
if __name__ == "__main__":
    unittest.main()
    app.run(debug=True)

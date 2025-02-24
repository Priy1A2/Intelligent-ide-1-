from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import os

# Set up API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBvsCWfAhgNSPW8rQEu6187lwDbx7UGz8o"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt).text
    return render_template("index.html", response=response)

@app.route("/generate_code", methods=["POST"])
def generate_code():
    prompt = request.form["code_prompt"]
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Write Python code for: {prompt}")

    if response and response.text:
        return jsonify({"response": response.text})
    else:
        return jsonify({"response": "Error generating code"}), 500


if __name__ == "__main__":
    app.run(debug=True)



@app.route("/generate_tests", methods=["POST"])
def generate_tests():
    prompt = request.form["test_prompt"]
    response = genai.GenerativeModel("gemini-pro").generate_content(f"Generate unit tests for: {prompt}")
    return response.text


@app.route("/debug_code", methods=["POST"])
def debug_code():
    prompt = request.form["debug_prompt"]
    response = genai.GenerativeModel("gemini-pro").generate_content(f"Find and fix bugs in the following code:\n{prompt}")
    return response.text


@app.route("/cicd_pipeline", methods=["POST"])
def cicd_pipeline():
    prompt = request.form["cicd_prompt"]
    response = genai.GenerativeModel("gemini-pro").generate_content(f"Write a GitHub Actions workflow for: {prompt}")
    return response.text
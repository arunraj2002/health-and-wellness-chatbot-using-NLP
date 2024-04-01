from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template("base.html")
@app.route('/mental_health')
def mental_health():
    return render_template("mental health.html")

@app.route('/diet_plan')
def diet_plan():
    return render_template("diet plan.html")

@app.route('/fitness')
def fitness():
    return render_template("fitness.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)


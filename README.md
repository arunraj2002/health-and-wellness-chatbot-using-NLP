# Health-and-Wellness-Chatbot

This project is a chatbot application designed to provide personalized health and wellness recommendations based on user's input and preferences. It utilizes natural language processing (NLP) techniques to understand and respond to user queries.

## Features:
1. User Input Analysis: Processes user input using NLP to understand health-related queries and requests.
2. Personalized Recommendations: Provides personalized health and wellness recommendations based on user input, preferences, and historical data.
3. Interactive Conversations: Engages in interactive conversations with users to gather additional information and refine recommendations.
4. Integration with External APIs: Retrieves relevant health and wellness information from external APIs.

## Requirements:
1. Python 3.7
2. Python packages like nltk,flask.

## Architecture Diagram/Flow:

![image](https://github.com/Kayalvizhi02/health-and-wellness-chatbot/assets/75413726/08caafe9-95be-410c-81af-57a3161a9a03)

## Installation

1. Clone the repository:
```
    git clone https://github.com/Kayalvizhi02/health-and-wellness-chatbot.git
   
```
2. Install the required packages:
```
   pip install Flask torch torchvision nltk
```
3. Download and set up the required language models for NLP processing.

## Usage

1. Run the chatbot application:
```
    App.py
```
2. Access the chatbot through your preferred messaging platform or in your web browser

3. Engage in a conversation with the chatbot, asking about diet plans and fitness guidance.

4. The chatbot will analyze your input using NLP and provide personalized recommendations based on the information gathered.

5. Enjoy an interactive and informative conversation with the health and wellness chatbot.

## Program:

### App.py
```python

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

```

## Output:

![image](https://github.com/Kayalvizhi02/health-and-wellness-chatbot/assets/75413726/8c15cd56-12ea-40c2-b645-73907ebd985b)

![image](https://github.com/Kayalvizhi02/health-and-wellness-chatbot/assets/75413726/ef9a3b43-179f-42d6-ae2a-b12c1040e95e)

## Result:
Finally, the results of a Health and Wellness Chatbot using NLP are expected to revolutionize the way individuals engage with their health. The integration of personalized guidance, continuous learning, and user-friendly interactions positions the chatbot as a valuable tool for promoting a healthier and more informed lifestyle.

We can use this this chatbot for planning diet, health planning, fitness guidance and also mental health support.

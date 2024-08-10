"""
This module implements a Flask web application that performs emotion detection
on user-provided text. The application is deployed on localhost:5000.
"""

# Import necessary components from the Flask framework
from flask import Flask, render_template, request

# Import the emotion detection function from the custom EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Detect emotion from the provided text.

    Retrieves the text to analyze from the request arguments, passes it to the
    emotion_detector function, and returns the detected emotion as a formatted string.

    Returns:
        str: A formatted string with emotion detection results or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)

    # Check if the result is None, indicating an error or invalid input
    if result is None:
        return "Invalid input! Try again."

    # Return a formatted string with the emotion label and score
    return (f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}.")


@app.route("/")
def render_index_page():
    """
    Render the main application page.

    This function initiates the rendering of the main application page over the Flask channel.

    Returns:
        A rendered HTML template for the main application page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

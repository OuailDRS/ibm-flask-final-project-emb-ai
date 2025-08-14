"""
This is a Flask web application for emotion detection.

It provides a user interface to enter text and an API endpoint to analyze
the emotions within that text using the watsone embbedable AI library.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")
@app.route("/")
def render_index_page():
    """
    This function is triggered when a user navigates to the root URL ('/').
    It serves the 'index.html' file which contains the user interface
    for submitting text to be analyzed.

    Returns:
        A rendered HTML template (index.html).
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detection():
    """
    This function is an API endpoint that analyzes text for emotions. 
    It takes text from the interface web, uses an emotion_detector function, 
    and returns a string with the emotion scores or an error if the analysis fails.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyse)
    if emotion['dominant_emotion'] is None :
        return "Invalid text! Please try again!."
    result = (
    f"For the given statement, the system response is "
    f"'anger': {emotion['anger']}, 'disgust': {emotion['disgust']}, "
    f"'fear': {emotion['fear']}, 'joy': {emotion['joy']} and "
    f"'sadness': {emotion['sadness']}. The dominant emotion is "
    f"{emotion['dominant_emotion']}"
            )
    return result
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)

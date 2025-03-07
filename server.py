''' 
server.py for Emotion Detector app 
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def em_detector():
    '''
    Response app
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotions
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Please try again."

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    ''' render index '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

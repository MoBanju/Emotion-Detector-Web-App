''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detetctor")

@app.route('/emotionDetector')
def emo_detector():
    ''' This code receives the text from the HTML interface and 
    runs sentiment analysis over it using emotion_detector()
    function. The output returned shows the emotions score and the dominant 
    emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    scores = response
    if scores['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
    f"For the given statement, the system response is "
    f"'anger': {scores['anger']}, 'disgust': {scores['disgust']}, "
    f"'fear': {scores['fear']}, 'joy': {scores['joy']} and "
    f"'sadness': {scores['sadness']}. "
    f"The dominant emotion is {scores['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

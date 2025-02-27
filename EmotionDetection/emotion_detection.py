import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    '''Define a function named emotion_detector that takes a string input (text_to_analyse)
    '''

    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Format response
    formatted_response = json.loads(response.text)

    # Extract emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotions['anger'],
    disgust = emotions['disgust'],
    fear = emotions['fear'],
    joy = emotions['joy'],
    sadness = emotions['sadness'],

    #Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
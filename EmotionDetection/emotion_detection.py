import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input_json, headers = header)
    if response.status_code == 400 : 
        return {
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'sadness': None,
    'dominant_emotion':None
    }
    result = json.loads(response.text)
    anger_score = result["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = result["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = result["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = result["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = result["emotionPredictions"][0]["emotion"]["sadness"]
    emotion_score = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score
    }
    dominant_emotion = max(emotion_score, key=lambda x: emotion_score[x])
    emotion_score['dominant_emotion'] = dominant_emotion
    return emotion_score
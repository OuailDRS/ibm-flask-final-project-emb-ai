import unittest
from EmotionDetection.emotion_detection import emotion_detector
class mytest(unittest.TestCase):
    def testing_emotion_prediction(self):
        st1=emotion_detector("I am glad this happened")
        self.assertEqual(st1["dominant_emotion"],"joy")
        st2=emotion_detector("I am really mad about this")
        self.assertEqual(st2["dominant_emotion"],"anger")
        st3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(st3["dominant_emotion"],"disgust")
        st4=emotion_detector("I am so sad about this")
        self.assertEqual(st4["dominant_emotion"],"sadness")
        st5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(st5["dominant_emotion"],"fear")
unittest.main()
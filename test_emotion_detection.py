from EmotionDetection.emotion_detection import emotion_detector
import unittest

class EmotionTest(unittest.TestCase):
    def test_emotion(self):
        res1 = emotion_detector("I am glad this happened")
        max_emotion = max(res1, key = res1.get)
        self.assertEqual(max_emotion, "joy")        

        res1 = emotion_detector("I am really mad about this")
        max_emotion = max(res1, key = res1.get)
        self.assertEqual(max_emotion, "anger")

        res1 = emotion_detector("I feel disgusted just hearing about this")
        max_emotion = max(res1, key = res1.get)
        self.assertEqual(max_emotion, "disgust")

        res1 = emotion_detector("I am so sad about this")
        max_emotion = max(res1, key = res1.get)
        self.assertEqual(max_emotion, "sadness")

        res1 = emotion_detector("I am really afraid that this will happen")
        max_emotion = max(res1, key = res1.get)
        self.assertEqual(max_emotion, "fear")

unittest.main()
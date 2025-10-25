"""
This is server file
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("App")

@app.route("/emotionDetector")
def emotion_analyser():
    """
    emotionDetector function
    """
    text = request.args.get("textToAnalyze")
    res = emotion_detector(text)

    if res is None:
        final_result = "Invalid text! Please try again!."
    else:
        emotion = max(res, key = res.get)
        prefix = "For the given statement, the system response is "
        res = str(res).strip("{}")
        final_result = prefix + res + " The dominant emotion is " + emotion
    return final_result

@app.route("/")
def return_res():
    """
    default page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

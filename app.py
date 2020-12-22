from flask import Flask, jsonify
from memeGenerator import ScrapMemes

# Making a flask app
app = Flask(__name__)
# setting flask jsonify to not sort dictionary keys while returning as API
app.config['JSON_SORT_KEYS'] = False


# Random Meme Generator
@app.route('/')
def meme_api():
    result = ScrapMemes()
    return jsonify(result)

# Numbered Meme Generator
@app.route('/<int:num>/')
def meme_api_no(num):
    result = ScrapMemes(num=num)
    return jsonify(result)

# Topic wise Meme Generator
@app.route('/<string:topic>/')
def meme_api_topic(topic):
    result = ScrapMemes(topic=topic)
    return jsonify(result)

# Topicwise and numbered meme generator
@app.route('/<string:topic>/<int:num>/')
def meme_api_topic_and_no(topic, num):
    result = ScrapMemes(topic=topic, num=num)
    return jsonify(result)


if __name__ == "__main__":
    # running the flask app in threaded mode 
    # to allow handling more requests at once
    app.run(threaded=True)

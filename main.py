from flask import Flask, jsonify
from memeGenerator import ScrapMemes

app=Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def hello_world():
    return '404 Page Not Found'


@app.route('/meme_api/')
def meme_api():
    result=ScrapMemes()
    return jsonify(result)


@app.route('/meme_api/<int:num>/')
def meme_api_no(num):
    result=ScrapMemes(num=num)
    return jsonify(result)


@app.route('/meme_api/<string:topic>/')
def meme_api_no(topic):
    result=ScrapMemes(topic=topic)
    return jsonify(result)


@app.route('/meme_api/<string:topic>/<int:num>/')
def meme_api_topic_and_no(topic,num):
    result=ScrapMemes(topic=topic,num=num)
    return jsonify(result)

if __name__ == "__main__":
    app.run(threaded=True)
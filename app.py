from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints


@app.route('/', methods=["GET", "POST"])
def home_page():
    subtitle = ''
    if request.method == "POST":
        videoid = request.form.get('vid-id', '')
        script = YouTubeTranscriptApi.get_transcript(videoid)
        for segment in script:
            subtitle = subtitle + ' ' + segment['text']
        return render_template('index.html', post=subtitle)

    elif request.method == "GET":
        return render_template('index.html', post=subtitle)



# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)

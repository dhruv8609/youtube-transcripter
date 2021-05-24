from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)


model_path = './summarizer_model'


def return_summary(text):
    model = pipeline('summarization', model=model_path, tokenizer=model_path)
    length = len(text)
    summary = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 2000
        end = (i + 1) * 2000
        res = model(text[start:end])
        res = res[0]
        res = res['summary_text']
        summary.append(res)
    return summary


@app.route('/', methods=["GET", "POST"])
def home_page():
    subtitle = ''
    if request.method == "POST":
        videoid = request.form.get('vid-id', '')
        script = YouTubeTranscriptApi.get_transcript(videoid)
        for segment in script:
            subtitle = subtitle + ' ' + segment['text']
        vid_summary = return_summary(subtitle)
        return render_template('index.html', post=vid_summary)

    elif request.method == "GET":
        return render_template('index.html', post=subtitle)


if __name__ == '__main__':
    app.run(debug=True)

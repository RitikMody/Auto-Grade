from flask import Flask , render_template, redirect
import flask
import pandas as pd
from model import get_answers
import report

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def upload_file():
	uploaded_files = flask.request.files.getlist("file[]")
	for uploaded_file in uploaded_files:
		if uploaded_file.filename != '':
			uploaded_file.save(f"./User/{uploaded_file.filename}")

	answer_key = pd.read_csv("./User/answers-multipage.csv")
	answered = get_answers("./User/test-multipage.pdf")
	answer_key["student_answer"] = pd.Series(answered)
	print(answer_key.head(), answer_key.columns)
	return ""

@app.route('/results')
def results():
	correct, incorrect = report.calc_correct_responses()
	return render_template('report.html', correct = correct, incorrect = incorrect)

if __name__ == '__main__':
   app.run(debug=True)

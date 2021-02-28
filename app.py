from flask import Flask , render_template, redirect
import flask
import pandas as pd
import model
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

	df = pd.read_csv("./User/answers-multipage.csv")
	answered = model.get_answers("./User/test-multipage.pdf")
	df["student_answer"] = pd.Series(answered)
	print(df.head(), df.columns)
	# df = pd.read_csv("./Data/corrected_sheet.csv")
	num_total, num_correct, num_incorrect = report.calc_correct_responses(df)
	topic_scores = report.calc_score_for_topic(df)
	incorrect_question = report.incorrct_question(df).reset_index()
	return render_template('report.html', num_total = num_total, num_correct = num_correct, num_incorrect = num_incorrect, topic_scores = topic_scores,
							question = incorrect_question['question'], answer = incorrect_question['correct_answer'], length = incorrect_question.shape[0])

if __name__ == '__main__':
   app.run(debug=True)

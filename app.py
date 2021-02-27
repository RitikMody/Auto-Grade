from flask import Flask , render_template, redirect
import flask

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
	return ""

if __name__ == '__main__':
   app.run(debug=True)

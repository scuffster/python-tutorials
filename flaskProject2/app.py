from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def validate_url():
    if request.method == 'GET':
        return render_template('validate_url.html')
    else:
        void_uri_space = request.form['void_uri_space']
        if "https://pid.myco.net/rd/data/identifier" in void_uri_space:
            result = "Valid URL"
        else:
            result = "Invalid URL"
        return render_template('validate_url.html', result=result)

if __name__ == '__main__':
    app.run()

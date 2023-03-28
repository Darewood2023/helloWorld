from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Darien Ghee!'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite_course', methods=['GET'])
def favoritecourse():
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET','POST'])
def contact():

    if request.method == 'GET':
        return render_template('contact.html',form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()

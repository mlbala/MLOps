from flask import Flask, render_template, request

# Initilize Flask app
## It creates an instances of the Flask class,
## Which will be your WSGI (Web Server Gateway Interface) applicaitons.

app=Flask(__name__)
# app = Flask(__name__, template_folder="../templates")

@app.route("/")
def welcome():
    return "Welcome to the Flask Welcome page, this should be amazing."

@app.route("/index", methods=['GET'])
def Index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route('/form', methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['name']
#         return f"Hello {name}!"
#     return render_template('form.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form1.html')


if __name__=="__main__":
    #app.run()
    app.run(debug=True)
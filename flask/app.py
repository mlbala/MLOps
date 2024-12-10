from flask import Flask

# Initilize Flask app
## It creates an instances of the Flask class,
## Which will be your WSGI (Web Server Gateway Interface) applicaitons.

app=Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the Flask Welcome page, this should be amazing."

@app.route("/index")
def Index():
    return "welcome to index page"

if __name__=="__main__":
    #app.run()
    app.run(debug=True)
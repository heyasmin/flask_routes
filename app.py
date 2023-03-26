from flask import Flask, Response, request, url_for

# variable called app, to activate Flask basically
app = Flask(__name__)


# wrap the function with a declarator
@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/bye')
def bye_from_flask():
    return "Bye! See you soon."


# @app.route('/get/text')
# def get_text():
#     return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


# this particular route will only match if it has a post request
@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You sent this data: " + data_sent)


@app.route('/dynamic/<word>')  # <placeholder>
def dynamic_route_a(word):
    return "Echo " + word


@app.route('/square/<int:number>')
def square(number):
    squared_number = number ** 2  # shorthand for square
    message = "Your number squared is: " + str(squared_number)
    return message


# @app.route('/hello/<name>')
# def dynamic_name(name):
#     return "Hello " + name


# page 439 exercise
@app.route('/hello/<name>')
def say_hello_page(name):
    return """
    <html>
    <head>
        <title>Sample - Flask routes</title>
    </head>
    <body>
        <h1>Name page</h1>
        <p>Hello {}!</p>
    </body>
    </html>
    """.format(name)


# page 440 exercise
@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')

@app.route('/about')
def about():
    url = url_for('get_text')
    return """
    <html>
    <head>
        <title>About page - Flask routes</title>
    </head>
    <body>
        <h1>About page</h1>
        <p>Example about page.</p>
        <hr>
        <a href="{}">Welcome</a>       
    </body>
    </html>
    """.format(url)


@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    return """
<html>
<head>
        <title>Sample - Flask routes</title>
</head>
<body>
        <h1>Name page</h1>
        <p>Hello {}!</p>
        <p>You are {} year(s) old.</p> 
        <hr>
        <a href="{}">Welcome</a>         
</body>
</html>
""".format(name, age, url)






# this always stays at the bottom of the file!!
if __name__ == "__main__":
    app.run(debug=True)

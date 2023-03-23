from flask import Flask

### WSGI application

app=Flask(__name__)

### Decoroter ( to define binding function)
@app.route('/')
def welcome():
    return " Welcome to New Project..."


@app.route('/mem')
def mem():
    return "Recap many times."


if __name__=='__main__':
    app.run(debug=True)

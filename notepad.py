from bottle import Bottle, route, template

app = Bottle()

@app.route('/')
def hi():
    return ('<br>Hello, world!<br>')

@app.route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.route('/login', method='POST')
def do_login():
    username = request.forms.username
    password = request.forms.password
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
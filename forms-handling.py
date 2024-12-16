from bottle import route, request, run, get, post, template

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.username
    password = request.forms.password
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
def check_login(un, pwd):
    if (un == 'abcd' and pwd == "1234"):
        return 1
    else:
        return 0
    
run (host='localhost', port=8080)
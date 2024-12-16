from bottle import route, run, template

@route('/hello/<route_name>')
def index(route_name):
    print(route_name)
    return template('<br>Hello {{name}}</b>!', name=route_name)

run (host='localhost', port=8080)
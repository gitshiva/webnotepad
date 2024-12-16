from bottle import Bottle, run, template

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/hello/<route_name>')
def index (route_name):
    return template('<br>Hello, {{name}}!<br>', name=route_name)

@app.route('/')
@app.route('/hello2/')
@app.route('/hello2/<route_name>')
def greet (route_name='Stranger'):
    print(route_name)
    return template('Hello {{name}}, how are you?', name=route_name)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
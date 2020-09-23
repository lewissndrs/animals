from flask import Flask, render_template
app = Flask(__name__)

from controllers.animals_controller import animals_blueprint

app.register_blueprint(animals_blueprint)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
from . import app

@app.route('/')
def index():
    return "Toto je index."
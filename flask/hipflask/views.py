# note, the following is a circular import, the top-level __init__.py imports this file.
# This is needed here for the decorators to work but is generally a bad idea and you shouldn't take this example
# as justification for doing it elsewehere also. See (//http://flask.pocoo.org/docs/0.12/patterns/packages/)
from hipflask import app

@app.route('/')
def index():
    return('<em>hipflask</em> as a flask app!')

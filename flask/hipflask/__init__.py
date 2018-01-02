from flask import Flask

app = Flask(__name__)
app.debug = True

import hipflask.views

if __name__ == "__main__":
    app.run(host='0.0.0.0')

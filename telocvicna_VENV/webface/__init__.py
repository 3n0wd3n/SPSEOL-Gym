import flask

app = flask.Flask(__name__)
app.secret_key = b'u\x19\xbd\xa7\x06\xfe^\xfet[\xaaUC\xc4\xc2z\xe8\x87\xce\x10y`\x02\xc3'

from . import routes 
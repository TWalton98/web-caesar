from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method="post">
      <input value="0" type="text" id="" name="rot">
      <textarea name="text">{0}</textarea>
      <button>Submit Message</button>
    </form>
  </body>  
</html>

"""

def encrypt():
@app.route("/", method=['POST'])
rot = []
text = []
rotate_string(text)
    return <h1>text</h1>
def index():
    return form
  
app.run()
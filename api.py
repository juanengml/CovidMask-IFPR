import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from IBM import Model
UPLOAD_FOLDER = 'folder'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

api_key = " "
model_id = " "


@app.route('/api/upload_file', methods=['POST'])
def upload_file():
      if request.method == 'POST':
           data = request.files.to_dict(flat=True)[''] # checa
           data.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(data.filename)))
           print(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(data.filename)))
           os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(data.filename))
           model = Model("folder/"+str(data.filename),
                           api_key=api_key,
                           model_id=model_id)
           result = model.label_predict()
           return {"result":"sucesso upload image","classificao":result}, 200

@app.route('/')
def index():
      return {"message":"Oi Api Upload Image /api/upload_file"}



if __name__ == "__main__":
    app.run(debug=True)

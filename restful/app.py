from flask import Flask, jsonify, request, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

languages = [{'name' : 'Javascript'}, {'name' : 'Ruby'}, {'name' : 'Python'},]

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
        if request.method == 'POST' and 'photo' in request.files:
                filename = photos.save(request.files['photo'])
                return filename
        return render_template('upload.html')

@app.route('/', methods=['GET'])
def test():
        return jsonify({'message' : 'It works'})

@app.route('/lang', methods=['GET'])
def returnAll():
        return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
        langs = [language for language in languages if language['name'] == name]
        return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
        language = {'name' : request.json['name']}
        languages.append(language)

        return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
        langs = [language for language in languages if language['name'] == name]
        print(langs)
        langs[0]['name'] = request.json['name']
        return jsonify({'languages' : languages})

@app.route('/lang/<string:name>' , methods=['DELETE'])
def removeOne(name):
        languages.remove([language for language in languages if language['name'] == name][0])
        return jsonify({'languages' : languages})


if __name__ == "__main__":
        app.run(debug=True)

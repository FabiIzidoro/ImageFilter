from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from filtros import aplicar_filtro

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROCESSED_FOLDER'] = 'static/processed'

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['imagem']
        filtro = request.form['filtro']
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)

            processed_image = aplicar_filtro(upload_path, filtro)
            processed_filename = f"processed_{filename}"
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
            processed_image.save(processed_path)

            return render_template('index.html',
                                   imagem_original=filename,
                                   imagem_processada=processed_filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

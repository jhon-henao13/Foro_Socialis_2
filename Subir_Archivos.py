# import os
# from flask import Flask, render_template, request
# from werkzeug import secure_filename

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = "./Archivos PDF"

# @app.route("/")
# def upload_file():
#     return render_template('myblog/templates/blog/create.html')

# @app.route("/uploader", methods=['POST'])
# def uploader():
#     if request.method == "POST":
#         f = request.files['files']
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return "Archivo subido exitosamente"

# if __name__ == '__main__':
#     app.run(debug=True)




#from flask import Flask, jsonify,render_template,request
#from werkzeug.utils import secure_filename
#import os
#
#app = Flask(__name__)
#app.config["UPLOAD_FOLDER"] = "Archivos PDF"
#ALLOWED_EXTENSIONS = set(['png',"jpg","jpeg","gif"])
#
#
#def allowed_files(files):
#    files = files.split(".")
#    print(files)
#    if files[1] in ALLOWED_EXTENSIONS:
#        return True
#    return False
#
#@app.route('/uploader' ,methods=["POST"])
#def uploader():
#    files = request.files["uploadFile"]
#    print(files,files.filename)
#    filename = secure_filename(files.filename)
#    print(filename)
#    if allowed_files(filename):
#        print("permitido")
#    return 'Vas bien'
from flask import(
    jsonify, render_template, Blueprint, flash, Flask, g, redirect, request, url_for, current_app
)

#from werkzeug.utils import secure_filename
# import os
from werkzeug.exceptions import abort

from myblog.models.post import Post
from myblog.models.post2 import Post2
from myblog.models.post_peliculas import PostPeliculas
from myblog.models.post_netflix import PostNetflix
from myblog.models.post_hbo import PostHbo
from myblog.models.post_comics import PostComics
from myblog.models.post_tech import PostTech
from myblog.models.post_literatura import PostLiteratura
from myblog.models.post_math import PostMath
from myblog.models.post_biologicas import PostBiologicas
from myblog.models.post_politicas import PostPoliticas
from myblog.models.post_computacion import PostComputacion
from myblog.models.post_programacion import PostProgramacion
from myblog.models.post_ciberseguridad import PostCiberseguridad
from myblog.models.post_quimica import PostQuimica
from myblog.models.post_artes import PostArtes
from myblog.models.post_vrandom import PostVrandom
from myblog.models.post_vindie import PostVindie
from myblog.models.post_vonline import PostVonline
from myblog.models.post_vmobile import PostVmobile
from myblog.models.post_vestrategia import PostVestrategia
from myblog.models.post_vnoticias import PostVnoticias

from myblog.models.user import User

from myblog.views.auth import login_required

from myblog import db

blog = Blueprint('blog', __name__)

#app = Flask(__name__)
#app.config["UPLOAD_FOLDER"] = "myblog/myblog/uploader"
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#def allowed_files(files):
#    files = files.split(".")
#    print(files)
#    if files[1] in ALLOWED_EXTENSIONS:
#        return True
#    return False

# Carpeta de archivos
#@blog.route('/uploader', methods=['POST'])
#def uploader():
#    files = request.files.get("files")
#    print(files,files.filename)
#    filename = secure_filename(files.filename)
#    print(filename)
#    if files and allowed_files(filename):
#        print("permitido")
#        files.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
#
#    return 'Archivo subido'


#@blog.route('/myblog/myblog/uploader/<filename>')
#def get_image(filename):
#    return current_app.send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


# Obtener un usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user




# Configurar directorio de carga de archivos en la aplicación principal
#@blog.record_once
#def on_load(state):
#    app = state.app
#    with app.app_context():
#        app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'myblog', 'uploader')


@blog.route("/")
def index():
    return render_template('blog/index.html')


@blog.route("/tableros/musica")
def post_musica():
    posts = Post.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    return render_template('blog/create.html', posts = posts, get_user=get_user)



# Registrar una publicacion
@blog.route('/tableros/musica', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')


        post = Post(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.post_musica'))

        flash(error)

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = Post.query.get(id)

    if post is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post.author != g.user.id:
        abort(404)

    return post

# Actualizar una publicacion
@blog.route('/blog/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):

    post = get_post(id)

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        
        error = None
        if not post.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.post_musica'))

        flash(error)

    return render_template('blog/update.html', post=post)

# Eliminar una publicacion
@blog.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.post_musica'))


# 22 foros, 22 funciones

# Actualizacion


@blog.route("/tableros/programas")
def post_programas():
    posts2 = Post2.query.all()
    posts2 = list(reversed(posts2))
    db.session.commit()
    return render_template('blog/create-programas.html', posts2 = posts2, get_user=get_user)



# Registrar una publicacion en programas
@blog.route('/tableros/programas', methods=('GET', 'POST'))
@login_required
def create_programas():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post2 = Post2(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post2)
            db.session.commit()
            return redirect(url_for('blog.post_programas'))

        flash(error)

    return render_template('blog/create-programas.html')

def get_post2(id, check_author=True):
    post2 = Post2.query.get(id)

    if post2 is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post2.author != g.user.id:
        abort(404)

    return post2

# Actualizar una publicacion en programas
@blog.route('/blog/programas/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update2(id):

    post2 = get_post2(id)

    if request.method == 'POST':
        post2.title = request.form.get('title')
        post2.body = request.form.get('body')
        
        error = None
        if not post2.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post2)
            db.session.commit()
            return redirect(url_for('blog.post_programas'))

        flash(error)

    return render_template('blog/update2.html', post2=post2)

# Eliminar una publicacion en programas
@blog.route('/blog/programas/delete/<int:id>')
@login_required
def delete2(id):
    post2 = get_post2(id)
    db.session.delete(post2)
    db.session.commit()

    return redirect(url_for('blog.post_programas'))




@blog.route("/tableros/peliculas")
def post_peliculas():
    posts_peliculas = PostPeliculas.query.all()
    posts_peliculas = list(reversed(posts_peliculas))
    db.session.commit()
    return render_template('blog/create-peliculas.html', posts_peliculas = posts_peliculas, get_user=get_user)


# Registrar una publicacion en peliculas
@blog.route('/tableros/peliculas', methods=('GET', 'POST'))
@login_required
def create_peliculas():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_peliculas = PostPeliculas(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_peliculas)
            db.session.commit()
            return redirect(url_for('blog.post_peliculas'))

        flash(error)

    return render_template('blog/create-peliculas.html')

def get_post3(id, check_author=True):
    post_peliculas = PostPeliculas.query.get(id)

    if post_peliculas is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_peliculas.author != g.user.id:
        abort(404)

    return post_peliculas


# Actualizar una publicacion en peliculas
@blog.route('/blog/peliculas/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updatePeliculas(id):

    post_peliculas = get_post3(id)

    if request.method == 'POST':
        post_peliculas.title = request.form.get('title')
        post_peliculas.body = request.form.get('body')
        
        error = None
        if not post_peliculas.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_peliculas)
            db.session.commit()
            return redirect(url_for('blog.post_peliculas'))

        flash(error)

    return render_template('blog/updatePeliculas.html', post_peliculas=post_peliculas)

# Eliminar una publicacion en peliculas
@blog.route('/blog/peliculas/delete/<int:id>')
@login_required
def deletePeliculas(id):
    post_peliculas = get_post3(id)
    db.session.delete(post_peliculas)
    db.session.commit()

    return redirect(url_for('blog.post_peliculas'))




@blog.route("/tableros/netflix")
def post_netflix():
    posts_netflix = PostNetflix.query.all()
    posts_netflix = list(reversed(posts_netflix))
    db.session.commit()
    return render_template('blog/create-netflix.html', posts_netflix = posts_netflix, get_user=get_user)

# Registrar una publicacion en Netflix
@blog.route('/tableros/netflix', methods=('GET', 'POST'))
@login_required
def create_netflix():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_netflix = PostNetflix(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_netflix)
            db.session.commit()
            return redirect(url_for('blog.post_netflix'))

        flash(error)

    return render_template('blog/create-netflix.html')

def get_post4(id, check_author=True):
    post_netflix = PostNetflix.query.get(id)

    if post_netflix is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_netflix.author != g.user.id:
        abort(404)

    return post_netflix


# Actualizar una publicacion en Netflix
@blog.route('/blog/netflix/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateNetflix(id):

    post_netflix = get_post4(id)

    if request.method == 'POST':
        post_netflix.title = request.form.get('title')
        post_netflix.body = request.form.get('body')
        
        error = None
        if not post_netflix.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_netflix)
            db.session.commit()
            return redirect(url_for('blog.post_netflix'))

        flash(error)

    return render_template('blog/updateNetflix.html', post_netflix=post_netflix)

# Eliminar una publicacion en Netflix
@blog.route('/blog/netflix/delete/<int:id>')
@login_required
def deleteNetflix(id):
    post_netflix = get_post4(id)
    db.session.delete(post_netflix)
    db.session.commit()

    return redirect(url_for('blog.post_netflix'))




@blog.route("/tableros/hbo")
def post_hbo():
    posts_hbo = PostHbo.query.all()
    posts_hbo = list(reversed(posts_hbo))
    db.session.commit()
    return render_template('blog/create-hbo.html', posts_hbo = posts_hbo, get_user=get_user)


# Registrar una publicacion en hbo
@blog.route('/tableros/hbo', methods=('GET', 'POST'))
@login_required
def create_hbo():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_hbo = PostHbo(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_hbo)
            db.session.commit()
            return redirect(url_for('blog.post_hbo'))

        flash(error)

    return render_template('blog/create-hbo.html')

def get_post5(id, check_author=True):
    post_hbo = PostHbo.query.get(id)

    if post_hbo is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_hbo.author != g.user.id:
        abort(404)

    return post_hbo


# Actualizar una publicacion en HBO
@blog.route('/blog/hbo/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateHbo(id):

    post_hbo = get_post5(id)

    if request.method == 'POST':
        post_hbo.title = request.form.get('title')
        post_hbo.body = request.form.get('body')
        
        error = None
        if not post_hbo.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_hbo)
            db.session.commit()
            return redirect(url_for('blog.post_hbo'))

        flash(error)

    return render_template('blog/updateHbo.html', post_hbo=post_hbo)

# Eliminar una publicacion en Hbo
@blog.route('/blog/hbo/delete/<int:id>')
@login_required
def deleteHbo(id):
    post_hbo = get_post5(id)
    db.session.delete(post_hbo)
    db.session.commit()

    return redirect(url_for('blog.post_hbo'))






@blog.route("/tableros/comics")
def post_comics():
    posts_comics = PostComics.query.all()
    posts_comics = list(reversed(posts_comics))
    db.session.commit()
    return render_template('blog/create-comics.html', posts_comics = posts_comics, get_user=get_user)



# Registrar una publicacion en Comics
@blog.route('/tableros/comics', methods=('GET', 'POST'))
@login_required
def create_comics():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_comics = PostComics(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_comics)
            db.session.commit()
            return redirect(url_for('blog.post_comics'))

        flash(error)

    return render_template('blog/create-comics.html')

def get_post6(id, check_author=True):
    post_comics = PostComics.query.get(id)

    if post_comics is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_comics.author != g.user.id:
        abort(404)

    return post_comics


# Actualizar una publicacion en Comics
@blog.route('/blog/comics/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateComics(id):

    post_comics = get_post6(id)

    if request.method == 'POST':
        post_comics.title = request.form.get('title')
        post_comics.body = request.form.get('body')
        
        error = None
        if not post_comics.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_comics)
            db.session.commit()
            return redirect(url_for('blog.post_comics'))

        flash(error)

    return render_template('blog/updateComics.html', post_comics=post_comics)

# Eliminar una publicacion en comics
@blog.route('/blog/comics/delete/<int:id>')
@login_required
def deleteComics(id):
    post_comics = get_post6(id)
    db.session.delete(post_comics)
    db.session.commit()

    return redirect(url_for('blog.post_comics'))





@blog.route("/tableros/tech")
def post_tech():
    posts_tech = PostTech.query.all()
    posts_tech = list(reversed(posts_tech))
    db.session.commit()
    return render_template('blog/create-tech.html', posts_tech = posts_tech, get_user=get_user)



# Registrar una publicacion en Tech
@blog.route('/tableros/tech', methods=('GET', 'POST'))
@login_required
def create_tech():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_tech = PostTech(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_tech)
            db.session.commit()
            return redirect(url_for('blog.post_tech'))

        flash(error)

    return render_template('blog/create-tech.html')

def get_post7(id, check_author=True):
    post_tech = PostTech.query.get(id)

    if post_tech is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_tech.author != g.user.id:
        abort(404)

    return post_tech


# Actualizar una publicacion en Tech
@blog.route('/blog/tech/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateTech(id):

    post_tech = get_post7(id)

    if request.method == 'POST':
        post_tech.title = request.form.get('title')
        post_tech.body = request.form.get('body')
        
        error = None
        if not post_tech.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_tech)
            db.session.commit()
            return redirect(url_for('blog.post_tech'))

        flash(error)

    return render_template('blog/updateTech.html', post_tech=post_tech)

# Eliminar una publicacion en Tech
@blog.route('/blog/tech/delete/<int:id>')
@login_required
def deleteTech(id):
    post_tech = get_post7(id)
    db.session.delete(post_tech)
    db.session.commit()

    return redirect(url_for('blog.post_tech'))





@blog.route("/tableros/literatura")
def post_literatura():
    posts_literatura = PostLiteratura.query.all()
    posts_literatura = list(reversed(posts_literatura))
    db.session.commit()
    return render_template('blog/create-literatura.html', posts_literatura = posts_literatura, get_user=get_user)



# Registrar una publicacion en Literatura
@blog.route('/tableros/literatura', methods=('GET', 'POST'))
@login_required
def create_literatura():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_literatura = PostLiteratura(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_literatura)
            db.session.commit()
            return redirect(url_for('blog.post_literatura'))

        flash(error)

    return render_template('blog/create-literatura.html')

def get_post8(id, check_author=True):
    post_literatura = PostLiteratura.query.get(id)

    if post_literatura is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_literatura.author != g.user.id:
        abort(404)

    return post_literatura


# Actualizar una publicacion en Literatura
@blog.route('/blog/literatura/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateLiteratura(id):

    post_literatura = get_post8(id)

    if request.method == 'POST':
        post_literatura.title = request.form.get('title')
        post_literatura.body = request.form.get('body')
        
        error = None
        if not post_literatura.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_literatura)
            db.session.commit()
            return redirect(url_for('blog.post_literatura'))

        flash(error)

    return render_template('blog/updateLiteratura.html', post_literatura=post_literatura)

# Eliminar una publicacion en Literatura
@blog.route('/blog/literatura/delete/<int:id>')
@login_required
def deleteLiteratura(id):
    post_literatura = get_post8(id)
    db.session.delete(post_literatura)
    db.session.commit()

    return redirect(url_for('blog.post_literatura'))




@blog.route("/tableros/math")
def post_math():
    posts_math = PostMath.query.all()
    posts_math = list(reversed(posts_math))
    db.session.commit()
    return render_template('blog/create-math.html', posts_math = posts_math, get_user=get_user)



# Registrar una publicacion en Math
@blog.route('/tableros/math', methods=('GET', 'POST'))
@login_required
def create_math():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_math = PostMath(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_math)
            db.session.commit()
            return redirect(url_for('blog.post_math'))

        flash(error)

    return render_template('blog/create-math.html')

def get_post9(id, check_author=True):
    post_math = PostMath.query.get(id)

    if post_math is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_math.author != g.user.id:
        abort(404)

    return post_math


# Actualizar una publicacion en Math
@blog.route('/blog/math/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateMath(id):

    post_math = get_post9(id)

    if request.method == 'POST':
        post_math.title = request.form.get('title')
        post_math.body = request.form.get('body')
        
        error = None
        if not post_math.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_math)
            db.session.commit()
            return redirect(url_for('blog.post_math'))

        flash(error)

    return render_template('blog/updateMath.html', post_math=post_math)

# Eliminar una publicacion en Math
@blog.route('/blog/math/delete/<int:id>')
@login_required
def deleteMath(id):
    post_math = get_post9(id)
    db.session.delete(post_math)
    db.session.commit()

    return redirect(url_for('blog.post_math'))






@blog.route("/tableros/biologicas")
def post_biologicas():
    posts_biologicas = PostBiologicas.query.all()
    posts_biologicas = list(reversed(posts_biologicas))
    db.session.commit()
    return render_template('blog/create-biologicas.html', posts_biologicas = posts_biologicas, get_user=get_user)


# Registrar una publicacion en C-Biologicas
@blog.route('/tableros/biologicas', methods=('GET', 'POST'))
@login_required
def create_biologicas():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_biologicas = PostBiologicas(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_biologicas)
            db.session.commit()
            return redirect(url_for('blog.post_biologicas'))

        flash(error)

    return render_template('blog/create-biologicas.html')

def get_post10(id, check_author=True):
    post_biologicas = PostBiologicas.query.get(id)

    if post_biologicas is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_biologicas.author != g.user.id:
        abort(404)

    return post_biologicas


# Actualizar una publicacion en C-Biologicas
@blog.route('/blog/biologicas/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateBiologicas(id):

    post_biologicas = get_post10(id)

    if request.method == 'POST':
        post_biologicas.title = request.form.get('title')
        post_biologicas.body = request.form.get('body')
        
        error = None
        if not post_biologicas.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_biologicas)
            db.session.commit()
            return redirect(url_for('blog.post_biologicas'))

        flash(error)

    return render_template('blog/updateBiologicas.html', post_biologicas=post_biologicas)

# Eliminar una publicacion en C-Biologicas
@blog.route('/blog/biologicas/delete/<int:id>')
@login_required
def deleteBiologicas(id):
    post_biologicas = get_post10(id)
    db.session.delete(post_biologicas)
    db.session.commit()

    return redirect(url_for('blog.post_biologicas'))







@blog.route("/tableros/politicas")
def post_politicas():
    posts_politicas = PostPoliticas.query.all()
    posts_politicas = list(reversed(posts_politicas))
    db.session.commit()
    return render_template('blog/create-politicas.html', posts_politicas = posts_politicas, get_user=get_user)


# Registrar una publicacion en C-Politicas
@blog.route('/tableros/politicas', methods=('GET', 'POST'))
@login_required
def create_politicas():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_politicas = PostPoliticas(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_politicas)
            db.session.commit()
            return redirect(url_for('blog.post_politicas'))

        flash(error)

    return render_template('blog/create-politicas.html')

def get_post11(id, check_author=True):
    post_politicas = PostPoliticas.query.get(id)

    if post_politicas is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_politicas.author != g.user.id:
        abort(404)

    return post_politicas


# Actualizar una publicacion en C-Politicas
@blog.route('/blog/politicas/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updatePoliticas(id):

    post_politicas = get_post11(id)

    if request.method == 'POST':
        post_politicas.title = request.form.get('title')
        post_politicas.body = request.form.get('body')
        
        error = None
        if not post_politicas.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_politicas)
            db.session.commit()
            return redirect(url_for('blog.post_politicas'))

        flash(error)

    return render_template('blog/updatePoliticas.html', post_politicas=post_politicas)

# Eliminar una publicacion en C-Politicas
@blog.route('/blog/politicas/delete/<int:id>')
@login_required
def deletePoliticas(id):
    post_politicas = get_post11(id)
    db.session.delete(post_politicas)
    db.session.commit()

    return redirect(url_for('blog.post_politicas'))




@blog.route("/tableros/computacion")
def post_computacion():
    posts_computacion = PostComputacion.query.all()
    posts_computacion = list(reversed(posts_computacion))
    db.session.commit()
    return render_template('blog/create-computacion.html', posts_computacion = posts_computacion, get_user=get_user)


# Registrar una publicacion en Computacion
@blog.route('/tableros/computacion', methods=('GET', 'POST'))
@login_required
def create_computacion():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_computacion = PostComputacion(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_computacion)
            db.session.commit()
            return redirect(url_for('blog.post_computacion'))

        flash(error)

    return render_template('blog/create-computacion.html')

def get_post12(id, check_author=True):
    post_computacion = PostComputacion.query.get(id)

    if post_computacion is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_computacion.author != g.user.id:
        abort(404)

    return post_computacion


# Actualizar una publicacion en Computacion
@blog.route('/blog/computacion/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateComputacion(id):

    post_computacion = get_post12(id)

    if request.method == 'POST':
        post_computacion.title = request.form.get('title')
        post_computacion.body = request.form.get('body')
        
        error = None
        if not post_computacion.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_computacion)
            db.session.commit()
            return redirect(url_for('blog.post_computacion'))

        flash(error)

    return render_template('blog/updateComputacion.html', post_computacion=post_computacion)

# Eliminar una publicacion en Computacion
@blog.route('/blog/computacion/delete/<int:id>')
@login_required
def deleteComputacion(id):
    post_computacion = get_post12(id)
    db.session.delete(post_computacion)
    db.session.commit()

    return redirect(url_for('blog.post_computacion'))







@blog.route("/tableros/programacion")
def post_programacion():
    posts_programacion = PostProgramacion.query.all()
    posts_programacion = list(reversed(posts_programacion))
    db.session.commit()
    return render_template('blog/create-programacion.html', posts_programacion = posts_programacion, get_user=get_user)


# Registrar una publicacion en Programacion
@blog.route('/tableros/programacion', methods=('GET', 'POST'))
@login_required
def create_programacion():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_programacion = PostProgramacion(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_programacion)
            db.session.commit()
            return redirect(url_for('blog.post_programacion'))

        flash(error)

    return render_template('blog/create-programacion.html')

def get_post13(id, check_author=True):
    post_programacion = PostProgramacion.query.get(id)

    if post_programacion is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_programacion.author != g.user.id:
        abort(404)

    return post_programacion


# Actualizar una publicacion en Programacion
@blog.route('/blog/programacion/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateProgramacion(id):

    post_programacion = get_post13(id)

    if request.method == 'POST':
        post_programacion.title = request.form.get('title')
        post_programacion.body = request.form.get('body')
        
        error = None
        if not post_programacion.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_programacion)
            db.session.commit()
            return redirect(url_for('blog.post_programacion'))

        flash(error)

    return render_template('blog/updateProgramacion.html', post_programacion=post_programacion)

# Eliminar una publicacion en Programacion
@blog.route('/blog/programacion/delete/<int:id>')
@login_required
def deleteProgramacion(id):
    post_programacion = get_post13(id)
    db.session.delete(post_programacion)
    db.session.commit()

    return redirect(url_for('blog.post_programacion'))





@blog.route("/tableros/ciberseguridad")
def post_ciberseguridad():
    posts_ciberseguridad = PostCiberseguridad.query.all()
    posts_ciberseguridad = list(reversed(posts_ciberseguridad))
    db.session.commit()
    return render_template('blog/create-ciberseguridad.html', posts_ciberseguridad = posts_ciberseguridad, get_user=get_user)


# Registrar una publicacion en Ciberseguridad
@blog.route('/tableros/ciberseguridad', methods=('GET', 'POST'))
@login_required
def create_ciberseguridad():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_ciberseguridad = PostCiberseguridad(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_ciberseguridad)
            db.session.commit()
            return redirect(url_for('blog.post_ciberseguridad'))

        flash(error)

    return render_template('blog/create-ciberseguridad.html')

def get_post14(id, check_author=True):
    post_ciberseguridad = PostCiberseguridad.query.get(id)

    if post_ciberseguridad is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_ciberseguridad.author != g.user.id:
        abort(404)

    return post_ciberseguridad


# Actualizar una publicacion en Ciberseguridad
@blog.route('/blog/ciberseguridad/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateCiberseguridad(id):

    post_ciberseguridad = get_post14(id)

    if request.method == 'POST':
        post_ciberseguridad.title = request.form.get('title')
        post_ciberseguridad.body = request.form.get('body')
        
        error = None
        if not post_ciberseguridad.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_ciberseguridad)
            db.session.commit()
            return redirect(url_for('blog.post_ciberseguridad'))

        flash(error)

    return render_template('blog/updateCiberseguridad.html', post_ciberseguridad=post_ciberseguridad)

# Eliminar una publicacion en Ciberseguridad
@blog.route('/blog/ciberseguridad/delete/<int:id>')
@login_required
def deleteCiberseguridad(id):
    post_ciberseguridad = get_post14(id)
    db.session.delete(post_ciberseguridad)
    db.session.commit()

    return redirect(url_for('blog.post_ciberseguridad'))







@blog.route("/tableros/quimica")
def post_quimica():
    posts_quimica = PostQuimica.query.all()
    posts_quimica = list(reversed(posts_quimica))
    db.session.commit()
    return render_template('blog/create-quimica.html', posts_quimica = posts_quimica, get_user=get_user)


# Registrar una publicacion en Quimica
@blog.route('/tableros/quimica', methods=('GET', 'POST'))
@login_required
def create_quimica():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_quimica = PostQuimica(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_quimica)
            db.session.commit()
            return redirect(url_for('blog.post_quimica'))

        flash(error)

    return render_template('blog/create-quimica.html')

def get_post15(id, check_author=True):
    post_quimica = PostQuimica.query.get(id)

    if post_quimica is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_quimica.author != g.user.id:
        abort(404)

    return post_quimica


# Actualizar una publicacion en Quimica
@blog.route('/blog/quimica/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateQuimica(id):

    post_quimica = get_post15(id)

    if request.method == 'POST':
        post_quimica.title = request.form.get('title')
        post_quimica.body = request.form.get('body')
        
        error = None
        if not post_quimica.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_quimica)
            db.session.commit()
            return redirect(url_for('blog.post_quimica'))

        flash(error)

    return render_template('blog/updateQuimica.html', post_quimica=post_quimica)

# Eliminar una publicacion en Quimica
@blog.route('/blog/quimica/delete/<int:id>')
@login_required
def deleteQuimica(id):
    post_quimica = get_post15(id)
    db.session.delete(post_quimica)
    db.session.commit()

    return redirect(url_for('blog.post_quimica'))




@blog.route("/tableros/artes")
def post_artes():
    posts_artes = PostArtes.query.all()
    posts_artes = list(reversed(posts_artes))
    db.session.commit()
    return render_template('blog/create-artes.html', posts_artes = posts_artes, get_user=get_user)


# Registrar una publicacion en Artes
@blog.route('/tableros/artes', methods=('GET', 'POST'))
@login_required
def create_artes():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_artes = PostArtes(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_artes)
            db.session.commit()
            return redirect(url_for('blog.post_artes'))

        flash(error)

    return render_template('blog/create-artes.html')

def get_post16(id, check_author=True):
    post_artes = PostArtes.query.get(id)

    if post_artes is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_artes.author != g.user.id:
        abort(404)

    return post_artes


# Actualizar una publicacion en Artes
@blog.route('/blog/artes/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateArtes(id):

    post_artes = get_post16(id)

    if request.method == 'POST':
        post_artes.title = request.form.get('title')
        post_artes.body = request.form.get('body')
        
        error = None
        if not post_artes.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_artes)
            db.session.commit()
            return redirect(url_for('blog.post_artes'))

        flash(error)

    return render_template('blog/updateArtes.html', post_artes=post_artes)

# Eliminar una publicacion en Artes
@blog.route('/blog/artes/delete/<int:id>')
@login_required
def deleteArtes(id):
    post_artes = get_post16(id)
    db.session.delete(post_artes)
    db.session.commit()

    return redirect(url_for('blog.post_artes'))










@blog.route("/tableros/v-random")
def post_vrandom():
    posts_vrandom = PostVrandom.query.all()
    posts_vrandom = list(reversed(posts_vrandom))
    db.session.commit()
    return render_template('blog/create-v-random.html', posts_vrandom = posts_vrandom, get_user=get_user)


# Registrar una publicacion en V-Random
@blog.route('/tableros/v-random', methods=('GET', 'POST'))
@login_required
def create_vrandom():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_vrandom = PostVrandom(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vrandom)
            db.session.commit()
            return redirect(url_for('blog.post_vrandom'))

        flash(error)

    return render_template('blog/create-v-random.html')

def get_post17(id, check_author=True):
    post_vrandom = PostVrandom.query.get(id)

    if post_vrandom is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_vrandom.author != g.user.id:
        abort(404)

    return post_vrandom


# Actualizar una publicacion en V-Random
@blog.route('/blog/v-random/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateVrandom(id):

    post_vrandom = get_post17(id)

    if request.method == 'POST':
        post_vrandom.title = request.form.get('title')
        post_vrandom.body = request.form.get('body')
        
        error = None
        if not post_vrandom.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vrandom)
            db.session.commit()
            return redirect(url_for('blog.post_vrandom'))

        flash(error)

    return render_template('blog/updateVrandom.html', post_vrandom=post_vrandom)

# Eliminar una publicacion en V-Random
@blog.route('/blog/v-random/delete/<int:id>')
@login_required
def deleteVrandom(id):
    post_vrandom = get_post17(id)
    db.session.delete(post_vrandom)
    db.session.commit()

    return redirect(url_for('blog.post_vrandom'))






@blog.route("/tableros/v-indie")
def post_vindie():
    posts_vindie = PostVindie.query.all()
    posts_vindie = list(reversed(posts_vindie))
    db.session.commit()
    return render_template('blog/create-v-indie.html', posts_vindie = posts_vindie, get_user=get_user)


# Registrar una publicacion en V-Indie
@blog.route('/tableros/v-indie', methods=('GET', 'POST'))
@login_required
def create_vindie():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_vindie = PostVindie(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vindie)
            db.session.commit()
            return redirect(url_for('blog.post_vindie'))

        flash(error)

    return render_template('blog/create-v-indie.html')

def get_post18(id, check_author=True):
    post_vindie = PostVindie.query.get(id)

    if post_vindie is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_vindie.author != g.user.id:
        abort(404)

    return post_vindie


# Actualizar una publicacion en V-Indie
@blog.route('/blog/v-indie/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateVindie(id):

    post_vindie = get_post18(id)

    if request.method == 'POST':
        post_vindie.title = request.form.get('title')
        post_vindie.body = request.form.get('body')
        
        error = None
        if not post_vindie.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vindie)
            db.session.commit()
            return redirect(url_for('blog.post_vindie'))

        flash(error)

    return render_template('blog/updateVindie.html', post_vindie=post_vindie)

# Eliminar una publicacion en V-Indie
@blog.route('/blog/v-indie/delete/<int:id>')
@login_required
def deleteVindie(id):
    post_vindie = get_post18(id)
    db.session.delete(post_vindie)
    db.session.commit()

    return redirect(url_for('blog.post_vindie'))






@blog.route("/tableros/v-online")
def post_vonline():
    posts_vonline = PostVonline.query.all()
    posts_vonline = list(reversed(posts_vonline))
    db.session.commit()
    return render_template('blog/create-v-online.html', posts_vonline = posts_vonline, get_user=get_user)


# Registrar una publicacion en V-Multijugador
@blog.route('/tableros/v-online', methods=('GET', 'POST'))
@login_required
def create_vonline():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_vonline = PostVonline(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vonline)
            db.session.commit()
            return redirect(url_for('blog.post_vonline'))

        flash(error)

    return render_template('blog/create-v-online.html')

def get_post19(id, check_author=True):
    post_vonline = PostVonline.query.get(id)

    if post_vonline is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_vonline.author != g.user.id:
        abort(404)

    return post_vonline


# Actualizar una publicacion en V-Multijugador
@blog.route('/blog/v-online/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateVonline(id):

    post_vonline = get_post19(id)

    if request.method == 'POST':
        post_vonline.title = request.form.get('title')
        post_vonline.body = request.form.get('body')
        
        error = None
        if not post_vonline.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vonline)
            db.session.commit()
            return redirect(url_for('blog.post_vonline'))

        flash(error)

    return render_template('blog/updateVonline.html', post_vonline=post_vonline)

# Eliminar una publicacion en V-Multijugador
@blog.route('/blog/v-online/delete/<int:id>')
@login_required
def deleteVonline(id):
    post_vonline = get_post19(id)
    db.session.delete(post_vonline)
    db.session.commit()

    return redirect(url_for('blog.post_vonline'))





@blog.route("/tableros/v-mobile")
def post_vmobile():
    posts_vmobile = PostVmobile.query.all()
    posts_vmobile = list(reversed(posts_vmobile))
    db.session.commit()
    return render_template('blog/create-v-mobile.html', posts_vmobile = posts_vmobile, get_user=get_user)


# Registrar una publicacion en V-Mobile
@blog.route('/tableros/v-mobile', methods=('GET', 'POST'))
@login_required
def create_vmobile():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_vmobile = PostVmobile(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vmobile)
            db.session.commit()
            return redirect(url_for('blog.post_vmobile'))

        flash(error)

    return render_template('blog/create-v-mobile.html')

def get_post20(id, check_author=True):
    post_vmobile = PostVmobile.query.get(id)

    if post_vonline is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_vmobile.author != g.user.id:
        abort(404)

    return post_vmobile


# Actualizar una publicacion en V-Mobile
@blog.route('/blog/v-mobile/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateVmobile(id):

    post_vmobile = get_post20(id)

    if request.method == 'POST':
        post_vmobile.title = request.form.get('title')
        post_vmobile.body = request.form.get('body')
        
        error = None
        if not post_vmobile.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vmobile)
            db.session.commit()
            return redirect(url_for('blog.post_vmobile'))

        flash(error)

    return render_template('blog/updateVmobile.html', post_vmobile=post_vmobile)

# Eliminar una publicacion en V-Mobile
@blog.route('/blog/v-mobile/delete/<int:id>')
@login_required
def deleteVmobile(id):
    post_vmobile = get_post20(id)
    db.session.delete(post_vmobile)
    db.session.commit()

    return redirect(url_for('blog.post_vmobile'))






@blog.route("/tableros/v-estrategia")
def post_vestrategia():
    posts_vestrategia = PostVestrategia.query.all()
    posts_vestrategia = list(reversed(posts_vestrategia))
    db.session.commit()
    return render_template('blog/create-v-estrategia.html', posts_vestrategia = posts_vestrategia, get_user=get_user)


# Registrar una publicacion en V-Estrategia
@blog.route('/tableros/v-estrategia', methods=('GET', 'POST'))
@login_required
def create_vestrategia():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_vestrategia = PostVestrategia(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vestrategia)
            db.session.commit()
            return redirect(url_for('blog.post_vestrategia'))

        flash(error)

    return render_template('blog/create-v-estrategia.html')

def get_post21(id, check_author=True):
    post_vestrategia = PostVestrategia.query.get(id)

    if post_vestrategia is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_vestrategia.author != g.user.id:
        abort(404)

    return post_vestrategia


# Actualizar una publicacion en V-Estrategia
@blog.route('/blog/v-estrategia/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateVestrategia(id):

    post_vestrategia = get_post21(id)

    if request.method == 'POST':
        post_vestrategia.title = request.form.get('title')
        post_vestrategia.body = request.form.get('body')
        
        error = None
        if not post_vestrategia.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vestrategia)
            db.session.commit()
            return redirect(url_for('blog.post_vestrategia'))

        flash(error)

    return render_template('blog/updateVestrategia.html', post_vestrategia=post_vestrategia)

# Eliminar una publicacion en V-Estrategia
@blog.route('/blog/v-estrategia/delete/<int:id>')
@login_required
def deleteVestrategia(id):
    post_vestrategia = get_post21(id)
    db.session.delete(post_vestrategia)
    db.session.commit()

    return redirect(url_for('blog.post_vestrategia'))












@blog.route("/tableros/v-noticias")
def post_vnoticias():
    posts_vnoticias = PostVnoticias.query.all()
    posts_vnoticias = list(reversed(posts_vnoticias))
    db.session.commit()
    return render_template('blog/create-v-noticias.html', posts_vnoticias = posts_vnoticias, get_user=get_user)


# Registrar una publicacion en V-Noticias
@blog.route('/tableros/v-noticias', methods=('GET', 'POST'))
@login_required
def create_vnoticias():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        

        post_vnoticias = PostVnoticias(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vnoticias)
            db.session.commit()
            return redirect(url_for('blog.post_vnoticias'))

        flash(error)

    return render_template('blog/create-v-noticias.html')

def get_post22(id, check_author=True):
    post_vnoticias = PostVnoticias.query.get(id)

    if post_vnoticias is None:
        abort(404, f'Id {id} de la publicacion no existe.')

    if check_author and post_vnoticias.author != g.user.id:
        abort(404)

    return post_vnoticias


# Actualizar una publicacion en V-Noticias
@blog.route('/blog/v-noticias/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updateVnoticias(id):

    post_vnoticias = get_post22(id)

    if request.method == 'POST':
        post_vnoticias.title = request.form.get('title')
        post_vnoticias.body = request.form.get('body')
        
        error = None
        if not post_vnoticias.title:
            error = 'Se requiere un titulo'

        if error is not None:
            flash(error)
        else:
            db.session.add(post_vnoticias)
            db.session.commit()
            return redirect(url_for('blog.post_vnoticias'))

        flash(error)

    return render_template('blog/updateVnoticias.html', post_vnoticias=post_vnoticias)

# Eliminar una publicacion en V-Noticias
@blog.route('/blog/v-noticias/delete/<int:id>')
@login_required
def deleteVnoticias(id):
    post_vnoticias = get_post22(id)
    db.session.delete(post_vnoticias)
    db.session.commit()

    return redirect(url_for('blog.post_vnoticias'))


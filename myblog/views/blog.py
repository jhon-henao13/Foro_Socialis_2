from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from myblog.models.post import Post
from myblog.models.user import User

from myblog.views.auth import login_required

from myblog import db

blog = Blueprint('blog', __name__)

# Obtener un usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

@blog.route("/")
def index():
    posts = Post.query.all()
    db.session.commit()
    return render_template('blog/index.html', posts = posts)

# Registrar una publicacion
#@blog.route('/tableros/<int:foro_id>/crear-publicacion', methods=('GET', 'POST'))
#@login_required
#def register():
#    if request.method == 'POST':
#        title = request.form.get('title')
#        body = request.form.get('body')
#
#        post = Post(g.user.id, title, body)
#
#        error = None
#        if not title:
#            error = 'Se requiere un titulo'
#
#        if error is not None:
#            flash(error)
#        else:
#            db.session.add(post)
#            db.session.commit()
#            return redirect(url_for('blog.index'))
#
#        flash(error)
#
#    return render_template('blog/create.html')

# 22 foros, 22 funciones

@blog.route('/tableros/musica.html', methods=('GET', 'POST'))
@login_required
def register_musica():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/musica.html')

    



@blog.route('/tableros/programas.html', methods=('GET', 'POST'))
@login_required
def register_programas():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/programas.html')


@blog.route('/tableros/peliculas.html', methods=('GET', 'POST'))
@login_required
def register_peliculas():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/peliculas.html')


@blog.route('/tableros/netflix.html', methods=('GET', 'POST'))
@login_required
def register_netflix():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/netflix.html')


@blog.route('/tableros/hbo.html', methods=('GET', 'POST'))
@login_required
def register_hbo():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/hbo.html')


@blog.route('/tableros/comics.html', methods=('GET', 'POST'))
@login_required
def register_comics():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/comics.html')


@blog.route('/tableros/tech.html', methods=('GET', 'POST'))
@login_required
def register_tech():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/tech.html')


@blog.route('/tableros/literatura.html', methods=('GET', 'POST'))
@login_required
def register_literatura():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/literatura.html')


@blog.route('/tableros/math.html', methods=('GET', 'POST'))
@login_required
def register_math():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/math.html')


@blog.route('/tableros/c-biologicas.html', methods=('GET', 'POST'))
@login_required
def register_biologicas():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/c-biologicas.html')


@blog.route('/tableros/c-politicas.html', methods=('GET', 'POST'))
@login_required
def register_politicas():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/c-politicas.html')


@blog.route('/tableros/computacion.html', methods=('GET', 'POST'))
@login_required
def register_computacion():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/computacion.html')


@blog.route('/tableros/desarrollo.html', methods=('GET', 'POST'))
@login_required
def register_desarrollo():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/desarrollo.html')


@blog.route('/tableros/ciberseguridad.html', methods=('GET', 'POST'))
@login_required
def register_ciberseguridad():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/ciberseguridad.html')


@blog.route('/tableros/quimica.html', methods=('GET', 'POST'))
@login_required
def register_quimica():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/quimica.html')


@blog.route('/tableros/v-random.html', methods=('GET', 'POST'))
@login_required
def register_random():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/v-random.html')


@blog.route('/tableros/v-indie.html', methods=('GET', 'POST'))
@login_required
def register_indie():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/v-indie.html')


@blog.route('/tableros/v-online.html', methods=('GET', 'POST'))
@login_required
def register_online():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/v-online.html')


@blog.route('/tableros/v-mobile.html', methods=('GET', 'POST'))
@login_required
def register_mobile():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/v-mobile.html')


@blog.route('/tableros/v-estrategia.html', methods=('GET', 'POST'))
@login_required
def register_estrategia():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/v-estrategia.html')


@blog.route('/tableros/v-noticias.html', methods=('GET', 'POST'))
@login_required
def register_noticias():
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
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('/tableros/v-noticias.html')

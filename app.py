from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import Kategorieform, Blogform

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)
from models import Blogeintrag, Kategorie


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kategorie_erstellen', methods=['GET', 'POST'])
def kategorie_erstellen():
    form = Kategorieform(request.form)
    if request.method == 'POST' and form.validate():
        kategorie = Kategorie()
        kategorie.text = form.kategorie.data
        db.session.add(kategorie)
        db.session.commit()
    return render_template('kategorie_erstellen.html')


@app.route('/blog_erstellen', methods=['GET', 'POST'])
def blog_erstellen():
    form = Blogform(request.form)
    if request.method == 'POST' and form.validate():
        datum = Datum()
        datum.date = form.datum.data
        db.session.add(datum)
        db.session.commit()

    form = Blogform(request.form)
    if request.method == 'POST' and form.validate():
        titel = Titel()
        Titel.string = form.titel.data
        db.session.add(titel)
        db.session.commit()

    form = Blogform(request.form)
    if request.method == 'POST' and form.validate():
        kategorie = Kategorie()
        kategorie.text = form.kategorie.data
        db.session.add(kategorie)
        db.session.commit()

    form = Blogform(request.form)
    if request.method == 'POST' and form.validate():
        eintrag = Eintrag()
        eintrag.text = form.eintrag.data
        db.session.add(eintrag)
        db.session.commit()

    return render_template('neuerBlog.html')


if __name__ == '__main__':
    app.run()

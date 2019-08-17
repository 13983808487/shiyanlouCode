import os
import json
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
            backref=db.backref('files'))

    def __repr__(self):
        return '<File>: {}'.format(self.name)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self):
        return '<Category: %s>' % self.name


class Files(object):

    directory = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '..', 'files'))

    def __init__(self):
        self._files = self._read_all_files()

    def _read_all_files(self):
        result = {}
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result

    def get_title_list(self):
        return [item['title'] for item in self._files.values()]

    def get_by_filename(self, filename):
        return self._files[filename]


files = Files()


@app.route('/')
def index():
    return render_template('index.html', title_list=files.get_title_list())


@app.route('/files/<filename>')
def file(filename):
    file_item = files.get_by_filename(filename)
    if not file_item:
        abort(404)
    return render_template('file.html', file_item=file_item)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

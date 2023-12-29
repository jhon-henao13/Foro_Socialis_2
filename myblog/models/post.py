from datetime import datetime
from myblog import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
#    files = db.Column(db.String(255))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, author, title, body) -> None:
        self.author = author
        self.title = title
        self.body = body
#        self.files = files

    def __repr__(self) -> str:
        return f'Post: {self.title}'

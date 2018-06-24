from application import db

class Pen(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    country = db.Column(db.String(144), nullable=False)
    manufacturer = db.Column(db.String(144), nullable=False)

    collection = db.relationship("Collection", backref='pen', lazy=True)

    def __init__(self, name):
        self.name = name
 
    def getId():
        return self.id

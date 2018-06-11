from application import db

class Collection(db.Model):

    __tablename__ = "collection"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    nib = db.Column(db.String(144), nullable=False)
    color = db.Column(db.String(144), nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    pen_id = db.Column(db.Integer, db.ForeignKey('pen.id'),
                           nullable=False)

    def __init__(self, pen_id):
        self.pen_id = pen_id
        

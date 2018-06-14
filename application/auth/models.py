from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    collection = db.relationship("Collection", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def get_users_and_pennro():

        stmt1 = text("SELECT account.name FROM account, collection"
                    " WHERE account.id = collection.account_id")
        res1 = db.engine.execute(stmt1)
        count = []
        for row in res1:
            count.append({row[0]})

        stmt2 = text("SELECT account.name FROM account")
        res2 = db.engine.execute(stmt2)
        names = []
        for row in res2:
            names.append({row[0]})
        
        response = []
        i = 0
        for value in names:
            nro = 0
            for name in count:
                if name == value:
                    nro = nro + 1
  
            S = str(value)
            length = len(S)
            S = S[2:length-2]
            response.append({"name":S, "nro":nro})    
 

        return response

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
    admin = db.Column(db.Boolean, nullable=False)

    collection = db.relationship("Collection", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.admin = False
  
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

        # Ensimmäien kysely tuottaa listan nimistä jossa jokainen nimi esiintyy niin monta kertaa,
        # kuin käyttäjällä on kyniä kokoelmassaan.

        stmt1 = text("SELECT account.name FROM account, collection"
                    " WHERE account.id = collection.account_id")
        res1 = db.engine.execute(stmt1)
        count = []
        for row in res1:
            count.append({row[0]})

        # Toine kysely palauttaa listan kaikista käyttäjien nimistä

        stmt2 = text("SELECT account.name FROM account")
        res2 = db.engine.execute(stmt2)
        names = []
        for row in res2:
            names.append({row[0]})

        # Kolmas kysely palauttaa listan käyttäjien id:istä

        stmt3 = text("SELECT account.id FROM account")
        res3 = db.engine.execute(stmt3)
        ids = []
        for row in res3:
            ids.append({row[0]})

        # Lasketaan kuinka monta kertaa kukin nimi esiintyy ensimmäisessä kyselyssä,
        # eli saadaan selville kuinka monta kynää kullakin on.
        # Liitetään palautettavaan listaan jokaiselle riville käyttäjän nimi, kynien lukumäärä ja käyttäjien id

        response = []
        i = 0
        for value in names:
            nro = 0
            for name in count:
                if name == value:
                    nro = nro + 1

            # Riisutaan nimen alusta ja lopusta turhat merkit. Näin se näyttää oikealta PostgreSQL käytettäessä.
            # Jos käytössä on jokin toinen tietokantajärjestelmä, kannattaa tätä osaa muokata.

            S = str(value)
            length = len(S)
            S = S[2:length-2]

            # Poistetaan id:stä ylimääräiset merkit jotka tulevat kyselyntuloksena.
            # Koska id on aina kokonaisluku, ei ole vaaraa oleellisen merkin poistamisesta.

            iidee = str(ids[i])
            iidee = iidee.replace("set","")
            iidee = iidee.replace("([","")
            iidee = iidee.replace("])","")
            iidee = iidee.replace("{","")
            iidee = iidee.replace("}","")

            response.append({"name":S, "nro":nro, "id":iidee})
            i += 1    
 

        return response



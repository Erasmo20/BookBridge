from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    clube = db.Column(db.String(80), nullable=False)
    comentario = db.Column(db.String(180), nullable=True)  # Comentário opcional

    def __repr__(self):
        return f"<Item {self.name} - {self.clube} - {self.comentario}>"

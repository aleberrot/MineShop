from . import db

class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(40), index=False, unique=False)
    email: str = db.Column(db.String(80), index=True, unique=True)
    password: str = db.Column(db.String(128))

    def __repr__(self) -> str:
        return f'User: <{self.username}>\nEmail: <{self.email}>'

class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), index=True, unique=False)
    description: str = db.Column(db.String(1024), index=False, unique=False)
    price: int = db.Column(db.Integer, index=False, unique=False)

    def __repr__(self) -> str:
        return f'Product: <{self.name}>\nPrice: <{self.price}>'
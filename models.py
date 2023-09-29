from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class ProductModel(db.Model):
    __tablename__="products"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    description=db.Column(db.String(255))
    price=db.Column(db.Integer())
    brand=db.Column(db.String(80))

    def __int__(self,name,description,price,brand):
        self.name=name
        self.description=description
        self.price=price
        self.brand=brand

    def json(self):
        return {"name":self.name,"description":self.description,"price":self.price,"brand":self.brand}

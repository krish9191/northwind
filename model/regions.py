import uuid

from extension import db


class Territory(db.Model):
    __tablename__ = 'territories'
    territory_id = db.Column(db.String, primary_key=True, nullable=False)
    territory_description = db.Column(db.String(40), nullable=False)
    region_id = db.Column(db.SmallInteger, db.ForeignKey('region.region_id'), nullable=False)

    def __init__(self, description):
        self.territory_id = str(uuid.uuid4())
        self.territory_description = description


class Region(db.Model):
    __tablename__ = 'region'
    region_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    region_description = db.Column(db.String(40), nullable=False)
    territories = db.relationship(Territory, backref='regions', lazy='select')

    def __init__(self, description):
        self.region_id = str(uuid.uuid4())
        self.region_description = description

    @classmethod
    def find_by_id(cls, id):
        return Region.query.filter(Region.region_id == id).first()

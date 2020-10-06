from shelo import db


class All_logo (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_category = db.Column(db.Integer(), db.ForeignKey('category.id'))
    id_brand = db.Column(db.Integer(), db.ForeignKey('brand.id'))
    # id_logo = db.Column(db.Integer(), db.ForeignKey('logo_info.id'))
    year = db.Column(db.Integer())
    description = db.Column(db.Text(), nullable=True)
    file_name = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "<ID : {}>".format(self.id)


class Category (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    logos = db.relationship('All_logo', backref='category', lazy=True)

    def __repr__(self):
        return "<Category : {}>".format(self.name)


class Brand (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer())
    description = db.Column(db.Text(), nullable=False)

    id_country = db.Column(db.Integer(), db.ForeignKey('country.id'))

    logos = db.relationship('All_logo', backref='brand', lazy=True)

    def __repr__(self):
        return "<Brand : {}>".format(self.name)

class Country (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    brands = db.relationship('Brand', backref='country', lazy=True)

    def __repr__(self):
        return "<Country : {}>".format(self.name)

# class Logo_info (db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     year = db.Column(db.Integer())
#     description = db.Column(db.Text(), nullable=True)
#     file_name = db.Column(db.String(80), nullable=False)

#     logos = db.relationship('All_logo', backref='logo_info', lazy=True)

#     def __repr__(self):
#         return "<File_name : {}>".format(self.file_name)
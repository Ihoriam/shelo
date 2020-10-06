from shelo import app, db
from shelo.models import All_logo, Brand, Country, Category
from flask import render_template, request

@app.route('/')
@app.route('/main')
def main():
    brands = Brand.query.all()[:3]
    latest_logos = []
    for brand in brands:
        logos = All_logo.query.filter_by(id_brand=brand.id).all()
        latest_logos.append(sorted(logos, key=lambda logos: logos.year, reverse=True)[0])
        print(latest_logos)
    return render_template('main.html', brands=brands, logos=latest_logos)

@app.route('/brand/<int:id_brand>')
def brand_page(id_brand):
    brand = Brand.query.filter_by(id=id_brand).first()
    country = Country.query.get(brand.id_country)
    logos = All_logo.query.filter_by(id_brand=brand.id).all()
    sorted_logo = sorted(logos, key=lambda logos: logos.year, reverse=False)
    return render_template('brand.html', brand=brand, country=country, logos=sorted_logo)
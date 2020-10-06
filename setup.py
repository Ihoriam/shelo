
# run app
from shelo import app, db
from shelo.models import All_logo, Brand, Category, Country

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'All_logo': All_logo,
            'Brand': Brand,
            'Category': Category,
            'Country': Country
            }
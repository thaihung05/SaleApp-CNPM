from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from eapp.models import Categary, Product, UserRole
from flask_login import current_user
from eapp import db, app

class AdmininView(ModelView):
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class ProductView(ModelView):
    column_list = ['id', 'name', 'price','active','category_id']
    column_filters = ['id','name','price']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    page_size = 30



admin = Admin(app=app, name="e-Commerce's Admin")

admin.add_view(AdmininView(Categary, db.session))
admin.add_view(AdmininView(Product, db.session))

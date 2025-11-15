from flask import render_template, request
from werkzeug.utils import redirect
from eapp import app, dao, login
from flask_login import login_user
from eapp.models import User


@app.route('/')
def index():
    categories = dao.load_category()


    products = dao.load_products(cate_id=request.args.get('category_id'), kw=request.args.get('kw'), page=request.args.get('page'))

    return render_template('index.html', categories=categories, products = products)

@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user)
        return redirect('/admin')
    else:
        return "Tên đăng nhập hoặc mật khẩu không đúng"


@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

if __name__ == '__main__':
    from eapp import admin
    app.run(debug=True)

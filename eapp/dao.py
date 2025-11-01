from eapp.models import Categary, Product


def load_category():
    return Categary.query.all()

def load_products(cate_id=None, kw=None, page=None):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    return query.all()


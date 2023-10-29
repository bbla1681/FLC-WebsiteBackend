from flask_restx import Api

from .reviews import review_ns
from .auth import auth_ns

api = Api(
    title='RateMyFLC',
    version='1.0',
    description='RateMyFLC API',
    doc= "/doc/"
)

api.add_namespace(review_ns, path= '/class')
api.add_namespace(auth_ns, path= '/users')

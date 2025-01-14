from django.conf.urls.defaults import patterns, include, url
# from vrscommon.resource import Resource
from piston.authentication import HttpBasicAuthentication

from authentication import DjangoAuthentication
from utils import api_url, Resource
from handlers import VeresedakiHandler, TransactionHandler, \
     RelationHandler, LoginHandler, LogoutHandler, \
     BalanceHandler, CurrencyHandler, UserHandler

django_auth = DjangoAuthentication(login_url='/api/login/')
basic_auth = HttpBasicAuthentication(realm='verese')
veresedaki_handler = Resource(VeresedakiHandler, django_auth)
transaction_handler = Resource(TransactionHandler, django_auth)
relation_handler = Resource(RelationHandler, django_auth)
login_handler = Resource(LoginHandler)
logout_handler = Resource(LogoutHandler)
balance_handler = Resource(BalanceHandler, django_auth)
currency_handler = Resource(CurrencyHandler)
user_handler = Resource(UserHandler, django_auth)

urlpatterns = patterns(
    '',

    api_url(r'^balance/$', balance_handler),

    api_url(r'^relation/(?P<relation_id>\d+)/details/$',
            relation_handler, { 'details':True }
            ),
    api_url(r'^relation/(?P<relation_id>\d+)/$', relation_handler),
    api_url(r'^relation/list/$', relation_handler),

    api_url(r'^transaction/(?P<transaction_id>\d+)/$', transaction_handler),
    api_url(r'^transaction/list/$', transaction_handler),
    api_url(r'^transaction/$', transaction_handler),

    api_url(r'^currency/list/$', currency_handler),

    api_url(r'^profile/$', user_handler),

    api_url(r'login/$', login_handler),
    api_url(r'logout/$', logout_handler),
    )

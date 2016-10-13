"""Environment"""
import sys

# defining environment via command line argument --env=<ENV> (e.g.: --env=local)
# ENV in ['local', 'jenkins']

ENV = 'local'  # BY DEFAULT the environent is set to local

opts = {}
for x in sys.argv:
    if '=' in x:
        opts[x.split('=')[0]] = x.split('=')[1]
        try:
            ENV = opts['--env'].lower()
        except (KeyError, IndexError) as e:
            ENV = 'qa'

"""Web URLs"""
LOGIN_URL = 'https://core.futuresimple.com/sales/users/login'

"""API URLs"""
HOST = "https://api.getbase.com"
TOKEN_URL = "/oauth2/token"

EMAIL = 'sergey.inshev@gmail.com'
PASSWORD = "1test1"
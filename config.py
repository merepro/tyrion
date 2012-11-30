import os
  _basedir = os.path.abspath(os.path.dirname(__file__))

  DEBUG = False

  ADMINS = frozenset(['youremail@yourdomain.com'])
  SECRET_KEY = 'SecretKeyForSessionSigning'

  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'tyrion.db')
  DATABASE_CONNECT_OPTIONS = {}

  THREADS_PER_PAGE = 8

  CSRF_ENABLED=True
  CSRF_SESSION_KEY="somethingimpossibletoguess"

  RECAPTCHA_USE_SSL = False
  RECAPTCHA_PUBLIC_KEY = 'blahblahblahblahblahblahblahblahblah'
  RECAPTCHA_PRIVATE_KEY = 'blahblahblahblahblahblahprivate'
  RECAPTCHA_OPTIONS = {'theme': 'white'}

  HOST_URL = 'http://localhost:5000'
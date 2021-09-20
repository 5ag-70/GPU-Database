from google.appengine.ext import ndb

class User(ndb.Model):
    Email = ndb.StringProperty()

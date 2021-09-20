import webapp2
from google.appengine.ext import ndb


class DeviceModel(ndb.Model):

        device_name = ndb.StringProperty()
        driver_name = ndb.StringProperty()
        api_name = ndb.StringProperty()
        vendor_name = ndb.StringProperty()
        date = ndb.DateProperty()
        geometry_shader = ndb.BooleanProperty()
        teselation_shader = ndb.BooleanProperty()
        shader = ndb.BooleanProperty()
        sparse_binding = ndb.BooleanProperty()
        texture_compression = ndb.BooleanProperty()
        vertex_pipeline = ndb.BooleanProperty()

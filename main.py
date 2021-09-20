
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb
from adddriver import AddEditDriver
from device import DeviceModel
import os
from MyUser import User
from showdetails import ShowDetails
from update import Update

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=["jinja2.ext.autoescape"],
                                       autoescape=True,)


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/html"

        url = ''
        url_string = ''
        welcome = 'Hello, welcome back'
        MyUser = None
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'
            MyUser_key = ndb.Key('User', user.user_id())
            MyUser = MyUser_key.get()
            if MyUser == None:
                welcome = 'Hello, welcome to the application'
                MyUser = User(id=user.user_id())
                MyUser.put()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'

        listdriver_query = DeviceModel.query()
        if self.request.GET.get("search_driver") == "Search":

            geometry_shader = bool(self.request.GET.get("radio_geometry"))
            teselation_shader = bool(self.request.GET.get("radio_teselation_shader"))
            shader = bool(self.request.GET.get("radio_shader_int"))
            sparse_binding = bool(self.request.GET.get("radio_sparse_blinding"))
            texture_compression = bool(self.request.GET.get("radio_texture"))
            vertex_pipeline = bool(self.request.GET.get("radio_vertex"))

            listdriver_query = DeviceModel.query(ndb.AND(DeviceModel.geometry_shader == geometry_shader, DeviceModel.teselation_shader == teselation_shader, DeviceModel.shader == shader,DeviceModel.sparse_binding == sparse_binding,DeviceModel.texture_compression == texture_compression,DeviceModel.vertex_pipeline == vertex_pipeline)).fetch()

        else:

            geometry_shader = False
            teselation_shader = False
            shader = False
            sparse_binding = False
            texture_compression = False
            vertex_pipeline = False
            listdriver_query = DeviceModel.query().fetch()

        template_values = {
            "list_drivers": listdriver_query,
            "radio_geometry" : geometry_shader,
            "radio_teselation_shader": teselation_shader,
            "radio_shader_int": shader,
            "radio_sparse_blinding": sparse_binding,
            "radio_texture": texture_compression,
            "radio_vertex" : vertex_pipeline,
            'url' : url,
            'url_string' : url_string,
            'user' : user,
            'welcome' : welcome,
            'MyUser' : MyUser
        }

        template = JINJA_ENVIRONMENT.get_template("main.html")
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/showdetails", ShowDetails),
    ("/adddriver",AddEditDriver),
    ("/update",Update),
], debug=True)

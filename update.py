import webapp2
import jinja2
from google.appengine.ext import ndb
import os
from device import DeviceModel
from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True
)

class Update(webapp2.RequestHandler):
    def get(self):
        edit= False
        self.response.headers['Content-Type'] = 'text/html'
        name = self.request.GET.get('value')
        done = self.request.GET.get('done')

        print(name)
        device_key=ndb.Key('DeviceModel', name)
        print(device_key)
        device=device_key.get()
        print  (device)
        action = self.request.get('edit')
        if action=="Edit":
            edit= True
        message = ''
        if done == 'su':
            message = 'GPU data updated'

        template_values ={
            'edit': edit,
            'list': device,
            'Message' : message
        }
        template = JINJA_ENVIRONMENT.get_template('update.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'


        devicename = self.request.get('value')
        print devicename
        devicekey = ndb.Key('DeviceModel', devicename)
        devisedata = devicekey.get()
        devisedata.driver_name = self.request.get('drivername')
        devisedata.driver_name = self.request.get('drivername')
        devisedata.api_name = self.request.get('apiname')
        devisedata.vendor_name = self.request.get('vendorname')
        devisedata.date = datetime.strptime(self.request.get('date'), '%Y-%m-%d')

        if self.request.get('radio_geometry') == 'on':
            devisedata.geometry_shader = True
        else:
            devisedata.geometry_shader = False

        if self.request.get('radio_teselation_shader') == 'on':
            devisedata.teselation_shader = True
        else:
            devisedata.teselation_shader = False

        if self.request.get('radio_shader_int') == 'on':
            devisedata.shader = True
        else:
            devisedata.shader = False

        if self.request.get('radio_sparse_blinding') == 'on':
            devisedata.sparse_binding = True
        else:
            devisedata.sparse_binding = False

        if self.request.get('radio_texture') == 'on':
            devisedata.texture_compression = True
        else:
            devisedata.texture_compression = False

        if self.request.get('radio_vertex') == 'on':
            devisedata.vertex_pipeline = True
        else:
            devisedata.vertex_pipeline = False



        devisedata.put()



        self.redirect('/update?value='+devicename+'&done=su')

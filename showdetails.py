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

class ShowDetails(webapp2.RequestHandler):
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
            message = 'Success'

        template_values ={
            'edit': edit,
            'list': device,
            'Message' : message
        }
        template = JINJA_ENVIRONMENT.get_template('showdetails.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'


        devicename = self.request.get('value')




        self.redirect('/update?value='+devicename)

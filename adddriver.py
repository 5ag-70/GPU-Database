import webapp2
import os
import jinja2
from datetime import datetime
from google.appengine.ext import ndb
from device import DeviceModel


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True
)

class AddEditDriver(webapp2.RedirectHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/html"

        list_all = DeviceModel.query().fetch()
        print(len(list_all))
        template_values = {
            'list_all': list_all
        }
        template = JINJA_ENVIRONMENT.get_template("adddriver.html")
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers["Content-Type"] = "text/html"

        device_name = self.request.get("device_name")
        driver_name = self.request.get("driver_name")
        api_name = self.request.get("api_name")
        vendor_name = self.request.get("vendor_name")
        date_raw = self.request.get("issue_date")
        date1 = datetime.strptime(date_raw, "%Y-%m-%d")
        geometry_shader = bool(self.request.get("geometry_shader"))
        teselation_shader = bool(self.request.get("tesse_shader"))
        shader = bool(self.request.get("shader_int"))
        sparse_binding = bool(self.request.get("sparse_binding"))
        texture_compression = bool(self.request.get("texture_compression"))
        vertex_pipeline = bool(self.request.get("vertex_pipeline"))
        if self.request.get("add_driver") == "Submit":
            device_key=ndb.Key('DeviceModel',device_name)
            device=device_key.get()


            if device == None:
                device = DeviceModel(id = device_name)
                device.device_name=device_name
                device.driver_name=driver_name
                device.api_name=api_name
                device.vendor_name=vendor_name
                device.date=date1
                device.geometry_shader=geometry_shader
                device.teselation_shader=teselation_shader
                device.shader=shader
                device.sparse_binding=sparse_binding
                device.texture_compression=texture_compression
                device.vertex_pipeline=vertex_pipeline
                device.put()

                self.redirect("/")

            else:
                list_all = DeviceModel.query().fetch()
                print(len(list_all))
                template_values = {
                    'list_all': list_all,
                    'Message': 'Device Alrady In the System'
                }
                template = JINJA_ENVIRONMENT.get_template("adddriver.html")
                self.response.write(template.render(template_values))


        # elif self.request.get("add_driver") == "Update Driver":
        #
        #     selected_id = self.request.get("driver_id")
        #     selected_driver_key = ndb.Key("DeviceModel", int(selected_id))
        #     selected_driver = selected_driver_key.get()
        #
        #     selected_driver.device_name = self.request.get("device_name")
        #     selected_driver.driver_name = self.request.get("driver_name")
        #     selected_driver.api_name = self.request.get("api_name")
        #     selected_driver.vendor_name = self.request.get("vendor_name")
        #
        #     selected_driver.geometry_shader = bool(self.request.get("radio_geometry"))
        #     selected_driver.teselation_shader = bool(self.request.get("radio_teselation_shader"))
        #     selected_driver.shader = bool(self.request.get("radio_shader_int"))
        #     selected_driver.sparse_binding = bool(self.request.get("radio_sparse_blinding"))
        #     selected_driver.texture_compression = bool(self.request.get("radio_texture"))
        #     selected_driver.vertex_pipeline = bool(self.request.get("radio_vertex"))


            # selected_driver.put()

        # listdriver_query = DeviceModel.query().fetch()



        if self.request.get("cancel"):

            self.redirect("/")

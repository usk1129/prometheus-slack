import falcon
from falcon_prometheus import PrometheusMiddleware

class HelloResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("Hello, World!")

class Page2Resource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("This is the second page!")

prometheus = PrometheusMiddleware()
app = falcon.API(middleware=prometheus)

hello = HelloResource()
page2 = Page2Resource()

app.add_route('/', hello)
app.add_route('/page2', page2)
app.add_route('/metrics', prometheus)

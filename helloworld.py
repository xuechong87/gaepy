import webapp2

class HellowWorld(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('this is say')

app = webapp2.WSGIApplication([('/', HellowWorld)])
'''
Created on 2013-5-30

@author: xuechong
'''
import webapp2

class Say(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('deploy ok!')

app = webapp2.WSGIApplication([('/deploy', Say)])
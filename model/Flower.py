# coding: utf-8
'''
Created on 2013-7-4

@author: xuechong
'''

import logging
from google.appengine.ext import db
from google.appengine.ext import search

class Flower(search.SearchableModel):
    
    name = db.StringProperty()
    content = db.StringProperty()
    
    def description(self):
        result = self.name + unicode(":\n","utf-8")\
             + self.content + unicode("\n","utf-8")
        return result
    @classmethod
    def SearchableProperties(cls):
        return [['name'],search.ALL_PROPERTIES]
    
    
def save(name,content):
    flower = Flower()
    flower._key_name = name
    flower.content = content
    flower.name = name
    flower.put()

    
def findByName(searchStr):
    query = Flower.all()
    logging.debug("search flower" + searchStr)
    query.search(searchStr.decode("utf-8"), properties=['name'])
    return query.fetch(20)

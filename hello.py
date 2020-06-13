#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return """
        <html>
        <head><title>Hello World</title></head>
        <body>
        <h1>Hello World desde Cherry!</h1>
        </body>
        </html>"""
    
    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)


cherrypy.config.update({'server.socket_port': 8090,
                        'engine.autoreload.on': False,
                        'log.access_file': './access.log',
                        'log.error_file': './error.log'})
cherrypy.quickstart(Root())
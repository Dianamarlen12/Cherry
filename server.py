#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import cherrypy

config = {
    'global' : {
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080
    }
}


class App:

    @cherrypy.expose
    def upload(self, ufile):
        # Either save the file to the directory where server.py is
        # or save the file to a given path:
        # upload_path = '/path/to/project/data/'
        upload_path = os.path.dirname(__file__)

        # Save the file to a predefined filename
        # or use the filename sent by the client:
        # upload_filename = ufile.filename
        upload_filename = 'saved.txt'

        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        out = '''
File received.
Filename: {}
Length: {}
Mime-type: {}
''' .format(ufile.filename, size, ufile.content_type, data)
        return out


if __name__ == '__main__':
    cherrypy.quickstart(App(), '/', config)
 
webpage.html
<form method="post" action="http://127.0.0.1:8080/upload" enctype="multipart/form-data">
    <input type="file" name="ufile" />
    <input type="submit" />
</form>
 
cli.py
Este ejemplo requiere un paquete de solicitudes de Python , sin embargo, el archivo se puede enviar al servidor en Python simple.

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests

url = 'http://127.0.0.1:8080/upload'
files = {'ufile': open('file.txt', 'rb')}

r = requests.post(url, files=files)

print(r)
print(r.text)
import os
import sys

import pysc



    
if __name__ == '__main__':
    service_name = 'testing'
    script_path = os.path.join(
        os.path.dirname(__file__), 'xmlrpc_server.py'
    )
    pysc.create(
        service_name=service_name,
        cmd=[sys.executable, script_path]
    )
    pysc.start(service_name)
    #app.run(host = '127.0.0.1',port=9005)  

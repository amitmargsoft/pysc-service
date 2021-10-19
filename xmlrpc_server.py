from xmlrpc.server import SimpleXMLRPCServer
from pysc import event_stop
from flask import Flask, render_template, session, copy_current_request_context



from werkzeug.serving import make_server

class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        log.info('starting server')
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()



class TestServer:

    def echo(self, msg):
        return msg


if __name__ == '__main__':
    #server = SimpleXMLRPCServer(('127.0.0.1', 9001))
    global server
    app = flask.Flask('myapp')
    server = ServerThread(app)
    

    @event_stop
    def stop():
        server.shutdown()

    server.register_instance(ServerThread(app))
    server.run()
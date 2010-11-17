from mongrel2_wsgi import server

import urllib2
from eventlet import spawn_n, sleep

from wsgiref.simple_server import demo_app
from wsgiref.validate import validator

import logging
log = logging.getLogger(__name__)

sender_id = 'ee3f2ae1-37e1-4866-a9bc-90cf5db31b9d'
sub_addr = 'tcp://127.0.0.1:9999'
pub_addr = 'tcp://127.0.0.1:9998'

def test_server():
    import logging
    logging.basicConfig(level=logging.DEBUG)

    request_data = """ee3f2ae1-37e1-4866-a9bc-90cf5db31b9d 45965 / 203:{"PATH":"/","user-agent":"Python-urllib/2.6","host":"localhost:6767","x-forwarded-for":"::1","connection":"close","accept-encoding":"identity","METHOD":"GET","VERSION":"HTTP/1.1","URI":"/","PATTERN":"/"},0:,"""

    class MockRecv(object):
        def recv(self):
            self.recv = None
            return request_data

    class MockSend(list):
        def send(self, data):
            self.append(data)

    app = validator(demo_app)

    s = server.Mongrel2WSGIServer(
            app, 
            sender_id=sender_id, 
            sub_addr=sub_addr,
            pub_addr=pub_addr
            )
    s.bind()
    s.ready = True
    s.reqs = MockRecv()
    s.resp = MockSend()
    s.tick()
    sleep(0.1) 
    log.debug(s.resp)


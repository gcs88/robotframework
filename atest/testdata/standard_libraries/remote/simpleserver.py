import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer

from remoteserver import announce_port


class SimpleServer(SimpleXMLRPCServer):

    def __init__(self, port=8270, port_file=None):
        SimpleXMLRPCServer.__init__(self, ('127.0.0.1', int(port)))
        self.register_function(self.get_keyword_names)
        self.register_function(self.run_keyword)
        announce_port(self.socket, port_file)
        self.serve_forever()

    def get_keyword_names(self):
        return ['Passing', 'Failing', 'Traceback', 'Returning', 'Logging']

    def run_keyword(self, name, args):
        if name == 'Passing':
            return {'status': 'PASS'}
        if name == 'Failing':
            return {'status': 'FAIL', 'error': ' '.join(args)}
        if name == 'Traceback':
            return {'status': 'FAIL', 'traceback': ' '.join(args)}
        if name == 'Returning':
            return {'status': 'PASS', 'return': ' '.join(args)}
        if name == 'Logging':
            return {'status': 'PASS', 'output': '\n'.join(args)}


if __name__ == '__main__':
    SimpleServer(*sys.argv[1:])

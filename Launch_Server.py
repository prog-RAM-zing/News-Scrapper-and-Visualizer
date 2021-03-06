
import BaseHTTPServer
import SimpleHTTPServer
from socket import error
import  SocketServer, os, subprocess,shlex
import webbrowser

class ThreadingSimpleServer(SocketServer.ThreadingMixIn,
                   BaseHTTPServer.HTTPServer):
    pass

home_path = os.getenv('HOME') + '/'
os.chdir(home_path + '/path/to/server/directory/')
port = 9000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


try:
    httpd = SocketServer.TCPServer(("", port), Handler)
    print "Serving at port : ", port
    httpd.serve_forever()
except error as e:
    if 'Address already in use' in e.message:
        p= subprocess.Popen(shlex.split('lsof -i :%s' %str(port)),stdout=subprocess.PIPE)
        op,err = p.communicate()
        if op:
            print 'Processes using port %d : \n' %port, op
            quit()



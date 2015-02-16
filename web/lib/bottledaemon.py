import os, argparse, signal, daemon, lockfile, bottle, json
from bottle import Bottle, get, run, ServerAdapter
from contextlib import contextmanager

config_file_dir = os.path.dirname(os.path.abspath(__file__)) + "/config.json"
config = json.loads(open(config_file_dir).read())


# Custom SSL serversocket
class SSLWSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        import ssl
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        srv = make_server(self.host, self.port, handler, **self.options)
        srv.socket = ssl.wrap_socket (
         srv.socket,
         certfile=config["paths"]["file_ssl_cert"],
         server_side=True)
        srv.serve_forever()
# End custom SSL serversocket


@contextmanager
def __locked_pidfile(filename):
    # Acquire the lockfile
    lock = lockfile.FileLock(filename)
    lock.acquire(-1)
    
    # Write out our pid
    realfile = open(filename, "w")
    realfile.write(str(os.getpid()))
    realfile.close()

    # Yield to the daemon
    yield
    
    # Cleanup after ourselves
    os.remove(filename)
    lock.release()


def daemon_run(host="0.0.0.0", port="80", pidfile=None, logfile=None):
    """
    Get the bottle 'run' function running in the background as a daemonized
    process. 

    :host: The host interface to listen for connections on. Enter 0.0.0.0
           to listen on all interfaces. Defaults to localhost.
    :port: The host port to listen on. Defaults to 8080.
    :pidfile: The file to use as the process id file. Defaults to "bottle.pid"
    :logfile: The file to log stdout and stderr from bottle to. Defaults to "bottle.log"

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["start", "stop"])
    args = parser.parse_args()

    if pidfile is None:
        pidfile = os.path.join(
            os.getcwd(),
            "pid/bottle.pid"
        )
    
    if logfile is None:
        logfile = os.path.join(
            os.getcwd(),
            config["paths"]["dir_webserver_root"] + 'log/bottle.log'
        )

    if args.action == "start":
        log = open(logfile,"w+")
        context = daemon.DaemonContext( 
            pidfile=__locked_pidfile(pidfile),
            stdout=log,
            stderr=log
        )
        print
        print ">>>> Security Monitor web started on 0.0.0.0:" + config["paths"]["server_port"] + "."
        print
        
        with context:
            # If you don't want SSL, please enable the following line and disable the next 2 lines.
            # bottle.run(host=host, port=port)
            srv = SSLWSGIRefServer(host="0.0.0.0", port=config["paths"]["server_port"])
            run(server=srv)
    if args.action == "stop":
        with open(pidfile,"r") as p:
            pid = int(p.read())
            os.kill(pid, signal.SIGTERM)
        print
        print ">>>> Security Monitor web stopped."
        print

if __name__ == "__main__":
    daemon_run()

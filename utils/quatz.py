import zmq, time, thread, threading, json, os, subprocess, signal
from settings import QUATZ_ADDRESS

def doorbell_mode():
    web_mode(8, ['http://127.0.0.1/~MAT/ipcamimages/index.html'])
    subprocess.call('/usr/local/bin/play /Users/mat/src/chandelier_infohub/static/69385__guitarguy1985__doorbell2.wav', shell=True)
    time.sleep(15)
    web_mode(4, ['http://127.0.0.1:8000/processing/sketch/dorkbot.pde'])

def open_quatz():
    if not quatz_running_p()[0]:
        subprocess.Popen("/Users/%s/src/chandelier_displayer/build/Release/Quatz.app/Contents/MacOS/Quatz" % os.environ['USER'])

def quit_quatz():
    runningp, pids = quatz_running_p()
    if runningp:
        for pid in pids:
            print pid
            os.kill(int(pid), signal.SIGTERM)

def test_quatz():
    open_quatz()
    time.sleep(2)
    quit_quatz()

def quatz_running_p():
    ps_output = subprocess.Popen('ps auxw | grep [Q]uatz', shell=True, stdout=subprocess.PIPE).stdout.read()
    runningp = (ps_output != '')
    pids = []
    if runningp:
        ps_lines = ps_output.split('\n')
        for l in ps_lines:
            if len(l) > 0:
                comps = l.split()
                if len(comps) > 1:
                    pids.append(comps[1])
    return runningp, pids

def web_mode(views, urls):
    """Starts the web mode on the chandelier.

    Args:
        views: An integer that specifies how many web views to load.
        urls: An array with web addresses.

    Returns:
        None

    If there are less urls than views, the urls will be repeated.
    This way you can have the same web page repeated, or two web
    pages alternating.
    """
    __set_screen_mode('web', urls=urls, views=views)


def quartz_mode(file):
    """Starts the quartz mode on the chandelier.

    Args:
        file: A string that points to a file on disk.

    Returns:
        None
    """
    __set_screen_mode('quartz', file=file)


def __set_screen_mode(mode, **kargs):
    d = {'mode': mode,
         'arguments': kargs}
    __Messenger.call_service(QUATZ_ADDRESS, d)


class __Messenger():

    ctxs = {}
    resolver = False
    initialized = False

    @classmethod
    def call_service(cls, address, data, timeout=3600):
        t = threading.currentThread()
        if t in cls.ctxs:
            tctx = cls.ctxs[t]
            ctx = tctx['ctx']
            socket = tctx['socket']
        else:
            # create new context for thread
            ctx = zmq.Context()
            socket = False
            tctx = {'ctx': ctx, 'socket': socket}
            cls.ctxs[t] = tctx
            # clean up contexts for threads that are not running anymore
            for thr in cls.ctxs.keys():
                if not thr.isAlive():
                    try:
                        del cls.ctxs[thr]
                    except:
                        pass
        if not (socket and not socket.closed):
            socket = ctx.socket(zmq.REQ)
            tctx['socket'] = socket
            socket.connect(address)
            time.sleep(0.5) # allow socket to connect

        # socket is set up, let's use s as a shorthand
        s = socket
        poller = zmq.Poller()
        poller.register(s, zmq.POLLIN|zmq.POLLOUT)
        # sending
        try:
            # relying on correct behaviour of zeromq's poll here, needs zeromq 2.1.6
            socks = dict(poller.poll(timeout*1000)) # this shouldn't time out!
            assert socks.has_key(s)
            assert socks[s] == zmq.POLLOUT
            s.send_unicode(json.dumps(data))
            # receiving
            try:
                socks = dict(poller.poll(timeout*1000))
                assert socks.has_key(s)
                assert socks[s] == zmq.POLLIN
                msg = s.recv_unicode()
            except AssertionError, e:
                s.close()
                error = 'Could not receive response from %s (%s).' % (address, str(e))
                raise Exception(error)
        except AssertionError, e:
            s.close()
            error = 'Could not send message to %s.' % address
            raise Exception(error)

        if msg == '':
            return None

        msg_obj = json.loads(msg)
        if isinstance(msg_obj, dict) and 'exception' in msg_obj and msg_obj['exception'] == True:
            raise Exception('Received an exception from service %s: \n\t%s' % (address, msg_obj['info']))
        else:
            return msg_obj


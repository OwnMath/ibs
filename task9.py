import threading
import time


def _10to1(interval, name):
    print(" '%s' counter just started!\n" % name)
    for x in range(10, 0, -1):
        print(" '%s' counter just said %s \n" % (name, x))
        time.sleep(interval)
    print(" '%s' counter just ended!\n" % name)


t = threading.Thread(target=_10to1, args=(1, "first"))
t.daemon = True
d = threading.Thread(target=_10to1, args=(1, "second"))
d.daemon = True

t.start()
d.start()

t.join()
d.join()

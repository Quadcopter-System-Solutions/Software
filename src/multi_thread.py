""" Classes for managing threading in communication_server """

import threading
import time


class MultiThread():
    """ Class for keeping track of threads """
    def __init__(self):
        self.threads = []
        self.count = 0

    def create_thread(self, function, name='', parameters=None):
        """ Creates a SingleThread subclassed from Thread """
        thread = SingleThread(self.count, name, function, parameters)
        self.threads.append(thread)
        self.count += 1
        return thread

    def create_test_thread(self):
        """ Creates a test thread for quick creations of threads """
        return self.create_thread(
            function=test_function,
            name='test',
            parameters={
                'delay': 1,
                'counter': 100,
                'thread_id': f'thread{self.count}'
            }
        )

    def get_thread(self, name):
        """ Returns a thread serached by name """
        for thread in self.threads:
            if name == thread.name:
                return thread

        return None


class SingleThread(threading.Thread):
    """
    "    SingleThread is subclassed from thread,
    "    keeps and ID, name, and the function with parameters
    """
    def __init__(self, thread_id, name, function, parameters=None):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.function = function
        self.parameters = parameters

    def run(self):
        """ Overrides the run function from Thread """
        if not self.parameters:
            self.function()
        else:
            self.function(self.parameters)


def test_function(data):
    """ MultiThread creates a test thread using this class """
    delay = data['delay']
    counter = data['counter']
    thread_id = data['thread_id']

    while counter:
        time.sleep(delay)
        print('%s: %s' % (thread_id, time.ctime(time.time())))
        counter -= 1

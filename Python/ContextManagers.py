with open('notes.txt', 'w') as f:
    f.write('some todo...')

f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()


from threading import Lock
lock = Lock()

# error-prone:
lock.acquire()
# do stuff
# lock should always be released!
lock.release()

# Better:
#with lock:
        #do stuff


class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')



class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value)
        print('exit')

# No exception
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
print('continuing...')

print()

# Exception is raised, but the file can still be closed
with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')


class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
        print('exit')
        return True


with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')


class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
        print('exit')
        return True


with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')
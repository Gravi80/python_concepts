import sys

# The sys.meta_path further extends the sources of potential imports by
# allowing a finder to be searched before the regular sys.path is scanned.
print(sys.meta_path)


# https://pymotw.com/2/sys/imports.html

class ImportModuleHook(object):
    def __init__(self):
        pass

    def find_module(self, fullname, path=None):
        print("fullname={0}".format(fullname))
        print("path={0}".format(path))


sys.meta_path.insert(0, ImportModuleHook())
print(sys.meta_path)
import yaml

yaml.Event()
del sys.meta_path[0]
print(sys.meta_path)
print("\n\n################## Call Stack ######################")


def hook(frame, event, *_):
    print(event, frame.f_code.co_name)


sys.setprofile(hook)


def func1():
    return 'func1'


def func2():
    return func1()


func2()

print("\n\n################## Call Stack ######################")

# https://www.youtube.com/watch?v=mr2SE_drU5o
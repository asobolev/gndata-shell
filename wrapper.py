import os, sys
import uuid


class Wrapper():
    """
    Wrapper Class that implements basic operations.
    Implements proxy behaviour for <git> by default. 
    """

    @classmethod
    def run(cls):
        params = [a for a in sys.argv[1:]]

        if len(params) > 0 and hasattr(cls, params[0]):
            func = getattr(cls, params[0])
            func(params[1:])

        else:
            default = (" ").join(params)
            os.system("git %s" % default)

    @classmethod
    def init(cls, params):
        os.system("git init")

        if not os.path.exists(".gndata"):
            os.mkdir(".gndata")

            with open(".gndata/data", "w") as f:
                pass

            with open(".gndata/config", "w") as f:
                #f.writelines("location_id=%s\n" % rep_id)
                f.writelines("nondata_max=1048576\n")

            os.system("git add .gndata")
            os.system("git commit -a -m initial")

        rep_id = params[0] if len(params) > 1 else cls._id()
        os.system("git annex init %s" % rep_id)

    @classmethod
    def add(cls, params):
        with open(".gndata/data", "r") as f:
            for line in f.readlines():
                os.system("git annex add %s" % line) # FIXME works only with .

        os.system("git add %s" % params[0])

    @classmethod
    def sync(cls, params):
        proxy = " ".join(params) if len(params) > 0 else ""
        os.system("git annex sync %s" % proxy) # FIXME --content?!

    @classmethod
    def clone(cls, params):
        proxy = " ".join(params) if len(params) > 0 else ""

        os.system("git clone %s" % proxy)

        parts = params[0].split("/")
        dir_name = parts[len(parts) - 1].replace(".git", "")
        os.system("cd %s" % dir_name) # FIXME any other way for that?

        rep_id = params[1] if len(params) > 1 else cls._id()
        os.system("git annex init %s" % rep_id)

        os.system("cd ..")

    @classmethod
    def _id(cls):
        return uuid.uuid1().hex[:10]




if __name__ == '__main__':
    Wrapper().run()



"""
parts = params[0].split("/")
dir_name = parts[len(parts) - 1].replace(".git", "")
os.system("cd %s" % dir_name) # FIXME any other way for that?
os.system("cd ..")

"""

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
        if len(params) > 0 and params[0] == "--all":
            os.system("git annex sync")
            os.system("git annex copy . --to %s" % cls._get_remote_id())
        else:
            proxy = " ".join(params) if len(params) > 0 else ""
            os.system("git annex sync %s" % proxy)

    @classmethod
    def clone(cls, params):
        proxy = " ".join(params) if len(params) > 0 else ""
        rep_id = params[1] if len(params) > 1 else cls._id()

        os.system("git clone %s" % proxy)

        parts = params[0].split("/")
        dir_name = parts[len(parts) - 1].replace(".git", "")

        curr_dir = os.getcwd()
        proj_dir = os.path.join(curr_dir, dir_name)
        
        os.chdir(proj_dir) # FIXME any other way for that?

        os.system("git annex init %s" % rep_id)
        os.system("git checkout master") # FIXME why it's not master by default?

        os.chdir(curr_dir)

    @classmethod
    def get(cls):
        proxy = " ".join(params) if len(params) > 0 else ""
        os.system("git annex get %s" % proxy)

    @classmethod
    def _id(cls):
        return uuid.uuid1().hex[:10]

    @classmethod
    def _get_remote_id(cls):
        with open(".git/config", "r") as f:
            for line in f.readlines():
                if line.find("annex-uuid") > 0:
                    return line.split("= ")[1]




if __name__ == '__main__':
    Wrapper().run()




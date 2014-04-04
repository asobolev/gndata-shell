import os, sys
import uuid
import dummy


class Wrapper():
    """
    Wrapper Class that implements basic operations.
    Implements proxy behaviour for <git> by default. 
    
    It's all fake.
    """

    @classmethod
    def run(cls):
        params = [a for a in sys.argv[1:]]

        if len(params) > 0 and hasattr(cls, params[0]):
            func = getattr(cls, params[0])
            func(params[1:])

        else:
            os.system("git %s" % " ".join(params))

    @classmethod
    def init(cls, params):
        os.system("git init %s" % " ".join(params))
        
        if "--bare" in params:
            os.chdir(params[params.index("--bare") + 1])

        else:
            cls._init_gndata()
            
        os.system("git annex init %s" % cls._id())

    @classmethod
    def add(cls, params):
        with open(".gndata/data", "r") as f:
            for line in f.readlines():
                os.system("git annex add %s" % line) # FIXME works only with .

        os.system("git add %s" % params[0])

    @classmethod
    def pushdata(cls, params):
        os.system("git annex copy . --to %s" % cls._get_remote_id())

    @classmethod
    def pulldata(cls, params):
        os.system("git annex get .")

    @classmethod
    def sync(cls, params):
        if len(params) > 0 and params[0] == "--all":
            os.system("git annex sync")
            os.system("git annex copy . --to %s" % cls._get_remote_id())
        else:
            os.system("git annex sync %s" % " ".join(params))

    @classmethod
    def clone(cls, params):
        os.system("git clone %s" % " ".join(params))

        dir_name = os.path.basename(os.path.normpath(params[0]))
        dir_name = dir_name.replace(".git", "")

        curr_dir = os.getcwd()
        os.chdir( os.path.join(curr_dir, dir_name) )

        cls._init_gndata()
        
        os.system("git annex init %s" % cls._id())
        #os.system("git annex sync")
        #os.system("git annex get .")

    @classmethod
    def get(cls, params):
        os.system("git annex get %s" % " ".join(params))

    @classmethod
    def create_dummy(cls, params):
        dummy.create(create_root = False)

    #--- private methods -------------------------------------------------------
    
    @classmethod
    def _id(cls):
        return uuid.uuid1().hex[:10]

    @classmethod
    def _get_remote_id(cls):
        with open(".git/config", "r") as f:
            for line in f.readlines():
                if line.find("annex-uuid") > 0:
                    return line.split("= ")[1]
         
    @classmethod           
    def _init_gndata(cls, gpath=".gndata"):
        if not os.path.exists(gpath):
            os.mkdir(gpath)

            with open(os.path.join(gpath, "data"), "w") as f:
                pass

            with open(os.path.join(gpath, "config"), "w") as f:
                f.writelines("nondata_max=1048576\n")
                
            os.system("git add %s" % gpath)
            os.system("git commit -a -m initial")




if __name__ == '__main__':
    Wrapper().run()




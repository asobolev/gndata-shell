import os, sys
import uuid
import dummy



class Wrapper():
    """
    Wrapper Class that implements basic operations.
    Implements proxy behaviour for <git> by default. 
    
    It's all fake.
    """
    
    git = "agit" # a version of git shipped with new version of git-annex
    ann = "annex"

    @classmethod
    def run(cls):
        params = [a for a in sys.argv[1:]]

        if len(params) > 0 and hasattr(cls, params[0]):
            func = getattr(cls, params[0])
            func(params[1:])

        else:
            os.system("%s %s" % (cls.git, " ".join(params)))

    @classmethod
    def init(cls, params):
        os.system("%s init %s" % (cls.git, " ".join(params)))
        
        if "--bare" in params:
            os.chdir(params[params.index("--bare") + 1])

        else:
            cls._init_gndata()
            
        os.system("%s init %s" % (cls.ann, cls._id()))

    @classmethod
    def add(cls, params):
        with open(".gndata/data", "r") as f:
            for line in f.readlines():
                os.system("%s add %s" % (cls.ann, line)) # works only with .

        os.system("%s add %s" % (cls.git, params[0]))

    @classmethod
    def pushdata(cls, params):
        os.system("%s copy . --to %s" % (cls.ann, cls._get_remote_id()))

    @classmethod
    def pulldata(cls, params):
        os.system("%s get ." % cls.ann)

    @classmethod
    def sync(cls, params):
        os.system("%s sync %s" % (cls.ann, " ".join(params)))

    @classmethod
    def clone(cls, params):
        os.system("%s clone %s" % (cls.git, " ".join(params)))

        dir_name = os.path.basename(os.path.normpath(params[0]))
        dir_name = dir_name.replace(".git", "")

        curr_dir = os.getcwd()
        os.chdir( os.path.join(curr_dir, dir_name) )

        cls._init_gndata()
        
        os.system("%s init %s" % (cls.ann, cls._id()))

    @classmethod
    def get(cls, params):
        os.system("%s get %s" % (cls.ann, " ".join(params)))

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




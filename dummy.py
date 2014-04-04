import os

def create(create_root = True):
    """ creation of the test folder structure """

    def create_datafile(where, index=1, trial=1):
        with open(os.path.join(where, "datafile%d.dat" % trial), "w") as f:
            f.writelines("data from day %d trial %d" % (index, trial))

    def create_metafile(where, index=1, trial=1):
        with open(os.path.join(where, "metadata%d.odml" % trial), "w") as f:
            f.writelines("metadata from day %d trial %d" % (index, trial))

    def create_analysis(where, index=1):
        with open(os.path.join(where, "analysis%d.py" % index), "w") as f:
            f.writelines("some analysis script %d" % index)

    root_name = "myproject"
    if create_root and not os.path.exists(root_name):
        os.mkdir(root_name)
        os.chdir(root_name)

    where = "scripts"
    os.mkdir(where)
    for i in range(3):
        create_analysis(where, i)

    where = "experiments"
    os.mkdir(where)

    for i in range(4):
        local = os.path.join(where, "day%d" % i)
        os.mkdir(local)
        
        for j in range(5):
            create_datafile(local, index=i, trial=j)

        for j in range(2):
            create_metafile(local, index=i, trial=j)
    

if __name__ == '__main__':
    create()

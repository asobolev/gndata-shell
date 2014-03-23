"""
creation of the test folder structure
"""
import os

if not os.path.exists("my_project"):
    os.mkdir("my_project")

# some analysis scripts
sfolder = "my_project/scripts"
os.mkdir(sfolder)
for i in range(3):
    with open("%s/analysis_%d.py" % (sfolder, i), "w") as f:
        f.writelines("foo %d" % i)

# some experiments with data and metadata
dfolder = "my_project/experiments"
os.mkdir(dfolder)
for i in range(4):
    os.mkdir("%s/day_%d" % (dfolder, i))
    for j in range(5):
        with open("%s/day_%d/datafile%d.dat" % (dfolder, i, j), "w") as f:
            f.writelines("data from day %d trial %d" % (i, j))
    for j in range(2):
        with open("%s/day_%d/metadata%d.odml" % (dfolder, i, j), "w") as f:
            f.writelines("metadata from day %d trial %d" % (i, j))


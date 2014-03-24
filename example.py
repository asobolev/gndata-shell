import os, sys

# init on the remote

os.system("ssh andrey@test.g-node.org")
os.system("mkdir ~/my_project")
os.system("cd ~/my_project")
os.system("gndata init")

# local init

os.system("cd ~/my_project")
os.system("gndata init")

# adding a remote

location = "ssh://andrey@test.g-node.org/home/andrey/my_project/"
os.system("gndata remote add gnode %s" % location)
os.system("gndata pull")

# manually: tell gndata which files are big

os.system('echo "*.dat" > .gndata/data')

# add files to commit

os.system("gndata add .")

# commit

os.system("gndata commit -a -m added")

# sync

os.system("gndata sync")

# adding/modyfying local files

os.system("echo foo > experiments/day_1/datafile123.dat")
os.system("mv scripts/analysis_0.py scripts/analysis_5.py")
os.system("gndata status")

# sync new files

os.system("gndata add .")
os.system("gndata commit -a -m new")
os.system("gndata sync")

# clone in a new place

os.system("cd /tmp")
os.system("gndata clone %s" % location)
os.system("tree")
os.system("gndata sync")




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

location = "ssh://andrey@test.g-node.org/home/andrey/my_project"
os.system("gndata remote add gnode %s" % location)
os.system("gndata pull gnode master")

# manually: tell gndata which files are big

os.system('echo "*.dat" > .gndata/data')

# add files to commit

os.system("gndata add .")

# commit

os.system("gndata commit -a -m added")

# sync

os.system("gndata sync") # git annex copy . --to 3cf6a6ec-b355-11e3-a41a-67632d7be958

# adding/modyfying local files

os.system("echo foo > experiments/day_1/datafile123.dat")
os.system("mv scripts/analysis_0.py scripts/analysis_5.py")
os.system("gndata status")

# sync new files

os.system("gndata add .")
os.system("gndata commit -a -m changed")
os.system("gndata sync")

# clone in a new place

os.system("cd /tmp")
os.system("gndata clone %s" % location)
os.system("tree")
os.system("gndata sync")




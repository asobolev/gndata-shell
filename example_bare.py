import os, sys

# init on the remote

os.system("ssh andrey@test.g-node.org")
os.system("gndata init --bare myproject.git")

# local init

location = "ssh://andrey@test.g-node.org/home/andrey/myproject.git"
os.system("gndata clone %s" % location)

# create dummy files

os.system("cd myproject")
os.system("gndata create_dummy")

# manually: tell gndata which files NOT to check in

os.system('echo "*.dat" > .gndata/data')
os.system("gndata add .")

# add and commit

os.system("gndata commit -a -m added")

# sync

os.system("gndata sync --content")

# adding/modyfying local files

os.system("echo foo > experiments/day_1/datafile123.dat")
os.system("gndata status")

# sync new files

os.system("gndata add .")
os.system("gndata commit -a -m changed")
os.system("gndata sync --content")

# clone in a new place

os.system("cd /tmp")
os.system("gndata clone %s" % location) # note does not fetch data

# fetch datafiles

os.system("gndata get .") # does fetch the data

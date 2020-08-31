import sys
import os
import shutil
import subprocess

name = sys.argv[1]

# create tmux pane
with open('atcoder.yml') as ein, open(f'{name}.yml', 'w') as out:
    for line in ein:
        line = line.replace('{}', name)
        out.write(line)

myenv = os.environ.copy()
myenv['ATCODER'] = name
subprocess.check_call(['tmuxp', 'load', f'{name}.yml'], env=myenv)

os.remove(f'{name}.yml')

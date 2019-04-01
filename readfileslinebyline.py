file='pycharm.txt'
with open(file) as file:
    for cnt, line in enumerate(file):
        print("{}:{}".format(cnt,line))
        
file='pyvenv.cfg'
with open(file) as file:
    for cnt, line in enumerate(file):
        print("{}:{}".format(cnt,line))

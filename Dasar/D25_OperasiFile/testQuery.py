import os

os.mkdir("tesmkdir")
input("Press any key to continue...")
os.rename('tesmkdir','newDirectory')

print(os.getcwd())
os.chdir(r'E:')
print(os.getcwd())

"""Write a Python program to create a symbolic link and read it to decide the original file pointed by the link.""" 
import os
path = '/tmp/' + os.path.basename(__file__)
print('Creating link {} -> {}'.format(path, __file__))
os.symlink(__file__, path)
stat_info = os.lstat(path)
print('\nFile Permissions:', oct(stat_info.st_mode))
print('\nPoints to:', os.readlink(path))
#removes the file path
os.unlink(path)
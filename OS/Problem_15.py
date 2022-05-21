"""
Write a Python program to get information about the file pertaining to the file mode.
Print the information - ID of device containing file, inode number, protection, number of 
hard links, user ID of owner, group ID of owner, total size (in bytes), time of last access, 
time of last modification and time of last status change.
""" 

import os
path = 'e:\\testpath\\p.txt'
fd = os.open(path, os.O_RDWR)
info = os.fstat(fd)
print (f"ID of device containing file: {info.st_dev}")
print (f"Inode number: {info.st_ino}")
print (f"Protection: {info.st_mode}")
print (f"Number of hard links: {info.st_nlink}")
print (f"User ID of owner: {info.st_uid}")
print (f"Group ID of owner: {info.st_gid}")
print (f"Total size, in bytes: {info.st_size}")
print (f"Time of last access: {info.st_atime}")
print (f"Time of last modification: {info.st_mtime }")
print (f"Time of last status change: {info.st_ctime }")
os.close( fd)
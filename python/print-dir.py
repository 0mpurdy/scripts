import os
import re

def count_all_files_ext(directory, ext=".*\\.txt", ignoredDirs = ['.git']):
	print('Counting files in %s with regex %s' % (directory, ext))
	count = 0
	for root, dirs, files in os.walk(directory):
		# https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
		dirs[:] = [d for d in dirs if d not in ignoredDirs]
		#print('Root: %s\nDir: %s\nFile: %s' % (root, dirs, files))
		for file in files:
			if re.search(ext, file):
				count += 1
	print(count)

def count_all_files(directory, ignoredDirs = ['.git']):
	print('Counting files in %s' % directory)
	count = 0
	for root, dirs, files in os.walk(directory):
		# https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
		dirs[:] = [d for d in dirs if d not in ignoredDirs]
		#print('Root: %s\nDir: %s\nFile: %s' % (root, dirs, files))
		count += len(files)
	print(count)

def print_all_files(directory, ignoredDirs = ['.git']):
	print('All files from %s' % directory)
	for root, dirs, files in os.walk(directory):
		# https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
		dirs[:] = [d for d in dirs if d not in ignoredDirs]
		#print('Root: %s\nDir: %s\nFile: %s' % (root, dirs, files))
		for file in files:
			print("%s" % os.path.join(root, file))

def sep():
	print("\n***\n")

#test examples
#print_all_files(os.path.join('c:\\', 'dev', 'fyp'))
#print_all_files('..')
count_all_files_ext('G:\dev\mse\MSE-Res-Lite')
count_all_files_ext('G:\dev\mse\MSE-Res-Lite', ext=".*\\.md")
count_all_files_ext('G:\dev\mse\MSE-Res-Lite', ext=".*\\.png")

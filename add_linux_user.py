#
#	Two methods to execute this file
#	1. python add_linux_user.py --adduser rocker_ako 
#		>> The program will search for userlist.txt inside unprocessed folder
#	2. python add_linux_user.py --adduser <file path>
#		>> The program will read the content from the filepath the execute adding user
#

import os 
import subprocess

DEFAULT_DIR = os.path.join(os.getcwd(),"UNPROCESSED")
DATA_FILE = os.path.join(DEFAULT_DIR, "userlist.txt")

def start(config_file_path=""):
	if os.path.isfile(config_file_path):
		AddLinuxUser(config_file_path)
	else:
		if os.path.isdir(DEFAULT_DIR):
			if "userlist.txt" in os.listdir(DEFAULT_DIR):
				AddLinuxUser(DATA_FILE)
			else: 
				print "userlist.txt missing in %s"%DEFAULT_DIR
		else:
			print "File Needed"
				
class AddLinuxUser(object):

	def __init__(self, contents):
		self.contents = os.path.realpath(contents)
		print "File: ", os.path.isfile(self.contents)
		self.read_contents()
	
	def read_contents(self):	
		contents = open(self.contents).read()
		for username in contents.split('\n'):
			print "Start adding user: %s" % username
			self.add_user_cmd(username)
				
	def add_user_cmd(self, username):
		try:
			process = subprocess.Popen(['useradd', username, '-s', '/bin/false'], 
						stdout = subprocess.PIPE)
			process.stdout.read()
			print "%s has been added"%username
		except Exception, oo:
			print "Unable to add user %s"%username
			print oo
		
if __name__ == '__main__':

	import argparse

	helptext = """Accept file path as parameter. 
				While if 'rock' is added as parameter,
				then it will reads file from UNPROCESSED/userlist.txt"""
		
	cmd = argparse.ArgumentParser()
	cmd.add_argument("--adduser", help=helptext)
	config_file_path = cmd.parse_args().adduser

	start(cmd.parse_args().adduser)
	
	
	
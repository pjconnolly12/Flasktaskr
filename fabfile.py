# fabfile.py

from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
	with settings(warn_only=True):
		result = local("noestests -v", capture=True)
	if result.failed and not confir("Tests failed. Continue?"):
		abort("Aborted at user request.")

def commit():
	message = raw_input("Enter a git commit message: ")
	local("git add . && git commit -am '{}'".format(message))

def push():
	local("git push origin master")

def prepare():
	test()
	commit()
	push()


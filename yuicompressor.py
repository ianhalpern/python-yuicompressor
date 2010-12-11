import subprocess

def compress( jsfile ):
	cmd = 'yuicompressor %s' % jsfile
	return subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE ).stdout.read()

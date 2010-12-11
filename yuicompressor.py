import subprocess

def compress( jsfile ):
	cmd = 'yui-compressor %s' % jsfile
	return subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE ).stdout.read()

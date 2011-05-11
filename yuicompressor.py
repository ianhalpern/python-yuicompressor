import subprocess

def compress( jsfile, **options ):
	"""
		To add cli options pass the option as an argument.

		Example:
			compress( 'file.js', nomunge=True, line_break=4 )
	"""
	options = ' '.join(
		map( lambda k: ( '--' if len(k) > 1 else '-' ) + k.replace( '_', '-' ) + ( ' %s' % options[k] if options[k] != True else '' ),
		[ k for k in options.keys() if options[k] ] )
	)

	cmd = 'yui-compressor %s %s' % ( options, jsfile )

	return subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE ).stdout.read()

if __name__ == '__main__':
	print compress( '', h=True )

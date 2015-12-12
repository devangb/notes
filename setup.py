from setuptools import setup

setup(
	name='Notes',
	version='1.0',
	py_modules=['notes'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		notes=notes:cli
	'''
)

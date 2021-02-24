#
#   EZ ARGPARSER v1.0.0
#	By: samulieronen
#	Date: 24.Feb.2021
#

import sys		#del this

ParserOptions = {
	'includeProgName': False,	#default: False
	'errorExtra': False,		#default: False
	'ignoreInvalid': False,		#default: False
}

ArgSchema = {
	'options': [['v', 'verbose'], ['l', 'long']],
	'optionParams': {
		'random_param': {'optional': False, 'type': 'String'},
	},
	'args': {
		'i_am_a_key': {'optional': False, 'type': 'String', 'count': 2},
		'asd': {'optional': False, 'type': 'Number'}
	}
}

def convert_to_nb(string):
	try:
		return int(string)
	except ValueError:
		print(f'EZArgParser ERROR: {string} has to be a number!')
		return None

def parse_args(args, schema, options=None):
	argDict = {}
	print('Parsing!')

	return argDict

def parse_options(args, schema):
	pass


class ArgParser:
	def __init__(self, args, schema, options=None):
		if isinstance(args, list):
			self.args = args.copy()
			self.schema = schema
			self.optionsParsed = parse_options(self.args, schema)
			self.argsParsed = parse_args(self.args, schema)
		else:
			print(f'EZArgParser ERROR: Args list not correct format!')
			print(f'\tExpected {list}, got {type(args)}\n')
			sys.exit() # Shouldn't exit, instead throw err

	def fetchArg(self, key):
		pass
	
	def checkOption(self, key):
		pass

	def fetchOptionParams(self, key):
		pass

	def printArgs(self):
		print('Printing args')
		for arg in self.args:
		   print('\t%s ' %arg)


lol = ArgParser(sys.argv(), ArgSchema)
lol.printArgs()
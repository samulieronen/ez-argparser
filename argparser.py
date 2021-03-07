#
#   EZ ARGPARSER v1.0.0
#	argparser.py
#	By: samulieronen
#	Date: 26.Feb.2021
#


from .args import parse_args
from .options import parse_options


class SchemaError(Exception):
	pass

class ArgumentError(Exception):
	pass


class ArgParser:
	def __init__(self, arguments, argumentSchema, options=False, optionSchema=None, parserOptions=None):
		if isinstance(arguments, list):
			self.untouched = arguments
			self.args = arguments.copy()
			self.argSchema = argumentSchema
			self.options = options
			self.optSchema = optionSchema

			'''Parse Options'''
			self.optParsed = {}
			if options:
				if optionSchema:
					self.optParsed = parse_options(self.args, optionSchema)
				else:
					raise SchemaError('SCHEMA ERROR: Mixed signals!\n\toptions was True but no optionSchema provided!')

			'''Parse Arguments'''
			self.argsParsed = parse_args(self.args, argumentSchema)
		else:
			raise ArgumentError(f'EZArgParser ERROR: Args list not correct format!\n\tExpected {list}, got {type(arguments)}\n')

	def fetchArg(self, key):
		if not isinstance(key, str):
			return None
		try:
			if self.argsParsed[key]:
				return self.argsParsed[key]
		except KeyError:
			return None
	
	def checkOption(self, option):
		try:
			return self.optParsed[option]['active']
		except KeyError:
			return False

	def fetchOptionParams(self, option, key):
		try:
			option = self.optParsed[option]
			return option[key]
		except KeyError:
			return None

	def fetchAllArgs(self):
		return self.untouched

	def printArgs(self):
		for arg in self.untouched:
		   print(arg)
		print()


#
#   EZ ARGPARSER v1.0.0
#	By: samulieronen
#	Date: 24.Feb.2021
#

import sys		# del this

ParserOptions = {
	'includeProgName': False,	#default: False
	'errorExtra': False,		#default: False
	'ignoreInvalid': False,		#default: False
	'returnList': False			#default: False
}

EZtestArgs = ['EZArgParser/exargparser.py', 'arg1', 'arg2','codingisfun', '1069', '-v']

ArgSchema = {
	'filename': {'type': str},
	'i_am_a_key': {'type': str, 'count': 2},
	'TADAA': {'type': str, 'count': 1},
	'random_number': {'type': int}
}

OptSchema = {
	'v': {'verbose': 'verbose'},
	'l': {'verbose': 'long'},
	'e': {'verbose': 'errors', 'params': {
		'path': {'type': str},
	}}
}

def converter(value, type_to_convert):
	if type(type_to_convert) is not type:
		print(f'EZArgParser SCHEMA ERROR: {type_to_convert} has to be a type!')
		sys.exit()
	try:
		return type_to_convert(value)
	except ValueError:
		print(f'EZArgParser ERROR: {value} has to be a number!')
		sys.exit()

def get_count(argSchema):
	count = 1
	try:
		count = argSchema['count']
		count = int(count)
		if count == 'all':
			return -1
		elif count < 1:
			return 1
	except KeyError or ValueError:
		return count
	return count


def validate_types(args, schema):
	try:
		type_to_convert = schema['type']
	except KeyError:
		type_to_convert = str
	newList = []
	for item in args:
		if item is not None:
			if type is not str:
				newList.append(converter(item, type_to_convert))
			else:
				newList.append(item)
	return newList

def get_args(argDict, currentSchema, args, amount, name):
	if amount < 0:
		argDict[name] = validate_types(args, currentSchema)
	else:
		argDict[name] = validate_types(args[:amount], currentSchema)
	if amount == 1:
		argDict[name] = argDict[name][0]
	return argDict
	

def parse_args(args, schema):
	argDict = {}
	index = 0
	keyIndex = 0
	schemaKeys = list(schema.keys())
	if len(schemaKeys) < 1:
		return argDict
	while index < len(args):
		if args[index] != None and keyIndex < len(schemaKeys):
			currentSchema = schema[schemaKeys[keyIndex]]
			currentSchemaName = schemaKeys[keyIndex]
			argDict = get_args(argDict, currentSchema, args[index:], get_count(currentSchema), currentSchemaName)
			increment = get_count(currentSchema)
			if increment < 0:
				break
			else:
				index += (increment - 1)
			keyIndex += 1
		index += 1
	return argDict

class ArgParser:
	def __init__(self, arguments, argumentSchema, options=False, optionSchema=None, parserOptions=None):
		if isinstance(arguments, list):
			self.args = arguments.copy()
			self.argSchema = argumentSchema
			self.argsParsed = parse_args(self.args, argumentSchema)
			self.options = options
			self.optSchema = optionSchema
		else:
			print(f'EZArgParser ERROR: Args list not correct format!')
			print(f'\tExpected {list}, got {type(arguments)}\n')
			sys.exit() # Shouldn't exit, instead throw err

	def fetchArg(self, key):
		if not isinstance(key, str):
			return None
		try:
			if self.argsParsed[key]:
				return self.argsParsed[key]
		except KeyError:
			return None
	
	def checkOption(self, key):
		pass

	def fetchOptionParams(self, key):
		pass

	def getAllArgs(self):
		return self.args

	def printArgs(self):
		print('Printing args')
		for arg in self.args:
		   print('\t%s ' %arg)


SuperHelpfulParser = ArgParser(EZtestArgs, ArgSchema)
SuperHelpfulParser.printArgs()
print(SuperHelpfulParser.fetchArg('filename')) # Works like a charm!
#print(SuperHelpfulParser.checkOption('haha')) TOO SOON!!

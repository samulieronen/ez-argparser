#
#   EZ ARGPARSER v1.0.0
#	options.py
#	By: samulieronen
#	Date: 26.Feb.2021
#

from .utils import get_count
from .utils import validate_types

class OptionSchemaError(Exception):
	pass

class ArgumentError(Exception):
	pass

indexesToDelete = []

def clean_option(arg):
	if arg[0] == '-' and arg[1] != '-':
		return arg[1:]
	else:
		return arg[2:]

def remove_optargs(args):
	index = 0
	rmIndex = 0
	while index < len(args):
		if index == indexesToDelete[rmIndex]:
			args[index] == None
			rmIndex += 1
		index += 1

def fetch_long_option(key, schema):
	try:
		return schema[key]['verbose']
	except KeyError:
		return None

def get_params(optDict, args, paramSchema, key, paramKey, index):
	paramcount = get_count(paramSchema)
	if paramcount < 0:
		raise OptionSchemaError(f'SCHEMA ERROR: Illegal flag in option param count!\n\tFlag \'all\' not allowed in option parameter schema!')
	if len(args) < paramcount:
		raise ArgumentError(f'ERROR: Too few arguments to satisfy option parameters!\n\tCheck input!')
	else:
		params = validate_types(args[:paramcount], paramSchema)
	optDict[key][paramKey] = params
	for i in range(paramcount):
		indexesToDelete.append(index + i)
	return optDict

def form_option(optDict, args, schema, key, index):
	optDict[key] = {'active': True}
	try:
		params = schema[key]['params']
	except KeyError:
		params = None
	if params:
		paramKeys = list(params.keys())
		increment = 1
		for paramKey in paramKeys:
			get_params(optDict, args[increment:], params[paramKey], key, paramKey, index + 1)
			increment += get_count(params[paramKey])
	return optDict

def get_option(optDict, args, schema, keys, index):
	option = clean_option(args[0])
	matches = 0
	for key in keys:
		long_option = fetch_long_option(key, schema)
		if key == option:
			optDict = form_option(optDict, args, schema, key, index)
			indexesToDelete.append(index)
			matches += 1
		elif long_option is not None and long_option == option:
			optDict = form_option(optDict, args, schema, key, index)
			indexesToDelete.append(index)
			matches += 1
	if matches == 0:
		raise ArgumentError(f'ERROR: Nonexistent option!\n\tNo matching option for {option}')
	return optDict

def parse_options(args, schema):
	optDict = {}
	index = 0
	schemaKeys = list(schema.keys())
	if len(schemaKeys) < 1:
		return optDict
	while index < len(args):
		if args[index] is not None:
			if type(args[index]) is not str:
				ArgumentError(f'ERROR: Invalid argument type:\n\tExpected {str}, got {type(args[index])}!')
			cleanedArg = args[index].strip()
			if cleanedArg[0] == '-':
				optDict = get_option(optDict, args[index:], schema, schemaKeys, index)
		index += 1
	remove_optargs(args)
	return optDict
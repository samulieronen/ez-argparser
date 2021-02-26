#
#   EZ ARGPARSER v1.0.0
#	args.py
#	By: samulieronen
#	Date: 26.Feb.2021
#

from .utils import validate_types
from .utils import get_count

class ArgumentSchemaError(Exception):
	pass

class ArgumentError(Exception):
	pass

def get_args(argDict, currentSchema, args, amount, name):
	if amount < 0 or len(args) < amount:
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

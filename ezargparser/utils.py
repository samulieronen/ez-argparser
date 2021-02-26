#
#   EZ ARGPARSER v1.0.0
#	utils.py
#	By: samulieronen
#	Date: 26.Feb.2021
#

class SchemaError(Exception):
	pass

class ArgumentError(Exception):
	pass

def get_count(argSchema):
	count = 1
	try:
		count = argSchema['count']
		if count == 'all':
			return -1
		try:
			count = int(count)
		except ValueError:
			raise SchemaError(f'SCHEMA ERROR: Invalid formatted value for key \'count\': {count}\n\tMust be int or \'all\'')
		if count < 1:
			return 1
	except KeyError:
		return 1
	return count

def converter(value, type_to_convert):
	if type(type_to_convert) is not type:
		raise SchemaError(f'SCHEMA ERROR: {type_to_convert} has to be a type!')
	try:
		return type_to_convert(value)
	except ValueError:
		raise ArgumentError(f'ERROR: {value} has to be a number!')

def validate_types(args, schema):
	try:
		type_to_convert = schema['type']
	except KeyError:
		type_to_convert = str
	newList = []
	index = 0
	while index < len(args):
		if args[index] is not None:
			if type is not str:
				newList.append(converter(args[index], type_to_convert))
			else:
				newList.append(args[index])
		index += 1
	return newList

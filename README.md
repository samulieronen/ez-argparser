```
   ________  ___            ___                      
  / __/_  / / _ | _______ _/ _ \___ ________ ___ ____
 / _/  / /_/ __ |/ __/ _ `/ ___/ _ `/ __(_-</ -_) __/
/___/ /___/_/ |_/_/  \_, /_/   \_,_/_/ /___/\__/_/   .py
                    /___/                            
```

# EZ Arg Parser
Never parse arguments again! (At least in python...)<br>

## Usage
```bash
$ git clone https://github.com/samulieronen/ez-argparser.git
```
```python
# in your .py file
from ezargparser import ArgParser

Parser = ArgParser(arguments=args, argSchema=argSchema)
```
<br>

### Argument Schema
You need to provide a schema for your arguments.<br>
Example:
```python
ArgSchema = {
	'filename': {'type': str},
	'i_am_a_key': {'type': str, 'count': 2},
	'i_can_be_anything': {'type': str, 'count': 1},
	'random_number': {'type': int}
}
```
__Each schema 'key' has to be unique, but they can be named however you want.__
```python
 {'type': str, 'count': 2}
```
`type` specifies the type you want the input to be. Defaults to string if not provided.<br>
Optional: `count` spcifies the number of arguments related to this key. Defaults to 1 if not provided<br>
* `'count': 'all'` will take the all the remaining arguments and store them to the key.
<br>

### Fetching arguments
Fetching arguments with a key:
```python
Parser.fetchArg('filename')
# if count was > 1, returns a list of the arguments related to this specific key.
# else, returns the single argument
# returns None if key was not found
```
Fetching all arguments:
```python
Parser.fetchAllArgs()
## returns a list of all arguments
```
<br>

### Option Schema
Using EZ ArgParser with options
```python
from ezargparser import ArgParser

Parser = ArgParser(arguments=args, argumentSchema=argSchema, options=True, optionSchema=optSchema)
```
As with arguments, if your program takes options, you need to specify a option schema.<br>
```python
OptSchema = {
	'v': {'verbose': 'verbose'},
	'l': {'verbose': 'long'},
	'e': {'verbose': 'errors', 'params': {
		'path': {'type': str},
		'3_numbers': {'type': int, 'count': 3}
	}}
}
```
This option schema specifies the following options:
* -v
* -l
* -e
<br>

Option bundling, f.ex. -vle __NOT__ supported at the moment.<br>
__Name schema keys WITHOUT leading hyphens! '-'__ <br>
Each schema key __MUST__ be a valid option. Name them wisely.<br>
If a option has a long version, you can specify it to the `verbose` field.<br>
If your option takes parameters:
```python
'e': {'verbose': 'errors', 'params': {
		'path': {'type': str},
		'3_numbers': {'type': int, 'count': 3}
	}}
```
Like with arguments,<br>
`type` specifies the type you want the parameter to be. Defaults to string if not provided.<br>
Optional: `count` spcifies the number of parameters related to this key.<br>
* Note that `'count': 'all'` can __NOT__ be used when dealing with option parameters (for now).
<br>

### Fetching options & option parameters
Check if option is active:
```python
Parser.checkOption('v')
# returns True if active, False if not active or nonexistent in schema
```
Fetch option parameter:
```python
Parser.fetchOptionParams('e', 'path')
# if count was > 1, returns a list of the parameters related to this specific key.
# else, returns the single parameter
# returns None if key or parameter key was not found
```

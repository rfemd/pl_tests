import json
import sys


def dfs(val,values):
	val['value'] = values.get(val['id'])
	if 'values' in val.keys():
		for val2 in val['values']:
			dfs(val2, values)
	else:
		return


if __name__ == '__main__':
	tests = sys.argv[1]
	val = sys.argv[2]
	report = sys.argv[3]

	with open(tests,'r') as f:
		tests = f.read()
		tests = json.loads(tests)

	with open(val,'r') as f:
		values = f.read()
		values = json.loads(values)
		values = {x['id']:x['value'] for x in values['values']}

	for i,val in enumerate(tests['tests']):
		dfs(val, values)

	with open(report,'w') as f:
		tests = json.dumps(tests)
		f.write(tests)

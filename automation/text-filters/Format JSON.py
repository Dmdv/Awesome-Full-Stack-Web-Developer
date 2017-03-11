#!/usr/bin/python
import fileinput
import json
if __name__ == "__main__":
  text = ''
  for line in fileinput.input():
    text = text + ' ' + line.strip()
  jsonObj = json.loads(text)
  print json.dumps(jsonObj, sort_keys=False, indent=2)

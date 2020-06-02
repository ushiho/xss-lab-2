#!/usr/bin/python3

import sys, os
from attack import Attack


def main(url):
	attack = Attack(url)
	payload = '&lt;img src="foo" onerror="alert(\'vulnerable\');" /&gt;'

	res = attack.run(payload)
	if res:
		msg = "The app is vulnerable"
	else:
		msg = "You are in good hands"
	return (res, msg)

if __name__ == '__main__':
	url = 'http://0.0.0.0:5000/'
	res = main(url)
	print(res)

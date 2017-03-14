#!/usr/bin/env python3

from sys import stdin, argv
from importlib import import_module

def get_count(input_string):
	return input_string.count("<item>")

#breaks on feeds with more than one channel
#assume, that there are items
def get_header(input_string):
	return input_string.split("<item>", 1)[0]

def get_footer(input_string):
	return input_string.rsplit("</item>", 1)[-1]

def get_items(input_string):
	item_list = input_string.split("<item>")[1:]
	return [item.split("</item>")[0] for item in item_list]


def get_tag_content(item_string, tag_name):
	"""extract the content of a tag named tag_name.
	assume, there is only one tag with this name and no tags whose name starts with the same string"""
	try:
		return item_string.split("<"+tag_name, 1)[1].split(">", 1)[1].rsplit("</"+tag_name+">",1)[0]
	except:
		return ""



if __name__ == "__main__":
	instring = stdin.read()
	if len(argv) >=2:
		customFilter = import_module(argv[1])
		show_content = argv[2:]

	count = get_count(instring)
	if count==0:
		print(instring)
	else:	#assume that there are items
		header = get_header(instring)
		items = get_items(instring)
		footer = get_footer(instring)

		print(header.strip())
		for item in items:
			if customFilter.filter_item(item, show_content):
				print("<item>" + item + "</item>")
		print(footer.strip())
		
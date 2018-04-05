#!/usr/bin/env python3

from sys import stdin, argv
from importlib import import_module

def is_Atom(input_string):
	return not not input_string.count("<feed")

def get_item_count(input_string):
	return input_string.count("<item>") + input_string.count("<entry>")

#breaks on feeds with more than one channel
#assume, that there are items
def get_header(input_string):
	item_tag = "<entry>" if is_Atom(input_string) else "<item>"
	return input_string.split(item_tag, 1)[0]

def get_footer(input_string):
	item_end_tag = "</entry>" if is_Atom(input_string) else "</item>"
	return input_string.rsplit(item_end_tag, 1)[-1]

def get_items(input_string):
	item_tag_name = "entry" if is_Atom(input_string) else "item"
	item_list = input_string.split("<"+item_tag_name+">")[1:]
	return [item.split("</"+item_tag_name+">")[0] for item in item_list]


def get_tag_content(item_string, tag_name):
	"""extract the content of a tag named tag_name.
	Use the first tag, that starts with the given name"""
	try:
		return item_string.split("<"+tag_name, 1)[1].split(">", 1)[1].split("</"+tag_name+">",1)[0]
	except:
		return ""


def get_tag_attribute(item_string, tag_name, attribute_name):
	"""extract a certain attribute from a tag.
	Use the first tag an the first attribute that start with the given names"""
	try:
		attribute_string = item_string.split("<"+tag_name, 1)[1].split(">", 1)[0].split(attribute_name+"=", 1)[1]
		return attribute_string.split(attribute_string[0])[1]
	except:
		return ""


if __name__ == "__main__":
	input_string = stdin.read()
	if len(argv) >=2:
		customFilter = import_module(argv[1])
		show_content = argv[2:]

	count = get_item_count(input_string)
	if count==0:
		print(input_string)
	else:	#assume that there are items
		header = get_header(input_string)
		items = get_items(input_string)
		footer = get_footer(input_string)

		print(header.strip())
		item_tag_name = "entry" if is_Atom(input_string) else "item"
		for item in items:
			if customFilter.filter_item(item, show_content):
				print("<"+item_tag_name+">" + item + "</"+item_tag_name+">")
		print(footer.strip())
		
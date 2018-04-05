#!/usr/bin/env python3
import filterRSS


def filter_item(item_string, criteria):
	link_target = filterRSS.get_tag_attribute(item_string, "link", "href")

	filters = {}

	filters["techstage"] = lambda link: (link.startswith("https://www.techstage.de/"))

	filters["notechstage"] = lambda link: not (link.startswith("https://www.techstage.de/"))


	for criterion in criteria:
		filter = filters.get(criterion)

		if not filter: continue	# there was no filter for this criterion
		if filter(link_target): return True


	#otherwise: don't show the item
	return False

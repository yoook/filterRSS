#!/usr/bin/env python3
import filterRSS


def filter_item(item_string, criteria):
	title_name = filterRSS.get_tag_content(item_string, "title")

	filters = {}

	filters["only#"] = lambda title: (title.startswith("#"))
	filters["no#"] = lambda title: not (title.startswith("#"))

	for criterion in criteria:
		filter = filters.get(criterion)

		if not filter: continue	# there was no filter for this criterion
		if filter(title_name): return True


	#otherwise: don't show the item
	return False

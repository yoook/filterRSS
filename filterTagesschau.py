#!/usr/bin/env python3
import filterRSS 


def filter_item(item_string, criteria):
	link_string = filterRSS.get_tag_content(item_string, "link")

	filters = {}
	filters["Sport"] = lambda link: (link.startswith("http://www1.sportschau.de/") 
		or link.startswith("http://www.sportschau.de/")
		or "sport" in link.split("/")[:-1])		#Sport should include any form of Regionalsport

	filters["Regionalsport"] = lambda link: link.startswith("http://www.tagesschau.de/ardimport/sport/")

	filters["Ausland"] = lambda link: link.startswith("http://www.tagesschau.de/ausland/")

	filters["Inland"] = lambda link: (link.startswith("http://www.tagesschau.de/inland/") or link.startswith("http://wahl.tagesschau.de/wahlen/"))

	filters["Wirtschaft"] = lambda link: (link.startswith("http://www.tagesschau.de/wirtschaft/") 
		or link.startswith("http://boerse.ard.de/"))

	filters["Kultur"] = lambda link: link.startswith("http://www.tagesschau.de/kultur/")

	filters["Regional"] = lambda link: (link.startswith("http://www.tagesschau.de/ardimport/regional/")
		or (link.startswith("http://hessenschau.de/")
				or link.startswith("http://www.rbb-online.de/")
				or link.startswith("http://www1.wdr.de/")
				or link.startswith("http://www.mdr.de/")
				or link.startswith("http://www.sr.de/")
				or link.startswith("http://www.ndr.de/")
			) and not (filters["Sport"](link))
		)

	filters["Videoblog"] = lambda link: link.startswith("http://www.tagesschau.de/videoblog/")

	filters["Eilmeldung"] = lambda link: link.startswith("http://www.tagesschau.de/eilmeldung/")

	filters["Kommentar"] = lambda link: link.startswith("http://www.tagesschau.de/kommentar/")

	filters["kurzerklaert"] = lambda link: link.startswith("http://www.tagesschau.de/multimedia/kurzerklaert/")

	filters["Schlusslicht"] = lambda link: link.startswith("http://www.tagesschau.de/")


	for criterion in criteria:
		filter = filters.get(criterion)

		if not filter: continue	# there was no filter for this criterion
		if filter(link_string): return True


	if "alles" in criteria: return True

	if "anderes" in criteria:
		for filter in filters.values():
			if filter(link_string): return False
		return True

	if "alles-außer-Sport" in criteria:		# this must be the last filter rule
		if filters["Sport"](link_string): return False
		if filters["Regionalsport"](link_string): return False
		return True


	#otherwise: don't show the item
	return False

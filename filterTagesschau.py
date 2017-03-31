#!/usr/bin/env python3
import filterRSS 

def filter_item(item_string, criteria):
	link_string = filterRSS.get_tag_content(item_string, "link")

	#never show sport
	if filter_item_Sport(link_string): return False
	if filter_item_Regionalsport(link_string): return False

	if "Inland"     in criteria and filter_item_Inland(link_string): return True
	if "Ausland"    in criteria and filter_item_Ausland(link_string): return True
	if "Kultur"     in criteria and filter_item_Kultur(link_string): return True
	if "Regional"   in criteria and filter_item_Regional(link_string): return True
	if "Videoblog"  in criteria and filter_item_Videoblog(link_string): return True
	if "Wirtschaft" in criteria and filter_item_Wirtschaft(link_string): return True
	if "anderes"   in criteria:
		if not filter_item_Ausland(link_string) and not filter_item_Inland(link_string) and not filter_item_Kultur(link_string) and not filter_item_Regional(link_string) and not filter_item_Videoblog(link_string) and not filter_item_Wirtschaft(link_string) and not filter_item_Kommentar(link_string) and not filter_item_kurzerklärt(link_string) and not filter_item_Schlusslicht(link_string):
			return True
	if "alles"     in criteria: return True #still no sport!

	#otherwise: don't show the item
	return False



def filter_item_Sport(link):
	return (link.startswith("http://www1.sportschau.de/") 
		or link.startswith("http://www.sportschau.de/")
		or "sport" in link.split("/")[:-1])		#Sport should include any form of Regionalsport

def filter_item_Regionalsport(link):
	return link.startswith("http://www.tagesschau.de/ardimport/sport/")

def filter_item_Ausland(link):
	return link.startswith("http://www.tagesschau.de/ausland/")
		
def filter_item_Inland(link):
	return (link.startswith("http://www.tagesschau.de/inland/")
		or link.startswith("http://wahl.tagesschau.de/wahlen/"))

def filter_item_Wirtschaft(link):
	return (link.startswith("http://www.tagesschau.de/wirtschaft/") 
		or link.startswith("http://boerse.ard.de/"))

def filter_item_Kultur(link):
	return link.startswith("http://www.tagesschau.de/kultur/")

def filter_item_Regional(link):
	return (link.startswith("http://www.tagesschau.de/ardimport/regional/")
		or (link.startswith("http://hessenschau.de/")
				or link.startswith("http://www.rbb-online.de/")
				or link.startswith("http://www1.wdr.de/")
				or link.startswith("http://www.mdr.de/")
				or link.startswith("http://www.sr.de/")
				or link.startswith("http://www.ndr.de/")
			) and not (filter_item_Sport(link)
	))

def filter_item_Videoblog(link):
	return link.startswith("http://www.tagesschau.de/videoblog/")

def filter_item_Eilmeldung(link):
	return link.startswith("http://www.tagesschau.de/eilmeldung/")

def filter_item_Kommentar(link):
	return link.startswith("http://www.tagesschau.de/kommentar/")

def filter_item_kurzerklärt(link):
	return link.startswith("http://www.tagesschau.de/multimedia/kurzerklaert/")

def filter_item_Schlusslicht(link):
	return link.startswith("http://www.tagesschau.de/")
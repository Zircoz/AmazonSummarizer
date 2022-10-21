"""
TODO: Add chromium driver, use the expectation below to edit this script & download files

Open an automated browser ->Ask user their amazon's base url -> STOP TO TAKE INPUT AND EXPECT USER TO LOGIN TO THEIR AMAZON ACCOUNT -> USER PRESSED C (continue) or Y (yes) -> start downloading files with a delay of 5 seconds between each request
"""

from json import load
from bs4 import BeautifulSoup

def getDownloadURLs(file: str="object.json", baseAmazonURL: str="amazon.in") -> list:
	"""
	file: str
		the json file created from table of Amazon data download page
	baseAmazonURL: str
		the base domain of the amazon account user has used to request the data
		example: amazon.com, amazon.in, amazon.co.uk
	"""
	
	f = open('object.json')
	obj = json.load(f)
	downloadURLs = []
	for eachRow in obj["rows"]:
    		downloadURLs.append(f"https://{baseAmazonURL.strip("/")}{ BeautifulSoup(eachRow).a['href'] }")
	return downloadURLs

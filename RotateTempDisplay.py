import tkinter as tk

import Credentials      # Get API keys, etc.

apikey = Credentials.prod_api
baseurl = 'https://api-na.hosted.exlibrisgroup.com'
queryGetItem = '/almaws/v1/bibs/{mms_id}/holdings/{holding_id}/items/{item_pid}?apikey={apikey}'
queryGetSet = '/almaws/v1/conf/sets/{id}/members?limit={limit}&offset={offset}&apikey={apikey}'
queryGetCollxn = '/almaws/v1/bibs/collections/{id}/bibs?limit={limit}&offset={offset}&apikey={apikey}'
queryListSets = '/almaws/v1/conf/sets?limit={limit}&offset={offset}&apikey={apikey}{id}'  # id is just empty value, but here for consistency

api_bib_rw = Credentials.bib_rw_api     # Production
api_conf_rw = Credentials.conf_rw_api   # Production


# Determine how many runs to make (ExL limits to 100 results per request)
def GetCount(SetID=None, CollxnID=None, ListSets=False):
    if (SetID is None and CollxnID is None and ListSets is False):
        raise ValueError("You must provide EITHER a Collection ID or a Set ID")
    if (SetID is not None):
        elements = 'members'
        ID = SetID
        query = queryGetSet
        APIKey = api_conf_rw
    elif(CollxnID is not None):
        elements = 'bibs'
        ID = CollxnID
        query = queryGetCollxn
        APIKey = api_bib_rw
    elif(ListSets is True):
        elements = 'sets'
        ID = ''
        query = queryListSets
        APIKey = api_conf_rw

    r = requests.get(''.join([baseurl, query.format(id=ID, limit=0, offset=0, apikey=APIKey)]))
    rdict = xmltodict.parse(r.content)
    count = int(rdict[elements]['@total_record_count'])
    runs = math.ceil(count / 100)
    return (count, runs)


# Get an actual list of up to 100 items from a set/collection/etc
def GetItems(offset=0, SetID=None, CollxnID=None, ListSets=False):
    if (SetID is None and CollxnID is None and ListSets is False):
        raise ValueError("You must provide EITHER a Collection ID or a Set ID")
    if (SetID is not None):
        elements = 'members'
        element = 'member'
        ID = SetID
        query = queryGetSet
        APIKey = api_conf_rw
    elif(CollxnID is not None):
        elements = 'bibs'
        element = 'bib'
        ID = CollxnID
        query = queryGetCollxn
        APIKey = api_bib_rw
    elif(ListSets is True):
        elements = 'sets'
        element = 'set'
        ID = ''
        query = queryListSets
        APIKey = api_conf_rw

    r = requests.get(''.join([baseurl, query.format(id=ID, limit=100, offset=(offset * 100), apikey=APIKey)]))
    rdict = xmltodict.parse(r.content)
    itemlist = rdict[elements][element]
    # Single-item set will return an OrderedDict or something instead of a list. Convert that.
    itemlist = itemlist if (isinstance(itemlist, list)) else [itemlist]
    return(itemlist)



# Import a list of existing Alma sets
#   As dict, with Set ID


# Ask which set to REMOVE temp location from


# Ask which set to ADD temp location to


# Ask which Primo collection to update (INCLUDE 'NONE' OPTION)

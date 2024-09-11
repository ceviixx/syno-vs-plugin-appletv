import argparse
import json
import requests
import datetime

from media import movie
from media import tvshow
from media import tvshow_episode

def getLocale(value):
    if value == "ger":
        return "de-DE"
    else:
        return "-"

def getLangCode(value):
    if value == "ger":
        return "143443"
    else:
        return "-"

def errorData():
    synoRes = []
    synoExtraItem = {
        "com.ceviixx": {
            "rating": {
                "com.ceviixx": 10.0
            },
            "poster": ["https://localhost/test.jpg"],
            "backdrop": ["https://localhost/test.jpg"]
        }
    }
    synoEntryItem = {
        "title": "ERROR",
        "tagline": "",
        "original_available": "1970-01-01",
        "original_title": "ERROR",
        "summary": "ERROR",
        "certificate": "",
        "genre": ["GENRE"],
        "actor": ["ACTOR"],
        "director": ["DIRECTOR"],
        "writer": ["WRITER"],
        "extra": synoExtraItem
    }
    
    synoRes.append(synoEntryItem)
    return synoRes






def main(type, language: str, input, limit: int, allowguess: bool):
    locale = getLocale(language)
    langCode = getLangCode(language)

    r = json.dumps(input)
    loaded_r = json.loads(r)

    data = json.loads(loaded_r)
    searchString = data['title']
    searchString = searchString.replace(' ', '+')

    if type == "movie":
        return movie.metaData(searchString, langCode, locale)
    elif type == "tvshow":
        return tvshow.metaData(searchString, "1", "1", langCode, locale)
    else:
        return errorData()



def setupData(requestType):
    synoExtraItem = {
        "com.ceviixx": {
            "rating": {
                "com.ceviixx": 2.0
            },
            "poster": ["http://localhost.com/test.jpg"],
            "backdrop": ["http://localhost.com/test.jpg"]
        }
    }
    synoEntryItem = {
        "title": requestType,
        "tagline": "",
        "original_available": "2024-01-01",
        "original_title": "TITLE",
        "summary": "DESCRIPTION",
        "certificate": "FSK12",
        "genre": ["GENRE"],
        "actor": ["ACTOR"],
        "director": ["DIRECTOR"],
        "writer": ["WRITER"],
        "extra": synoExtraItem
    }
    return [synoEntryItem]









if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Search',
        description='Forward search query from DSVideo to AppleTV API')

    parser.add_argument('--type')
    parser.add_argument('--lang')
    parser.add_argument('--input')
    parser.add_argument('--limit')
    parser.add_argument('--allowguess')

    args = parser.parse_args()

    

    result = []

    if "--setup" in args.input:
        if args.type == "movie":
            result = movie.setupData()
        elif args.type == "tvshow":
            result = tvshow.setupData()
        elif args.type == "tvshow_episode":
            result = tvshow_episode.setupData()
        else:
            result = setupData(args.type)
            print(args.type)
    else:
        data = main(args.type, args.lang, args.input, args.limit, args.allowguess)
        result = data

    result = {
        "success": True,
        "result": result
    }

    loaded_r = json.dumps(result, ensure_ascii=False, separators=(',', ':'), indent=2)
    print(loaded_r)
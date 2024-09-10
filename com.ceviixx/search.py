import argparse
import sys
import json
import requests
import datetime

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







def movieMeta(searchString, langCode, locale):
    # langCode - locale, title
    url = "https://uts-api.itunes.apple.com/uts/v2/search/incremental?sf={}&locale={}&caller=wta&utsk=0893ae2c4df5b61%3A%3A%3A%3A%3A%3Ac5a7986b1ef4302&v=34&pfm=desktop&q={}".format(langCode, locale, searchString)
    result = requests.get(url)
    shelves = result.json()["data"]["canvas"]["shelves"]

    print(url)
    synoRes = []

    for item in shelves:
        type = item["id"] # uts.col.search.MV
        if type == "uts.col.search.SH":
            continue

        items = item["items"]
        for item in items:
            entryId = item["id"]
            if ".bun." in entryId:
                continue

            # detailUrl = "https://tv.apple.com/api/uts/v2/view/product/{}/?utscf=OjAAAAAAAAA~&utsk=000000000000000000&caller=web&sf=143443&v=40&pfm=web&locale={}".format(entryId, locale)
            # detailData = requests.get(detailUrl)
            
            releaseDate = str(datetime.datetime.fromtimestamp( ( item["releaseDate"] / 1000 ) ))

            posterUrl = item["images"]["coverArt"]["url"]
            posterUrl = posterUrl.replace("{w}", "300" )
            posterUrl = posterUrl.replace("{h}", "600" )
            posterUrl = posterUrl.replace("{f}", "jpg" )

            backdropUrl = item["images"]["previewFrame"]["url"]
            backdropUrl = backdropUrl.replace("{w}", "3840" )
            backdropUrl = backdropUrl.replace("{h}", "2160" )
            backdropUrl = backdropUrl.replace("{f}", "jpg" )

            synoExtraItem = {
                "com.ceviixx": {
                    "rating": {
                        "com.ceviixx": 10.0
                    },
                    "poster": [posterUrl],
                    "backdrop": [backdropUrl]
                }
            }

            # original_available > releaseDate
            synoEntryItem = {
                "title": item["title"],
                "tagline": "",
                "original_available": "2024-01-01",
                "original_title": "TITLE",
                "summary": item["description"],
                "certificate": "FSK12",
                "genre": ["GENRE"],
                "actor": ["ACTOR"],
                "director": ["DIRECTOR"],
                "writer": ["WRITER"],
                "extra": synoExtraItem
            }



            synoRes.append(synoEntryItem)

    return synoRes





def main(type: str, language: str, input, limit: int, allowguess: bool):
    locale = getLocale(language)
    langCode = getLangCode(language)

    r = json.dumps(input)
    loaded_r = json.loads(r)

    data = json.loads(loaded_r)
    searchString = data['title']
    searchString = searchString.replace(' ', '+')
    if type == "movie":
        return movieMeta(searchString, langCode, locale)
    else:
        return "No results"











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
        "title": "TITLE",
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

    

    result = []

    if "--setup" in args.input:
        result = [synoEntryItem]
    else:
        data = main(args.type, args.lang, args.input, args.limit, args.allowguess)
        result = data

    result = {
        "success": True,
        "result": result
    }

    #loaded_r = json.dumps(result, indent=2)
    loaded_r = json.dumps(result, ensure_ascii=False, separators=(',', ':'), indent=2)
    print(loaded_r)
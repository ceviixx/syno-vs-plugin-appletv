import requests
import datetime


def setupData():
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
    return [synoEntryItem]

def metaData(searchString, langCode, locale):
    # langCode - locale, title
    url = "https://uts-api.itunes.apple.com/uts/v2/search/incremental?sf={}&locale={}&caller=wta&utsk=0893ae2c4df5b61%3A%3A%3A%3A%3A%3Ac5a7986b1ef4302&v=34&pfm=desktop&q={}".format(langCode, locale, searchString)
    result = requests.get(url)
    shelves = result.json()["data"]["canvas"]["shelves"]

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

            releaseDate = datetime.datetime.fromtimestamp( ( item["releaseDate"] / 1000 ) )
            releaseDate = releaseDate.strftime('%Y-%m-%d')

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
            synoEntryItem = {
                "title": item["title"],
                "tagline": "",
                "original_available": releaseDate,
                "original_title": item["title"],
                "summary": item["description"],
                "certificate": item["rating"]["displayName"],
                "genre": ["GENRE"],
                "actor": ["ACTOR"],
                "director": ["DIRECTOR"],
                "writer": ["WRITER"],
                "extra": synoExtraItem
            }



            synoRes.append(synoEntryItem)

    return synoRes

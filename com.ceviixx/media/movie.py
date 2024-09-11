import requests
import datetime


def setupData():
    synoEntryItem = {
        "title": "TITLE",
        "tagline": "",
        "original_available": "2024-01-01",
        "original_title": "TITLE",
        "summary": "DESCRIPTION",
        "genre": ["Unknown"],
        "actor": ["Unknown"],
        "director": ["Unknown"],
        "writer": ["Unknown"]
    }
    return [synoEntryItem]



def _parsePoster(data):
    if "coverArt" in data:
        url = data["coverArt"]["url"]
        width = str(data["coverArt"]["width"])
        height = str(data["coverArt"]["height"])

        finalUrl = url
        finalUrl = finalUrl.replace("{w}", width)
        finalUrl = finalUrl.replace("{h}", height)
        finalUrl = finalUrl.replace("{f}", "jpg")

        return [finalUrl]
    else:
        return []

def _parseBackdrop(data):
    if "previewFrame" in data:
        url = data["previewFrame"]["url"]
        width = str(data["previewFrame"]["width"])
        height = str(data["previewFrame"]["height"])

        finalUrl = url
        finalUrl = finalUrl.replace("{w}", width)
        finalUrl = finalUrl.replace("{h}", height)
        finalUrl = finalUrl.replace("{f}", "jpg")

        return [finalUrl]
    else:
        return []

def _parseGenres(data):
    genres = []
    for item in data:
        genres.append(item["name"])
    return genres

def _parseReleaseDate(data):
    releaseDate = datetime.datetime.fromtimestamp( ( data / 1000 ) )
    return releaseDate.strftime('%Y-%m-%d')

def _parseActor(data):
    actors = []
    for item in data:
        if item["type"] == "Voice" or item["type"] == "Actor":
            actors.append(item["personName"])

    return actors

def _parseDirector(data):
    directors = []
    for item in data:
        if item["type"] == "Director":
            directors.append(item["personName"])
    return directors

def _parseWriter(data):
    writers = []
    for item in data:
        if item["type"] == "Writer":
            writers.append(item["personName"])
    return writers



def detailsFor(entryId):
    url = "https://tv.apple.com/api/uts/v2/view/product/{}/?utscf=OjAAAAAAAAA~&utsk=000000000000000000&caller=web&sf=143443&v=40&pfm=web&locale=de-DE".format(entryId)
    
    resp = requests.get(url)
    if resp.status_code != 200:
        exit("Response not valid for {}".format(entryId))
    
    j = resp.json()
    content = j["data"]["content"]
    roles = j["data"]["roles"]

    title = content["title"]
    description = content["description"]
    releaseDate = _parseReleaseDate(content["releaseDate"])
    genres = _parseGenres(content["genres"])
    certificate = content["rating"]["displayName"]

    rating = 0
    if "tomatometerPercentage" in content:
        rating = content["tomatometerPercentage"]

    actor = _parseActor(roles)
    director = _parseDirector(roles)
    writer = _parseWriter(roles)

    images = content["images"]
    poster = _parsePoster(images)
    backdrop = _parseBackdrop(images)

    synoExtraItem = {
        "com.appletv": {
            "rating": {
                "com.rottentomatoes": rating
            },
            "poster": poster,
            "backdrop": backdrop
        }
    }
    synoEntryItem = {
        "title": title,
        "tagline": "",
        "original_available": releaseDate,
        "original_title": title,
        "summary": description,
        "certificate": certificate,
        "genre": genres,
        "actor": actor,
        "director": director,
        "writer": writer,
        "extra": synoExtraItem
    }

    return synoEntryItem

    




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
            if "id" not in item:
                continue

            entryId = item["id"]
            if ".bun." in entryId or ".cpc." in entryId:
                continue
            
            detailData = detailsFor(entryId)
            synoRes.append(detailData)
            """
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
            """
    return synoRes

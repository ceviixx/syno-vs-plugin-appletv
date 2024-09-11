import requests
import datetime

def setupData():
    synoEntryItem = {
        "title": "title",
        "original_available": "1970-01-01",
        "original_title": "title",
        "summary": "summary",
        "extra": {
            "con.synology.TheMovieDB": {
                "poster": ["http://localhost/test.jpg"],
                "backdrop": ["http://localhost/test.jpg"]
            }
        }
    }
    return [synoEntryItem]


def metaData(searchString, season, episode, langCode, locale):
    synoRes = []
    synoExtraItem = {
        "com.appletv": {
            "rating": {
                "com.rottentomatoes": 10.0
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


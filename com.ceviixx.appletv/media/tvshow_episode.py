import requests
import datetime

def setupData():
    synoEntryItem = {
        "title": "title",
        "tagline": "tagline",
        "original_available": "1970-01-01",
        "summary": "summary",
        "certificate": "12",
        "genre": ["Unknown"],
        "actor": ["Unknown"],
        "director": ["Unknown"],
        "writer": ["Unknown"],
        "season": 1,
        "episode": 1,
        "extra": {
            "com.synology.TheMovieDB": {
                "tvshow": {
                    "title": "title",
                    "original_available": "1970-01-01",
                    "original_title": "title",
                    "summary": "summary",
                    "extra": {
                        "com.synology.TheMovieDBExample": {
                            "poster": ["http://localhost/test.jpg"],
                            "backdrop": ["http://localhost/test.jpg"]
                        }
                    }
                },
                "poster": ["http://localhost/test.jpg"],
                "raiting": {
                    "com.tomatos": 2.0
                }
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


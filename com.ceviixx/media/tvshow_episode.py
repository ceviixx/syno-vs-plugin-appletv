import requests
import datetime

def setupData():
    synoExtraItem = {
       "com.synology.TheMovieDb": {
           "tvshow": {
               "title": "",
               "original_available": "1970-01-01",
               "original_title": "",
               "summary": "",
               "extra": {
                   "com.synology.TMDBExample": {
                       "poster": ["http://localhost/test.jpg"],
                       "backdrop": ["http://localhost/test.jpg"]
                   }
               }
            },
            "poster": ["http://localhost/test.jpg"],
            "rating": {
                "com.synology.TheMovieDb": 7.9
            }
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
        "season": 1,
        "episode": 1,
        "extra": synoExtraItem
    }
    return [synoEntryItem]


def metaData(searchString, season, episode, langCode, locale):
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


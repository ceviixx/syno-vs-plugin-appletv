import requests
import datetime

def setupData():
    synoExtraItem = {
        "com.ceviixx": {
            "poster": ["http://localhost.com/test.jpg"],
            "backdrop": ["http://localhost.com/test.jpg"]
        }
    }
    synoEntryItem = {
        "title": "TITLE",
        "original_available": "2024-01-01",
        "original_title": "TITLE",
        "summary": "DESCRIPTION",
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


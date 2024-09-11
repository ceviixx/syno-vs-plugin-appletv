
### getLocale(value)
def getLocale(value):
    if value == "ger":
        return "de-DE"
    else:
        return "-"

### getLangCode(value)
def getLangCode(value):
    if value == "ger":
        return "143443"
    else:
        return "-"

### errorData()
def errorData():
    synoRes = []
    synoExtraItem = {
        "ceviixx.appletv": {
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

### errorDataDisplay(requestType)
def errorDataDisplay(requestType):
    synoExtraItem = {
        "ceviixx.appletv": {
            "rating": {
                "com.rottentomatoes": 2.0
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

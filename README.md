# Synology Video Station Plugin
An Synology Video Station Plugin to fetch movie metdata from the **Apple TV**-API.

# Test & build
```
tar --no-xattrs -cvf com.ceviixx.tar com.ceviixx
```
```
clear; sh plugin/com.ceviixx/loader.sh  --type movie --lang ger --input "{\"title\":\"Toy Story\", \"original_available\": \"1995-11-22\"}" --limit 1 --allowguess
false
```

**Synology Video Station Plugin Docu can be find [here](https://download.synology.com/download/Document/Software/DeveloperGuide/Package/VideoStation/All/enu/Synology_Video_Station_API_enu.pdf).**



## Supported media types
- [x] Movies
- [ ] TV-Shows
- [ ] TV-Episodes


## Supported languages
- [x] German
- [ ] English
- [ ] ...



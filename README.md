# Synology Video Station Plugin
An Synology Video Station Plugin to fetch movie metadata from the **Apple TV**-API.

### Test & build
```
sh ceviixx.appletv/run.sh  \
    --type movie \
    --lang ger \
    --input "{\"title\":\"Toy Story\", \"original_available\": \"1995-11-22\"}" \
    --limit 1 \
    --allowguess false
```

```
tar --no-xattrs -cvf ceviixx.appletv.tar ceviixx.appletv
```



### Supported media types
- [x] Movies
- [ ] TV-Shows


### Supported languages
- [x] Danish (dan)
- [x] German (ger)
- [x] English (enu)
- [x] Spanish (spn)
- [x] French (fre)
- [x] Italian (ita)
- [x] Hungarian (hun)
- [x] Nederlands (nld)
- [x] Norwegian (nor)
- [x] Polish (plk)
- [x] European Portuguese (ptg)
- [x] Brazilian Portuguese (ptb)
- [x] Swedish (sve)
- [x] Turkish (trk)
- [ ] Czech (csy)
- [x] Russian (rus)
- [ ] Thai (tha)
- [x] Japanese (jpn)
- [x] Simplified Chinese (chs)
- [x] Traditional Chinese (krn)
- [x] Korean (krn)



**Synology Video Station Plugin Docu can be find [here](https://download.synology.com/download/Document/Software/DeveloperGuide/Package/VideoStation/All/enu/Synology_Video_Station_API_enu.pdf).**

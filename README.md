# Synology Video Station Plugin
An Synology Video Station Plugin to fetch movie metadata from the **Apple TV**-API.

### Test & build
```
tar --no-xattrs -cvf com.ceviixx.tar com.ceviixx
```
```
sh com.ceviixx/run.sh  \
    --type movie \
    --lang ger \
    --input "{\"title\":\"Toy Story\", \"original_available\": \"1995-11-22\"}" \
    --limit 1 \
    --allowguess false
```


### Supported media types
- [x] Movies
- [ ] TV-Shows


### Supported languages
- [ ] Danish (dan)
- [x] German (ger)
- [ ] English (enu)
- [ ] Spanish (spn)
- [ ] French (fre)
- [ ] Italian (ita)
- [ ] Hungarian (hun)
- [ ] Nederlands (nld)
- [ ] Norwegian (nor)
- [ ] Polish (plk)
- [ ] European Portuguese (ptg)
- [ ] Brazilian Portuguese (ptb)
- [ ] Swedish (sve)
- [ ] Turkish (trk)
- [ ] Czech (csy)
- [ ] Russian (rus)
- [ ] Thai (tha)
- [ ] Japanese (jpn)
- [ ] Simplified Chinese (chs)
- [ ] Traditional Chinese (krn)
- [ ] Korean (krn)



**Synology Video Station Plugin Docu can be find [here](https://download.synology.com/download/Document/Software/DeveloperGuide/Package/VideoStation/All/enu/Synology_Video_Station_API_enu.pdf).**

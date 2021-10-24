# Creates a list of urls for a web scraping project
# Store -> Model -> Trim

# Dealership URLs
jswr = "www.URL1.com"
jsof = "www.URL2.com"
sshi = "www.URL3.com"
wcgc = "www.URL4.com"

# URL Segment
srpurl = "VehicleSearchResults?search=new&model="

# Vehicle Models
eq = "Equinox"
cr = "Cruze"
co = "Colorado"
ma = "Malibu"
tr = "Traverse"

# Vehicle Trim Levels
fwdls = "&trim=FWD%20LS"
fwdlt = "&trim=FWD%20LT"
fwdpr = "&trim=FWD%20Premier"

# Lists made up of dealers, models, and trims
dealers = [jswr, jsof, sshi, wcgc]
models = [eq,cr,ma,tr]
trims = [fwdls,fwdlt,fwdpr]

for i in dealers:
  for j in models:
    for k in trims:
      print(i + srpurl + j + k)
      list1.append(i + srpurl + j + k)

outFile = open('url_list.txt', 'w')
outFile.write("\n".join(list1))
outFile.close()

import urllib.request as req

imgurl ="https://thispersondoesnotexist.com/image"

req.urlretrieve(imgurl, "image.jpg")

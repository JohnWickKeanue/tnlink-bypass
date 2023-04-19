import requests

url = "https://tnshort.in/9Sb4aK5"  
#https://link.tnlink.in/TS95D7
#https://tnshort.in/9Sb4aK5

def tnlink(url):
    code = url.split("/")[-1]
    xurl = f"https://page.tnlink.in/{code}"
    download = requests.get(xurl, stream=True, allow_redirects=False) 
    return download.headers["location"]
print(tnlink(url))

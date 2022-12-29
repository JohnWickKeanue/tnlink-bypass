import requests
print("Enter your tnlink url:")
url = input()  #@param {type:"string"}


def tnlink(url):
    client = requests.session()
    DOMAIN = "https://gadgets.earnme.club"
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    download = requests.get(final_url, stream=True, allow_redirects=False)
    return download.headers["location"]
    
# ---------------------------------------------------------------------------------------------------------------------
print(tnlink(url))

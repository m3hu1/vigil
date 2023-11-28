import requests

def checkRedirects(url):
    response = requests.get(url)
    if response.history:
        counter=1
        for redirect in (response.history):
            print(f"[{counter}] URL: {redirect.url}")
            print(f" ↓  Status Code: {redirect.status_code}")
            counter+=1
        print(f"Final URL: {response.url}")
        print(f"Final Status Code: {response.status_code}")
    else:
        print(f"{url} does not redirect.")

n = input("Enter the link: ")
print()
checkRedirects(n)
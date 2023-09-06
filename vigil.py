#Vigil - Under Construction
import requests
from urllib.parse import urlparse

def get_redirected_url(url):
    redirects = []
    while True:
        response = requests.head(url, allow_redirects=False)
        if response.status_code in (301, 302, 303, 307, 308):
            next_url = response.headers.get('Location')
            if not next_url:
                break
            redirects.append(url)
            url = next_url
        else:
            break
    return redirects, url

def main():
    input_url = input("Enter the URL: ")
    redirects, final_destination = get_redirected_url(input_url)
    
    print("Redirect Hops:")
    for i, redirect in enumerate(redirects):
        print(f"{i + 1}: {redirect}")
    
    print("Final Destination:")
    print(final_destination)

if __name__ == "__main__":
    main()
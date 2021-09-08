import requests

def main():
    print(requests.__version__ + "\n")
    
    googleHome = requests.get("http://www.google.com")
    print("Requesting to GET the Google homepage...")
    print("This is the headers of response:")
    print(googleHome.headers)
    print()


if __name__ == "__main__":
    main();
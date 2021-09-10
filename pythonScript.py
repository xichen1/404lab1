import requests

def main():
    # requests version
    print(requests.__version__ + "\n")

    # GET google homepage
    print("Requesting to GET the Google homepage...")
    googleHome = requests.get("http://www.google.com")
    print("This is the headers of response:")
    print(googleHome.headers)
    print()

    # download and print the file itself
    print("Downoading the script itself from github...")
    scriptFile = requests.get("https://raw.githubusercontent.com/xichen1/404lab1/master/pythonScript.py")
    print("This is the source code of the script file:")
    print(scriptFile.text)


if __name__ == "__main__":
    main()

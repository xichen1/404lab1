import requests

def main():
    print(requests.__version__ + "\n")

    print("Requesting to GET the Google homepage...")
    googleHome = requests.get("http://www.google.com")
    print("This is the headers of response:")
    print(googleHome.headers)
    print()

    print("Downoading the script itself from github...")
    scriptFile = requests.get("https://raw.githubusercontent.com/xichen1/404lab1/master/pythonScript.py")
    print("This is the source code of the script file:")
    print(scriptFile.text)


if __name__ == "__main__":
    main();
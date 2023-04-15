import requests
import os

directory = "securimage-data"

def main():
    if not os.path.exists(directory):
        os.mkdir(directory)
    s = requests.Session()
    for i in range(10000):
        if i % 200 == 0:
            print(i)
        securimage_show = s.get("http://localhost:8000/securimage_show.php")
        securimage_code = s.get("http://localhost:8000/securimage_code.php")

        with open("{}/{}.png".format(directory, securimage_code.text), "wb") as f:
            f.write(securimage_show.content)

if __name__ == "__main__":
    main()
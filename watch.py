import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(html):
    not_src = ".*?"
    https = "(https://)"
    www = r"www\."
    pattern = rf"{not_src}src=\"{https}{www}(.*?)\"{not_src}"
    if matches := re.search(pattern, html):
        youtube_url = matches.group(2)
        https = matches.group(1)
        _,_,last = youtube_url.split("/")
        new_youtube_url = f"{https}youtu.be/{last}"
        return new_youtube_url

if __name__ == "__main__":
    main()
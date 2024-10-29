import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(html):
    not_src = ".*?"
    https = "(?:https?://)"
    www = r"(?:www\.)?"
    pattern = rf"{not_src}src=\"{https}{www}.*?/embed/(.*?)\"{not_src}"
    if matches := re.search(pattern, html):
        yt_vid_id = matches.group(1)
        return f"https://youtu.be/{yt_vid_id}"

if __name__ == "__main__":
    main()
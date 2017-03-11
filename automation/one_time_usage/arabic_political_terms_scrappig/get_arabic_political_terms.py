#! python3
# coding=utf-8

import random
import bs4
import urllib3

urllib3.disable_warnings()

def load_user_agent(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1 - 1])
    random.shuffle(uas)
    return uas


def main():
    cwd = "/Users/anas/projects/main_private_repo/task_automation/"

    user_agents = load_user_agent(uafile=cwd + "user_agents")
    header = {
        "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "ACCEPT_ENCODING": "gzip, deflate, sdch, br",
        "CACHE_CONTROL": "max-age=0",
        "Connection": "close",
        "User-Agent": user_agents[0].decode("utf-8"),
        "ACCEPT_LANGUAGE": "en-US,en;q=0.8,de-DE;q=0.6,de;q=0.4,ar;q=0.2,fr;q=0.2"
    }

    http = urllib3.PoolManager(10, headers=header)
    base_url = "http://arabic.desert-sky.net/m_govt.html"
    main_page = http.request("GET", base_url, timeout=urllib3.Timeout(connect=5.0, read=20.0))

    arabic_words_tags = bs4.BeautifulSoup(main_page.data, "html.parser").findAll("span", {"class": "arabic"})

    with open('arabic_words.txt', 'w') as f:
        for tag in arabic_words_tags:
            word = tag.getText()
            tmp = word.split(' (ج) ')
            tmp_more = [item.split(' | ') for item in tmp]

            tmp_stripped = [item.strip() for sublist in tmp_more for item in sublist]
            new_words=('|'.join(tmp_stripped))
            print(new_words)
            f.write(new_words.strip())
            f.write("|")
    f.close()


    exit(0)


# def main():
#     cwd = "/Users/anas/projects/main_private_repo/task_automation/"
#
#     user_agents = load_user_agent(uafile=cwd + "user_agents")
#     header = {
#         "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#         "ACCEPT_ENCODING": "gzip, deflate, sdch, br",
#         "CACHE_CONTROL": "max-age=0",
#         "Connection": "close",
#         "User-Agent": user_agents[0].decode("utf-8"),
#         "ACCEPT_LANGUAGE": "en-US,en;q=0.8,de-DE;q=0.6,de;q=0.4,ar;q=0.2,fr;q=0.2"
#     }
#
#     http = urllib3.PoolManager(10, headers=header)
#     urls = []
#
#     with open('dropbox2.txt.unique', 'r') as drps:
#         urls =  drps.read().splitlines()
#
#     print(urls)
#
#     for url_ in urls:
#         main_page = http.request("GET", url_, timeout=urllib3.Timeout(connect=5.0, read=20.0))
#         print(main_page)
#
#         data = bs4.BeautifulSoup(main_page.data, "html.parser")
#
#         file_name = url_[url_.rindex('/'): url_.index('?')]
#         print('downloading ' + file_name+ ' ...')
#
#         with open(cwd + '/swedish' + file_name, "wb") as f :
#             f.write(data)
#             f.close()
#
#     exit(0)


if __name__ == "__main__":
    main()

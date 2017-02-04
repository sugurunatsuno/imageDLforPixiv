import pixivpy3
import json
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='image download from pixiv')
parser.add_argument("--user_id", type=int, default=None)
parser.add_argument("--path", type=str, default=None)
parser.add_argument("--userdata_json", type=str, default=None)
parser.add_argument("--score", type=int, default=700)

args = parser.parse_args()

with open(args.userdata_json, "r") as f:
    userdata = json.load(f)

save_path = args.path


def imageDlFromUserId(user_id, path, username, password, score=700):
    papi = pixivpy3.PixivAPI()
    papi.login(username, password)

    res = papi.users(user_id)
    work_num = res['response'][0]['stats']['works']
    json_result = papi.users_works(user_id, per_page=work_num)

    aapi = pixivpy3.AppPixivAPI()
    for work in json_result["response"]:

        sleep(1)

        if work['stats']['score'] < score:
            continue

        #もし一つの記事に複数枚あるならそれを全部取得
        if work['is_manga']:
            for i in range(work['page_count']):
                url = work["image_urls"]['large'][0:-5] + str(i) + work["image_urls"]['large'][-4:]
                print("\r"+url)
                aapi.download(url, path)

        else:
            url = work["image_urls"]['large']
            print("\r"+url)
            aapi.download(url, path)

imageDlFromUserId(args.user_id, args.path, userdata["username"], userdata["password"], args.score)

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

#ログイン
papi = pixivpy3.PixivAPI()
#username, password
papi.login(userdata["username"], userdata["password"])

user_id = args.user_id

#そのユーザーの全ての記事を取得
res = papi.users(user_id)
work_num = res['response'][0]['stats']['works']
json_result = papi.users_works(user_id, per_page=work_num)

#ダウンロード用のAPIのインスタンス作成
aapi = pixivpy3.AppPixivAPI()

#取得した記事のループ
for work in json_result["response"]:

    sleep(1)

    if work['stats']['score'] < args.score:
        continue

    #もし一つの記事に複数枚あるならそれを全部取得
    if work['is_manga']:
        for i in range(work['page_count']):
            url = work["image_urls"]['large'][0:-5] + str(i) + work["image_urls"]['large'][-4:]
            print("\r",url)
            aapi.download(url, save_path)

    else:
        url = work["image_urls"]['large']
        print("\r",url)
        aapi.download(url, save_path)

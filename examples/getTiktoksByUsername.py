from TikTokApi import TikTokApi

api = TikTokApi()

count = 10

tiktoks = api.byUsername('definitelynotjakez', count=count)

for tiktok in tiktoks:
    print(tiktok)
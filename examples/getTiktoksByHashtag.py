from TikTokApi import TikTokApi

api = TikTokApi()

count = 30

tiktoks = api.byHashtag('NJ', count=count)

for tiktok in tiktoks:
    print(tiktok)
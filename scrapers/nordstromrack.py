import requests
import json

r = requests.get("https://www.nordstromrack.com/api/ecomcp/public/pages/04dfeab6-38a0-4aa6-b206-16b6f20687b0/catalog?department=Shoes&division=Women&includeFlash=false&includePersistent=true&limit=99&page=1&sort=most_popular")
shoes = json.loads(r.content)
print(shoes["total"])
page_num = int(shoes["_links"]["last"]["href"].split("page=")[1])
shoe_count, size_count = 0, 0
for page in range(1, page_num):
    page_link = "https://www.nordstromrack.com/api/ecomcp/public/pages/04dfeab6-38a0-4aa6-b206-16b6f20687b0/catalog?department=Shoes&division=Women&includeFlash=false&includePersistent=true&limit=99&page="+str(page)+"&sort=most_popular"
    r = requests.get(page_link)
    shoes = json.loads(r.content)
    for shoe in shoes["_embedded"]["http://hautelook.com/rels/products"]:
        # print(shoe["name"])
        shoe_count += 1
        for size in shoe["_embedded"]["http://hautelook.com/rels/skus"]:
            if size["standard_size"] == "12":
                size_count += 1
                print(shoe["name"], shoe["brand_name"])
print("total shoes: ", shoe_count)
print("total size 12 shoes: ", size_count)

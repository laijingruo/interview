import random
import re
import time
import json
# from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

js = 1
fy = 0
all_products = []
while js <= 48:
  url = f"https://api.nike.com.cn/cic/browse/v2?queryid=products&anonymousId=DSWX4D6A387147570D8AF4F741964CF9CFE9&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D{fy}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D"

  payload = {}
  headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'if-none-match': 'W/"14cc7-Fy5YwhOH2iF2GaU8R+8s9+6yIII"',
    'origin': 'https://www.nike.com.cn',
    'priority': 'u=1, i',
    'referer': 'https://www.nike.com.cn/',
    'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
    'Cookie': 'geoloc=cc=CN; sajssdk_2015_cross_new_user=1; anonymousId=DSWX4D6A387147570D8AF4F741964CF9CFE9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22DSWX4D6A387147570D8AF4F741964CF9CFE9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fmail.qq.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk3YWEwMGE1OTY0YmEtMDAxYzA1ZTY0YjZlMzIyNi00YzY1N2I1OC0xMzI3MTA0LTE5N2FhMDBhNTk3MmMzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22197aa00a5964ba-001c05e64b6e3226-4c657b58-1327104-197aa00a5972c3%22%7D; ppd=pw|nikecom>pw>no%20page%20title; acw_tc=0a27a99417509063282796670e0064582a4cf5407bcf97692dabef1406cd9f; sensorsdata2015jssdksession=%7B%22session_id%22%3A%22197aa00ac936f30d83ea5e40c1484c657b581327104197aa00ac94cc8%22%2C%22first_session_time%22%3A1750903860370%2C%22latest_session_time%22%3A1750906430962%7D; tfstk=gXIoNLG0Ua87g_Vvkit777CPlCzxo3tBy6np9HdUuIRjwbnRLwqha1YF23BRoBfDGbdPx9iHL95QFBe7kT6WAHPT6MqOFTi3PCS8MHyF3HpnlPBFHT6WAxTiAi0OFvbbB78yY6-2udp9YXRyL-x2pp-E4eorujRXgHJEzDo2gdpkU08PTtyDdIJyYU5e0-vIMEayNMSV0SeBA-4kHtIDEUAN3PiExho9rCWkiDkNrLxW_TRmYDAGsRYhnTFoftK5Y1vOwools9W18Ejng5ACmtSP8tGu3hXckNLlo7oHMgpH7H8mLDWDYa1G0hrZiK_VewS5ZvmeFgI9-CT0LDTp0GLN7_DQCt-yL6T1v5iWa9W1fNKgqf9luOxc4-3q7MgZAKyd02gBzK9D6TPXFJAsId9an-0adUJXFCe0n2MDzK9DC-2mSHLyhL0V.; ssxmod_itna=eqUx9DnDB7qYqDKi=DXiq8r4xgDTrC3COt3ODl=WxA5D8D6DQeGTW0diWrtk3eA9D7IQbe8DPqefm74PxeYhGb5KDHxY=DUonxpTD4+KGwD0eG+DD4DWDmmFDnxAQDjxGpnXvTs=DEDmb8DWPDYxDrE=KDRxi7DDvd7x07DQ5kiDDzijO5DYe7YeAh7EACb4viKt0DExG1W40HbDdeEg7ju4xzKISfVhR7DlF0DCK1RpvFb4GdjEH1V6ubtGDPS74PbA+iqQ44iCWcqC2I3QGiiGhiCurNen6H7WpcDDcDEk1K4D; ssxmod_itna2=eqUx9DnDB7qYqDKi=DXiq8r4xgDTrC3COt3D618AiYx0vT403DuBiYLiTNBtYqAP5RiDdBX+qx/wIXwcQ3mAupTEPl8uLashYAHqUmljBXfPEO7jeX3mB0p0siI3ndiXqS6WoBBSqRDO4koulfYG98YeXkAI0dAPwTEszrfu/wQHALfxzCtOCDttO8uvY0nfWYc3umtexchHY138d+To26Use6tpWiKZReRO5e77237YInrYDzD9RCDP78XsbBfxinrpwkQ8ATkKqIDtBPhrq9TSBBTOAMp3aXvPayEh+NWOB0EH=bbi1LG=phDNvGm/=pDI0HWiP/tLQ0K42mQ0ID36QinAr2D2Hm=AQIheI2Gixc3rKboS4XBNCQbHCRxg+v=TOI2bg0+m5ADR=bvIQmCbrwn3iKKsRiHCPSeIsGiiRN5trq4fNSrKz4DQ9RD08DiQYYD=; acw_tc=ac11000117509050675852959e00638d79c01810246e2032fdf1e2bd4fdf7d'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  data_list = response.json().get("data")["products"]["products"]
  for data in data_list:
    product_info = {}
    title = data["title"]
    price = f"{data['price']['currency']}:{data['price']['currentPrice']}"
    color = []
    img_urls = []
    for a in data['colorways']:
      color.append(a['colorDescription'])
      img_urls.append(a['images']['portraitURL'])
    url = f"https://www.nike.com.cn{data['url'].replace('{countryLang}', '')}"
    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")
    details = soup.find("div", class_="pt7-sm").find("p").text
    sku = url.split('/')[-1]
    pattern = r"-([a-zA-Z0-9]*)/"
    match = re.search(pattern, url)
    code = match.group(1) if match else None
    url = f"https://api.nike.com.cn/discover/product_details_availability/v1/marketplace/CN/language/zh-Hans/consumerChannelId/d9a5bc42-4b9c-4976-858a-f159cf99c647/groupKey/{code}"
    # print(url)
    headers = {
      'accept': '*/*',
      'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
      'nike-api-caller-id': 'com.nike.commerce.nikedotcom.web',
      'origin': 'https://www.nike.com.cn',
      'priority': 'u=1, i',
      'referer': 'https://www.nike.com.cn/',
      'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
      'Cookie': 'acw_tc=dcb5422617509256480454879ef56c88d235277e9a439d54b2e329ffba; cdn_sec_tc=dcb5422617509256480454879ef56c88d235277e9a439d54b2e329ffba'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response)
    sizes = response.json().get("sizes")
    size_list = []
    for size in sizes:
      if size["productCode"] == sku:
        if size["availability"]["isAvailable"] == True:
          size_list.append(f"{size['localizedLabel']}在售")
        else:
          size_list.append(f"{size['localizedLabel']}售罄")

    product_info["title"] = title
    product_info["price"] = price
    product_info["color"] = color
    product_info["size"] = size_list
    product_info["sku"] = sku
    product_info["details"] = details
    product_info["img_urls"] = img_urls
    all_products.append(product_info)

    print(f"title:{title},price:{price},color:{color},size:{size_list},sku:{sku},details:{details},img_urls:{img_urls}")
    js += 1
    time.sleep(random.randint(1, 3))
  fy += 24

with open('nike_products.json', 'w', encoding='utf-8') as f:
  json.dump(all_products, f, ensure_ascii=False, indent=4)
print("数据已保存到 nike_products.json 文件")



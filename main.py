import requests

headers = {
    'authority': 'yuchen.tonghuaios.com',
    'sec-ch-ua': '"Chromium";v="96", " Not A;Brand";v="99"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.97 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://yuchen.tonghuaios.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://yuchen.tonghuaios.com/',
    'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8,zh-Hans;q=0.7',
    'cookie': 'wordpress_sec_3fded9bb7b81e244ce750634dc5801ae=W170653759061%7C1706766777%7CoL2BNNPxv0Hd4NQAQJ8ch7ww4S6VfDd7gYqqIE3Vh74%7C894f2e084b4d035a739dde102eaa637f25890bdb8253e6fded0d4d4e103d8562; pps_cookie_431=3_days; chenxing_logged_in_redirect_https://yuchen_tonghuaios_com=https%253A%252F%252Fyuchen.tonghuaios.com%252Fusers%253Ftab%253Dcredit; wordpress_logged_in_3fded9bb7b81e244ce750634dc5801ae=W170653759061%7C1706766777%7CoL2BNNPxv0Hd4NQAQJ8ch7ww4S6VfDd7gYqqIE3Vh74%7Cd692ac3915b41ed8256f644fa343edda66308d88fa2cb1fca0e6b81382504ffb',
}

data = {
  'action': 'daily_sign'
}

response = requests.post('https://yuchen.tonghuaios.com/wp-admin/admin-ajax.php', headers=headers, data=data)

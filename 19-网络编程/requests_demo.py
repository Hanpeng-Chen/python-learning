import requests

def main():
    resp = requests.get('http://api.help.bj.cn/apis/weather/?id=101230201')
    data = resp.json()
    print(data)

if __name__ == '__main__':
    main()
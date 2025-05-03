import requests
import csv
import time
from DrissionPage import ChromiumPage
def tt(shij):
    import datetime

    timestamp = shij
    # 使用fromtimestamp方法将时间戳转换为datetime对象
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    return str(dt_object)
    #print("转换后的日期和时间为:", dt_object)
def jj():
    from datetime import datetime, timedelta
    start_date = datetime(2025, 6, 2)
    end_date = start_date + timedelta(days=30)
    if start_date > end_date:
        return
    else:
        current_date = datetime.now()
        page = ChromiumPage()
        page.get('https://amae-koromo.sapk.ch/player/13415180/9/luck')

        page.listen.start('data.amae-koromo.com/api/v2/pl4/player_records')

        page.wait(2)  # 停顿
        timeout = 5  # 设置超时时间为 5 秒
        last_response_time = time.time()

        while True:
            if time.time() - last_response_time > timeout:
                print("五秒内无数据加载，程序结束。")
                break
            page.scroll.to_bottom()  # 下滑
            page.wait(2)
            try:
                rpk = page.listen.wait(timeout=1)
                last_response_time = time.time()
                response = rpk.response.body
                # print(response)
                for i in response:
                    a1 = i['uuid']
                    shijs = tt(i['startTime'])
                    for uu in i['players']:
                        a2 = uu['nickname']

                        dic = {}
                        dic['名字'] = a2
                        dic['时间'] = shijs
                        dic['点数'] = uu['score']
                        dic['链接'] = f'https://game.maj-soul.com/1/?paipu={a1}'

                        lst = []

                        lst.append(dic)
                        print(dic)
                        with open(f'模版.csv', 'a+', encoding='utf-8-sig', newline='') as f:
                            write = csv.DictWriter(f, fieldnames=['名字','时间','点数', '链接'])  # 创建表头
                            with open(f'模版.csv', 'r', encoding='utf-8-sig', newline='') as ec:
                                if len(ec.readline()) == 0:
                                    write.writeheader()  # 写入表头
                                write.writerows(lst)  # 写入内容
            except:
                print('运行结束')
                return
        #continue
jj()
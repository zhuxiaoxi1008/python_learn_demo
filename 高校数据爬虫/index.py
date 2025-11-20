import requests
from bs4 import BeautifulSoup
import json
# pip3 install requests beautifulsoup4

def get_tsinghua_colleges():
    url = "https://www.zhijiao.cn/mingdan.shtml"
    
    try:
        # 发送HTTP请求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'  # 确保中文编码正确

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 示例：提取清华大学的学院列表（根据实际网页结构调整选择器）
        college_elements = soup.select('.province a')

        # 地区链接列表
        link_list = []

        # 存储学校列表
        college_list = []
        for linkEl in college_elements:
            # print(linkEl.get('href'))
            link_list.append(linkEl.get('href'))

        for link in link_list:
            sub_response = requests.get(link, headers=headers, timeout=10)
            sub_response.encoding = 'utf-8'  # 确保中文编码正确

            # # 解析HTML
            sub_soup = BeautifulSoup(sub_response.text, 'html.parser')

            college_elements_trs = sub_soup.select('table tbody tr')
            # print(college_elements_trs)

            for tr in college_elements_trs[2:]:
                tds = tr.select('td')
                college_item = {
                    "id": tds[2].get_text(strip=True),
                    "value" : tds[1].get_text(strip=True),
                }
                college_list.append(college_item)

        filename = "colleges.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(college_list, f, ensure_ascii=False, indent=2)

        print("数据已保存到 %s", filename)       
        
        """ for elem in college_elements:
            college_name = elem.get_text(strip=True)
            if college_name:  # 过滤空值
                colleges.append(college_name)

        # 结构化数据
        university_data = {
            "name": "清华大学",
            "colleges": colleges
        }

        # 保存为JSON
        with open('tsinghua_colleges.json', 'w', encoding='utf-8') as f:
            json.dump(university_data, f, ensure_ascii=False, indent=2)

        print("数据已保存到 tsinghua_colleges.json")
        return university_data """

    except Exception as e:
        print(f"爬取失败: {e}")
        return None

# 执行爬取
if __name__ == "__main__":
    data = get_tsinghua_colleges()
    if data:
        print(json.dumps(data, ensure_ascii=False, indent=2))
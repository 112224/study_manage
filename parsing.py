import bs4
import requests

def reader():
    names = []


def baekjoon_parser(names, problems):
    base_url = "https://www.acmicpc.net/status?"

    data = []
    for name in names:
        row = [name]
        for problem in problems:
            problem_id = 'problem_id=' + str(problem)
            user_id = 'user_id='+str(name)
            url = base_url + problem_id + '&' + user_id
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.content, "html.parser")
            results = soup.find('table', {'class': "table table-striped table-bordered"}).tbody
            results = results.find_all('td', {'class': 'result'})

            if not results:
                row.append(-1)
                continue
            solve_flag = 0
            for link in results:
                answer = link.find('span', {'class' : 'result-text'}).text
                if '맞았습니다!!' == answer:
                    solve_flag = 1
                    break
            row.append(solve_flag)
        data.append(row)
    return data



print(baekjoon_parser(names=['112224', 'ans4572'], problems=[1005, 11779]))

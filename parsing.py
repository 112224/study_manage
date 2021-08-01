import bs4
import requests


def reader():
    names = []
    with open('participants', 'r') as f:
        names.extend(f.readline().split())

    # 해당 부분 수정 예정 ex) key 라는 파일에서 현재 주차에 해당하는 숫자를 가져옴
    # 아니면 문제에 해당하는 파일이 commit 된 경우 바뀌게?
    problems = []
    with open('1week', 'r') as f:
        problems.extend(f.readline().split())
    return names , problems


def writer(api, parser_data):
    print('api : ', api)
    print('parser_data : ', parser_data)
    with open('state.md','w') as f:
        content = '|    | '
        for _id, title, level in api:
            content += f'<img height="25px" width="25px" src="https://static.solved.ac/tier_small/{level}.svg"/>'
            content += f'[{title}](https://www.acmicpc.net/problem/{_id}) | '
            print(content)
        f.write(content + '  \n')
        for_table = '|:----:|' + ':----:|' * len(api) + '  \n'
        f.write(for_table)
        for ele in parser_data:
            content = f'| {ele[0]} |'
            for flag in ele[1:]:
                if flag == 0:
                    content += ' WA |'
                elif flag == -1:
                    content += ' not yet |'
                else:
                    content += ' AC |'
            f.write(content + '  \n')


def solved_api(problems):
    base_url = "https://solved.ac/api/v3/problem/show?problemId="
    header = {'Content-type': 'application/json'}
    # <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/>
    # [요세푸스 문제](https://www.acmicpc.net/problem/1158)
    data = []
    for problem in problems:
        url = base_url + str(problem)
        res = requests.get(url, header)
        if res.status_code == 200:
            json = res.json()
            data.append((problem, json['titleKo'], json['level']))
    return data


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


if __name__ == '__main__':
    names, problems = reader()
    print(baekjoon_parser(names, problems))
    solved_api(problems)
    writer(solved_api(problems), baekjoon_parser(names, problems))
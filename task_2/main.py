import json

def report(path: str):
    result = {} # создадим словарь для хранения данных
    with open(path, 'r') as file:
        data = json.load(file)
    # по ключу "vulnerabilities" добавим список, который будет содержать название уязвимости и число доказательств ее проявления для каждой найденной уязвимости
    result['vulnerabilities'] = [{'name': vulnerability['name'], 'count': vulnerability['count']} for vulnerability in data['site'][0]['alerts']]
    with open('task_2/result_report.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

def main():
    path = 'task_2/report.json'
    report(path=path)

if __name__ == '__main__':
    main()
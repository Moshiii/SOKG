import json


def process(filename):
    with open(filename, 'r') as jsonFile:
        data = json.load(jsonFile)
        di = {}
        for key in data:
            a = key.split('/')
            di[a[0]] = a[1:len(a)]

    with open('verbList.json', 'w') as fp:
        json.dump(di, fp, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    filename = 'p_pattern_for_category.json'
    process(filename)

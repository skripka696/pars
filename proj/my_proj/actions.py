import json


def f():

    # f = open('domiki.json', 'r')
    #
    # # a = []
    # for line in f:
    #     # a.append(line)
    #     print line
    # # print '11111111111111'
    # # print f.read()

    with open("domiki.json") as json_file:
        json_data = json.load(json_file)
    return json_data

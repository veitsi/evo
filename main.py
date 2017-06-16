import string
from pprint import pprint


def optimize_data(template, data):
    def review(data):
        for k in list(data):
            value = data[k]
            del data[k] #print ('try to delete ', k)
            try:
                template.format(**rootdata)
            except KeyError: #print ('oops, we need it')
                data[k]=value
                if type(data[k]) is dict:
                    review(data[k])
            else: # print ('cool. we dont need ', k)
                pass
    rootdata=data
    review(data)
    return data


def main():
    template = 'Python version: {languages[python][latest_version]}'
    data = {
        'languages': {
            'python': {
                'latest_version': '3.6',
                'site': 'http://python.org',
            },
            'rust': {
                'latest_version': '1.17',
                'site': 'https://rust-lang.org',
            },
        },
    }
    print("Original data:")
    pprint(data)

    new_data = optimize_data(template, data)
    print("Optimized data:")
    pprint(new_data)


if __name__ == '__main__':
    main()

def leaves(dictionary):
    for k in list(dictionary):
        if type(dictionary[k]) is not dict:
            print (k, dictionary[k])
            del dictionary[k]
        else:
            leaves(dictionary[k])
            if dictionary[k] == {}:
                del dictionary[k]


def optimize_data(template, data):
    def review(data):
        print (data)
        for k in list(data):
            value = data[k]
            del data[k] #print ('try to delete ', k)
            try:
                template.format(**rootdata)
            except KeyError: #print ('oops, we need it')
                data[k]=value
                if type(data[k]) is dict:
                    review(data[k])
            else: # print ('cool. we dont need it', k)
                pass
    rootdata=data
    review(data)
    print (data)



# except KeyError:
# p = {'meaning':42, 'meta': { 'author':'Doug','year':1970} }

if __name__ == '__main__':
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
        'animals': ['cow', 'penguin'],
    }
    template =    (
        'Python version: {languages[python][latest_version]}\n'
        'Python site: {languages[python][site]}\n'
        'Rust version: {languages[rust][latest_version]}\n'
    )
    # print(data)
    optimize_data(template, data)
    # print(data)

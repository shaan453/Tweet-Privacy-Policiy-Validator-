from iohandler import *
from analysis import *

if __name__ == '__main__':
    m = iohandler()
    link = m.take_input()
    link_data = m.make_request(link)
    analyst = analysis()
    result = analyst.checking(link_data)
    if result is True:
        print('This is an abusive words in your sentence.')
    else:
        print('Nice, friend.')
    

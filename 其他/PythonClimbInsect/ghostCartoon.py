# -*- coding:utf8 -*-
#!/usr/bin/python
from ghost import Ghost

class FetcherCartoon:
    def getCartoonUrl(self,url):
        
        if url is None:
                return false
        #todo many decide about url
        
        ghost = Ghost()
        #open webkit
        ghost.open(url)
        #exceute javascript and get what you want 
        result, resources = ghost.evaluate("document.getElementById('cpimg').getAttribute('src');")
        del resources
        return result

if __name__ == "__main__":
    url = 'http://www.1kkk.com/ch1-93986/'
    result = None
    fetcher = FetcherCartoon()

    result = fetcher.getCartoonUrl(url)
    print result

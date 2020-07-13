from html.parser import HTMLParser
from django.apps import apps
import urllib.request
import threading

"""
Класс при создании принмает теги URL которые необходимо обработать,
метод feed принимает html и возврает значения в виде словаря, где ключи теги, а значения ключей, данные тегов

"""




class MyHtmlParser(HTMLParser):
    def __init__(self, *tags, getEncoding=True):
        self._getEncoding = getEncoding
        self._result = {}
        self._starttag = ""
        self._data = ""
        self._innerTagCounter = False
        for tag in tags:
            self._result.setdefault(tag, [])
        if getEncoding:
            self._result["charset"] = ""
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag in self._result.keys():
            self._starttag = tag

        if self._getEncoding and attrs != [] and tag == "meta":
            self._result["charset"] = self.getCharset(attrs)

    """
           Функция которой передаются атрибуты тега meta, ищет среди них значение charset
    """
    def getCharset(self, attrs):
        for attr in attrs:
            if attr[0] == "charset":
                self._getEncoding = False
                return attr[1]

        strAtrrs = str(attrs)
        index = strAtrrs.find("charset")
        if index == -1:
            return None
        result = ""
        for chr in strAtrrs[index + len("charset="):]:
            if chr != "'" and chr != ";" and chr != ")":
                result += chr
            else:
                break
        self._getEncoding = False
        return result

    """
       Функция запускающаяся на данные между тегов, сохраняет это значение
    """
    def handle_data(self, data):
        if self._innerTagCounter:
            self._data += data
        elif self._starttag in self._result.keys():
            self._data = data
            self._innerTagCounter = True

    """
    Функция запускающаяся, когда встречается закрывающий тег, сохраняет данные в словарь
    """
    def handle_endtag(self, tag):
        if tag in self._result.keys():
            self._result[tag].append(self._data)
            self._innerTagCounter = False
            self._starttag = None


    def feed(self, data):
        super().feed(data)
        return self._result


"""
Функция создает парсер, получает html и отдает его парсеру
если не удается открыть URL возвращает False

"""
def getDataTags(url):
    try:
            fp = urllib.request.urlopen(url)
            bytesHtml = fp.read()
            html = bytesHtml.decode()
            fp.close()

    except:
        return False

    parcer = MyHtmlParser("title", "h1")
    return parcer.feed(html)


"""
Функция которая сохраняет в БД уже анализированные сайты
"""
def analyzeSite(site):
    data = getDataTags(site.url)
    ParsedSite = apps.get_model('sibparser',"ParsedSite")
    if data:
        title = attrListToStr(data["title"])
        h1 = attrListToStr(data["h1"])
        ParsedSite(title=title, h1=h1, encoding=str(data["charset"]), site=site).save()
    else:
        ParsedSite(site=site, successfully=False).save()

def attrListToStr(attrs):
    result = ""
    try:
        for attr in attrs:
            result += attr + " "
        return result
    except:
        return ""

"""
Функция запускает поток в котором обрабатывается URL
"""
def threadStart(site):
    delay = site.timeshiftMinutes * 60 + site.timeshiftSeconds
    t = threading.Timer(delay, analyzeSite, args=(site,))
    t.start()

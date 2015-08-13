# -*- encoding: utf-8 -*-
 
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from orphanage.items import OrphanageItem
 
class OrphanLoader(XPathItemLoader):
    default_output_processor = TakeFirst()
 
class OrphanSpider(CrawlSpider):
    name = "detskiedomiki"
    allowed_domains = ["www.detskiedomiki.ru"]
    start_urls = ["http://www.detskiedomiki.ru/guide/child/"]
 
    rules = (
        Rule(SgmlLinkExtractor(allow=('act=home_reg', 'act=home_zone')), follow=True),
        Rule(SgmlLinkExtractor(allow=('act=home_more')), callback='parse_item'),
    )
 
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        l = OrphanLoader(OrphanageItem(), hxs)
 
        #
        l.add_xpath('id', "//td[text()='%s']/following-sibling::td/text()" % u"Рег. номер:")
        l.add_xpath('region', "//td[text()='%s']/following-sibling::td/text()" % u"Регион:")
        l.add_xpath('district', "//td[text()='%s']/following-sibling::td/text()" % u"Район:")
        l.add_xpath('type', "//td[text()='%s']/following-sibling::td/text()" % u"Тип учреждения:")
        l.add_xpath('name', "//td[text()='%s']/following-sibling::td/strong/text()" % u"Название:")
        l.add_xpath('post', "//td[text()='%s']/following-sibling::td/text()" % u"Почтовый адрес:")
        l.add_xpath('phone', "//td[text()='%s']/following-sibling::td/text()" % u"Телефоны:")
        l.add_xpath('director', "//td[text()='%s']/following-sibling::td/text()" % u"Руководство:")
        l.add_xpath('bank', "//td[text()='%s']/following-sibling::td/text()" % u"Банковские реквизиты:")
        l.add_xpath('parent', "//td[text()='%s']/following-sibling::td/text()" % u"Вышестоящая организация:")
 
        # 
        l.add_xpath('foundation', "//td[text()='%s']/following-sibling::td/text()" % u"Дата основания:")
        l.add_xpath('activities', "//td[text()='%s']/following-sibling::td/text()" % u"Направления деятельности:")
        l.add_xpath('history', "//td[text()='%s']/following-sibling::td/text()" % u"История:")
        l.add_xpath('staff', "//td[text()='%s']/following-sibling::td/text()" % u"Персонал:")
        l.add_xpath('publications', "//td[text()='%s']/following-sibling::td/text()" % u"Публикации в СМИ:")
 
        #
        l.add_xpath('children', "//td[text()='%s']/following-sibling::td/text()" % u"Количество детей в учреждении:")
        l.add_xpath('age', "//td[text()='%s']/following-sibling::td/text()" % u"Возраст детей:")
        l.add_xpath('orphans', "//td[text()='%s']/following-sibling::td/text()" % u"Количество детей-сирот:")
        l.add_xpath('deviated', "//td[text()='%s']/following-sibling::td/text()" % u"Количество детей с отклонениями в развитии:")
        l.add_xpath('principle', "//td[text()='%s']/following-sibling::td/text()" % u"Принцип формирования группы:")
        l.add_xpath('education', "//td[text()='%s']/following-sibling::td/text()" % u"Обучение детей:")
        l.add_xpath('treatment', "//td[text()='%s']/following-sibling::td/text()" % u"Лечение детей:")
        l.add_xpath('holidays', "//td[text()='%s']/following-sibling::td/text()" % u"Летний отдых:")
        l.add_xpath('communication', "//td[text()='%s']/following-sibling::td/text()" % u"Общение детей:")
 
        #
        l.add_xpath('buildings', "//td[text()='%s']/following-sibling::td/text()" % u"Здания:")
        l.add_xpath('vehicles', "//td[text()='%s']/following-sibling::td/text()" % u"Автотранспорт:")
        l.add_xpath('farming', "//td[text()='%s']/following-sibling::td/text()" % u"Подсобное хозяйство:")
        l.add_xpath('working_cabinet', "//td[text()='%s']/following-sibling::td/text()" % u"Кабинеты труда:")
        l.add_xpath('library', "//td[text()='%s']/following-sibling::td/text()" % u"Библиотека:")
        l.add_xpath('computers', "//td[text()='%s']/following-sibling::td/text()" % u"Компьютеры:")
        l.add_xpath('toys', "//td[text()='%s']/following-sibling::td/text()" % u"Игрушки и игры")
 
        #
        l.add_xpath('patronage', "//td[text()='%s']/following-sibling::td/text()" % u"Шефство, помощь:")
        l.add_xpath('needs', "//td[text()='%s']/following-sibling::td/text()" % u"Потребности учреждения:")
        l.add_xpath('volunteers', "//td[text()='%s']/following-sibling::td/text()" % u"Привлечение добровольцев:")
 
        l.add_value('url', response.url)
 
        return l.load_item()
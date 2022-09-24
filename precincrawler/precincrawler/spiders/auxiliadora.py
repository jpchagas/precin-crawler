import scrapy


class AuxiliadoraSpider(scrapy.Spider):
    name = 'auxiliadora'
    allowed_domains = ['www.auxiliadorapredial.com.br']
    start_urls = ['http://www.auxiliadorapredial.com.br/']

      
    def parse(self, response):
        pass


'''
https://www.auxiliadorapredial.com.br/comprar/residencial/rs+porto-alegre+centro-historico?tipoImovel=apartamento
https://www.auxiliadorapredial.com.br/alugar/comercial/rs+porto-alegre+centro-historico?tipoImovel=casa
https://www.auxiliadorapredial.com.br/alto-padrao/residencial/rs+porto-alegre+petropolis
'''
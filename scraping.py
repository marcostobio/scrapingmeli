import requests
from bs4 import BeautifulSoup
from lxml import etree

def allproducto(producto):
    #creamos las listas
    lista_titulos = []
    lista_url = []
    lista_precios = []

    siguiente = 'https://listado.mercadolibre.com.ar/'+producto
    print(siguiente)

    while True:
        
        r = requests.get(siguiente)
        #hacemos el requerimiento y deberia contestar 200 en el primer ciclo mandamos solo mercadolibre
        if r.status_code == 200:
            #validamos que responda la pagina si responde hacemos el soup
            soup = BeautifulSoup(r.content,'html.parser')
            #traemos los titulos las url y los precios con sus for
            #Titulos
            titulos = soup.find_all('h2',attrs={"class":"ui-search-item__title shops__item-title"})
            titulos = [i.text for i in titulos]
            lista_titulos.extend(titulos) #agregamos a las en cada ciclo a la lista_titulos todo lo que extrajo
            #URL
            urls = soup.find_all('a',attrs={"class":"ui-search-item__group__element shops__items-group-details ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_url.extend(urls)  #agregamos a las en cada ciclo a la lista_url todo lo que extrajo
            #precios
            dom = etree.HTML(str(soup))
            precios = dom.xpath("//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='price-tag-text-sr-only']")
            precios=[i.text for i in precios]
            lista_precios.extend(precios)
            #validamos inicio y fin de las paginas
            inicio = soup.find('span',attrs={"andes-pagination__link"}).text
            inicio = int(inicio)
            fin = soup.find('li',attrs={"andes-pagination__page-count"})
            fin = int(fin.text.split(" ")[1])
        
        else:
            print("Algo detuvo el ciclo")
            break
            #si no responde. rompemos el ciclo
        
        print(inicio,fin)
        
        if inicio == fin:
            break
            #si inicio = fin /rompemos el ciclo, sino pasamos a la siguiente pagina dentro de mercadolibre
        siguiente = dom.xpath("//div[@class='ui-search-pagination shops__pagination-content']/ul/li[contains(@class,'--next')]/a")[0].get('href')
        
    return lista_titulos,lista_url,lista_precios



#siguiente funcion con limite de devolucion

def conlimite(producto,limite):
    #creamos las listas
    lista_titulos = []
    lista_url = []
    lista_precios = []

    siguiente = 'https://listado.mercadolibre.com.ar/'+producto
    print(siguiente)

    while True:
        
        r = requests.get(siguiente)
        #hacemos el requerimiento y deberia contestar 200 en el primer ciclo mandamos solo mercadolibre
        if r.status_code == 200:
            #validamos que responda la pagina si responde hacemos el soup
            soup = BeautifulSoup(r.content,'html.parser')
            #traemos los titulos las url y los precios con sus for
            #Titulos
            titulos = soup.find_all('h2',attrs={"class":"ui-search-item__title shops__item-title"})
            titulos = [i.text for i in titulos]
            lista_titulos.extend(titulos) #agregamos a las en cada ciclo a la lista_titulos todo lo que extrajo
            #URL
            urls = soup.find_all('a',attrs={"class":"ui-search-item__group__element shops__items-group-details ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_url.extend(urls)  #agregamos a las en cada ciclo a la lista_url todo lo que extrajo
            #precios
            dom = etree.HTML(str(soup))
            precios = dom.xpath("//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='price-tag-text-sr-only']")
            precios=[i.text for i in precios]
            lista_precios.extend(precios)
            #validamos inicio y fin de las paginas
            inicio = soup.find('span',attrs={"andes-pagination__link"}).text
            inicio = int(inicio)
            fin = soup.find('li',attrs={"andes-pagination__page-count"})
            fin = int(fin.text.split(" ")[1])
        
        else:
            print("Algo detuvo el ciclo")
            break
            #si no responde. rompemos el ciclo
        
        print(inicio,fin)

        if len(lista_titulos)>=int(limite): #hacemos un int por las dudas nos manden un texto
            return lista_titulos[:limite],lista_url[:limite],lista_precios[:limite]
        if inicio == fin:
            break
            #si inicio = fin /rompemos el ciclo, sino pasamos a la siguiente pagina dentro de mercadolibre
        siguiente = dom.xpath("//div[@class='ui-search-pagination shops__pagination-content']/ul/li[contains(@class,'--next')]/a")[0].get('href')
        
    return lista_titulos,lista_url,lista_precios


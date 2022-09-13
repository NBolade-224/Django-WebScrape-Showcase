from django.http import HttpResponse
from django.template import loader
from requests_html import AsyncHTMLSession
import asyncio

def home(request):
  global session
  ################################################################
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  ################################################################
  session  = AsyncHTMLSession()
  session.run(gamePS5,gameXBOX_X,gameSWITCH,gameXBOX_S,
              AmazonPS5,AmazonXBOX_X,AmazonSWITCH,AmazonXBOX_S,
              argosPS5,argosXBOX_X,argosSWITCH,argosXBOX_S)
  ################################################################
  template = loader.get_template('main.html')
  context = {'gamePS5Price':gamePS5Price,'gameXBOX_XPrice':gameXBOX_XPrice,'gameSWITCHPrice':gameSWITCHPrice,'gameXBOX_SPrice':gameXBOX_SPrice,
            'AmazonPS5Price':AmazonPS5Price,'AmazonXBOX_XPrice':AmazonXBOX_XPrice,'AmazonSWITCHPrice':AmazonSWITCHPrice,'AmazonXBOX_SPrice':AmazonXBOX_SPrice,
            'argosPS5Price':argosPS5Price,'argosXBOX_XPrice':argosXBOX_XPrice,'argosSWITCHPrice':argosSWITCHPrice,'argosXBOX_SPrice':argosXBOX_SPrice,}
  return HttpResponse(template.render(context,request))


async def gamePS5():
  global gamePS5Price
  urls1 = "https://www.game.co.uk/en/playstation/consoles/?cm_sp=Nav-_-PlayStation-_-Consoles-_-Heading"
  page = await session.get(urls1)
  products = page.html.find('.mintPrice[data-sku="798801"] .value')
  for x in products:
    gamePS5Price = x.text
  await session.close()
  return gamePS5Price
async def gameXBOX_X():
  global gameXBOX_XPrice
  urls1 = "https://www.game.co.uk/en/xbox/consoles/xbox-series-x/?cm_sp=Nav-_-Xbox-_-Consoles-_-XSXConsoles"
  page = await session.get(urls1)
  products = page.html.find('.mintPrice[data-sku="800821"] .value')
  for x in products:
    gameXBOX_XPrice = x.text
  await session.close()
  return gameXBOX_XPrice
async def gameSWITCH():
  global gameSWITCHPrice
  urls1 = "https://www.game.co.uk/en/nintendo/consoles/?contentOnly=&inStockOnly=true&listerOnly=true&pageSize=72&sortBy=PRICE_DESC&pageNumber=1"
  page = await session.get(urls1)
  products = page.html.find('.mintPrice[data-sku="807837"] .value')
  for x in products:
    gameSWITCHPrice = x.text
  await session.close()
  return gameSWITCHPrice
async def gameXBOX_S():
  global gameXBOX_SPrice
  urls1 = "https://www.game.co.uk/en/xbox/consoles/xbox-series-s/?cm_sp=Nav-_-Xbox-_-Consoles-_-XSXConsoles"
  page = await session.get(urls1)
  products = page.html.find('.mintPrice[data-sku="800825"] .value')
  for x in products:
    gameXBOX_SPrice = x.text
  await session.close()
  return gameXBOX_SPrice

async def AmazonPS5():
  global AmazonPS5Price
  urls1 = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/"
  page = await session.get(urls1)
  #page.html.arender()
  products = page.html.find('#corePrice_feature_div .a-offscreen')
  for x in products:
    AmazonPS5Price = x.text
  await session.close()
  return AmazonPS5Price
async def AmazonXBOX_X():
  global AmazonXBOX_XPrice
  urls1 = "https://www.amazon.co.uk/Xbox-RRT-00007-Series-X/dp/B08H93GKNJ/"
  page = await session.get(urls1)
  products = page.html.find('#corePrice_feature_div .a-offscreen')
  for x in products:
    AmazonXBOX_XPrice = x.text
  await session.close()
  return AmazonXBOX_XPrice
async def AmazonSWITCH():
  global AmazonSWITCHPrice
  urls1 = "https://www.amazon.co.uk/Nintendo-Switch-OLED-Model-White/dp/B098TVDYZ3/"
  page = await session.get(urls1)
  products = page.html.find('#corePrice_feature_div .a-offscreen')
  for x in products:
    AmazonSWITCHPrice = x.text
  await session.close()
  return AmazonSWITCHPrice
async def AmazonXBOX_S():
  global AmazonXBOX_SPrice
  urls1 = "https://www.amazon.co.uk/Xbox-RRS-00007-Series-S/dp/B08GD9MNZB/"
  page = await session.get(urls1)
  products = page.html.find('#corePrice_feature_div .a-offscreen')
  for x in products:
    AmazonXBOX_SPrice = x.text
  await session.close()
  return AmazonXBOX_SPrice

async def argosPS5():
  global argosPS5Price
  urls1 = "https://www.argos.co.uk/product/8349000?/"
  page = await session.get(urls1)
  products = page.html.find('[itemprop="priceCurrency"] + h2')
  for x in products:
    argosPS5Price = x.text
  await session.close()
  return argosPS5Price
async def argosXBOX_X():
  global argosXBOX_XPrice
  urls1 = "https://www.argos.co.uk/product/8448262?/"
  page = await session.get(urls1)
  products = page.html.find('[itemprop="priceCurrency"] + h2')
  for x in products:
    argosXBOX_XPrice = x.text
  await session.close()
  return argosXBOX_XPrice
async def argosSWITCH():
  global argosSWITCHPrice
  urls1 = "https://www.argos.co.uk/product/9482210?/"
  page = await session.get(urls1)
  products = page.html.find('[itemprop="priceCurrency"] + h2')
  for x in products:
    argosSWITCHPrice = x.text
  await session.close()
  return argosSWITCHPrice
async def argosXBOX_S():
  global argosXBOX_SPrice
  urls1 = "https://www.argos.co.uk/product/8448248?/"
  page = await session.get(urls1)
  products = page.html.find('[itemprop="priceCurrency"] + h2')
  for x in products:
    argosXBOX_SPrice = x.text
  await session.close()
  return argosXBOX_SPrice



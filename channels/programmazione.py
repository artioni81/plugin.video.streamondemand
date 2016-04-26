# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canale Video Corsi Programmazione
# Creato dall'utente costaplus
# http://www.mimediacenter.info/foro/viewforum.php?f=36.
#------------------------------------------------------------
import re
import urlparse

from core import config
from core import logger
from core import scrapertools
from core.item import Item

__channel__ = "programmazione"
__category__ = "D"
__type__ = "generic"
__title__ = "programmazione(IT)"
__language__ = "IT"

 
DEBUG = config.get_setting("debug")

site = "https://www.youtube.com/"

def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.programmazione mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Html 5[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL7A4A3449C649048F", thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/220px-HTML5_logo_and_wordmark.svg.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Css[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PLD74C5E763D39793D", thumbnail="http://www.hub4tech.com/sites/default/files/InterviewQA/CSS3.png?1444984729"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Javascript[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL1A447BA7F7F9EB9E", thumbnail="https://www.freeenergymedia.com/wp-content/uploads/2015/03/20120709-164039-Javascript.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso PHP[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJc664i2Cv0X0ibM9b1YqRyd", thumbnail="https://media.phpnuke.org/000/984/101/bd2_6f5_636_330-1-original.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso PHP Mysql[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL101314D973955661", thumbnail="https://media.phpnuke.org/000/984/101/bd2_6f5_636_330-1-original.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Jquery[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PLC959BB22285B353F", thumbnail="http://4.bp.blogspot.com/-78DiBtASpKM/UezbYVxfOGI/AAAAAAAAAQE/iscqFa93-9w/s320/jquery_logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java da Zero[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJe2dpE7di4aPJwrQuRD6IDD", thumbnail="http://resources.workable.com/wp-content/uploads/2013/04/java.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java 2 OOP[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJee1dk24wX-68yHTnMfzdX5", thumbnail="http://resources.workable.com/wp-content/uploads/2013/04/java.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java Interfaccia Grafica[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJfRML8EDs7v9nwjdOt6dvaf", thumbnail="http://resources.workable.com/wp-content/uploads/2013/04/java.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java Android[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJeqmBWbE1Rbac2QWHoPCjR2", thumbnail="http://www.nexus-lab.com/wp-content/uploads/2015/12/Android-java.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Progettazione DB[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJcJPSV4sOfhLtPbtQ-yycFH", thumbnail="http://glue-talk.com/wp-content/uploads/2011/05/progettazione_db.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso SQL[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PLE555DB6188C967AC", thumbnail="http://codeblog.altervista.org/wp-content/uploads/2015/12/Introduction-to-SQL.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Python[/COLOR]", action="peliculas", url="https://www.youtube.com/playlist?list=PLC64779F4E2E7EB10", thumbnail="http://www.bebetterdeveloper.com/img/post_img/python-logo.png"))
   
    return itemlist
   
def peliculas(item):
   logger.info("streamondemand.programmazione peliculas")
   itemlist = []

    # Descarga la pagina
   data = scrapertools.cache_page(item.url)
        
   # Extrae las entradas (carpetas)
   patron  = '<a class="pl-video-title-link.*?href="(.*?)"[^>]+>(.*?)</a>'
   matches = re.compile(patron,re.DOTALL).findall(data)
   scrapertools.printMatches(matches)
   
   for scrapedurl,scrapedtitle in matches:
       scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
       itemlist.append( Item(channel=__channel__, action="findvideos", fulltitle=scrapedtitle, show=scrapedtitle, title=scrapedtitle, url=site+scrapedurl , thumbnail="", plot="" , folder=True) )
   
   return itemlist
   
   
def HomePage(item):
    import xbmc
    xbmc.executebuiltin("ReplaceWindow(10024,plugin://plugin.video.streamondemand)")

import httpx

with open("proxy.txt", 'w') as file:
    print("Proxies Scraper")
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous").text)
    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt").text)
    file.write(httpx.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5").text)
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5").text)
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true").text)
    file.write(httpx.get("https://www.proxyscan.io/download?type=http").text)
    file.write(httpx.get("https://www.proxyscan.io/download?type=https").text)
    file.write(httpx.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt").text)
    file.write(httpx.get("https://proxyspace.pro/http.txt").text)
    file.write(httpx.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http").text)
    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=http").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text)
    file.write(httpx.get("http://worm.rip/socks4.txt").text)
    file.write(httpx.get("http://worm.rip/socks5.txt").text)
    file.write(httpx.get("http://worm.rip/http.txt").text)
    file.write(httpx.get("https://sheesh.rip/all.txt").text)
    file.write(httpx.get("http://alexa.lr2b.com/proxylist.txt").text)
    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=socks4").text)
    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=socks5").text)    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=http").text)
    file.write(httpx.get("https://api.openproxylist.xyz/http.txt").text)
    file.write(httpx.get("https://api.openproxylist.xyz/socks4.txt").text)
    file.write(httpx.get("https://api.openproxylist.xyz/socks5.txt").text)
    file.write(httpx.get("http://rootjazz.com/proxies/proxies.txt").text)
    file.write(httpx.get("https://multiproxy.org/txt_all/proxy.txt").text)
    file.write(httpx.get("https://proxy-spider.com/api/proxies.example.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/RX4096/proxy-list/main/archive/all.txt").text)    file.write(httpx.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/mallisc5/master/proxy-list-raw.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt")").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http").text)
    file.write(httpx.get("    file.write(httpx.get("https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/casals-ar/proxy-list/main/https").text)
    file.write(httpx.get("https://raw.githubusercontent.com/casals-ar/proxy-list/main/http").text)
    file.write(httpx.get("https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt").text)
    file.write(httpx.get("http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html").text)
    file.write(httpx.get("http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html").text)
    file.write(httpx.get("http://www.cybersyndrome.net/pla5.html").text)
    file.write(httpx.get("http://vipprox.blogspot.com/2013_06_01_archive.html").text)
    file.write(httpx.get("http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html").text)
    file.write(httpx.get("http://vipprox.blogspot.com/p/blog-page_7.html").text)
    file.write(httpx.get("http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html").text)
    file.write(httpx.get("http://vipprox.blogspot.com/2013_02_01_archive.html").text)
    file.write(httpx.get("http://alexa.lr2b.com/proxylist.txt").text)
    file.write(httpx.get("http://vipprox.blogspot.com/2013_03_01_archive.html").text)
    file.write(httpx.get("http://browse.feedreader.com/c/Proxy_Server_List-1/449196260").text)
    file.write(httpx.get("http://browse.feedreader.com/c/Proxy_Server_List-1/449196258").text)
    file.write(httpx.get("http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html#comment-form").text)
    file.write(httpx.get("http://browse.feedreader.com/c/Proxy_Server_List-1/449196251").text)
    file.write(httpx.get("http://free-ssh.blogspot.com/feeds/posts/default").text)
    file.write(httpx.get("http://browse.feedreader.com/c/Proxy_Server_List-1/449196259").text)
    file.write(httpx.get("http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html").text)
    file.write(httpx.get("http://proxyfirenet.blogspot.com/").text)
    file.write(httpx.get("https://www.javatpoint.com/proxy-server-list").text)
    file.write(httpx.get("https://openproxy.space/list/http").text)
    file.write(httpx.get("http://proxydb.net/").text)
    file.write(httpx.get("http://olaf4snow.com/public/proxy.txt
    file.write(httpx.get("http://westdollar.narod.ru/proxy.htm").text)
    file.write(httpx.get("https://openproxy.space/list/socks4").text)
    file.write(httpx.get("https://openproxy.space/list/socks5").text)
    file.write(httpx.get("http://tomoney.narod.ru/help/proxi.htm").text)
    file.write(httpx.get("http://sergei-m.narod.ru/proxy.htm").text)
    file.write(httpx.get("http://rammstein.narod.ru/proxy.html").text)
    file.write(httpx.get("http://greenrain.bos.ru/R_Stuff/Proxy.htm").text)
    file.write(httpx.get("http://inav.chat.ru/ftp/proxy.txt").text)
    file.write(httpx.get("http://johnstudio0.tripod.com/index1.htm").text)
    file.write(httpx.get("http://atomintersoft.com/transparent_proxy_list").text)
    file.write(httpx.get("http://atomintersoft.com/anonymous_proxy_list").text)
    file.write(httpx.get("http://atomintersoft.com/high_anonymity_elite_proxy_list").text)
    file.write(httpx.get("http://atomintersoft.com/products/alive-proxy/proxy-list/3128").text)
    file.write(httpx.get("http://atomintersoft.com/products/alive-proxy/proxy-list/com").text)
    file.write(httpx.get("http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/").text)
    file.write(httpx.get("http://atomintersoft.com/products/alive-proxy/socks5-list").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_domain_com").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_domain_edu").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_domain_net").text)
    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_domain_org").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_port_3128").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_port_80").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_port_8000").text)
    file.write(httpx.get("http://atomintersoft.com/proxy_list_port_81").text)
    file.write(httpx.get("http://hack-hack.chat.ru/proxy/allproxy.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt").text)
    file.write(httpx.get("http://hack-hack.chat.ru/proxy/anon.txt").text)
    file.write(httpx.get("http://hack-hack.chat.ru/proxy/p1.txt").text)
    file.write(httpx.get("http://hack-hack.chat.ru/proxy/p2.txt").text)
    file.write(httpx.get("http://hack-hack.chat.ru/proxy/p3.txt").text)
    file.write(httpx.get("http://hack-hack.chat.ru/proxy/p4.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt").text)
    file.write(httpx.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text)
    file.write(httpx.get("https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all").text)
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text)
    print("Done")
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

while True:
    coursenum = input('input course number please.\n')

    req = Request('https://pocu-ko.teachable.com/p/' + coursenum, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()

    # with urlopen('https://pocu-ko.teachable.com/p/comp2200') as response:
    soup = BeautifulSoup(response, 'html.parser')

    totalhr = 0
    totalmin = 0
    totalsec = 0

    for anchor in soup.select('span.block__curriculum__section__list__item__lecture-duration'):
        # print(anchor.get('href', '/'))
        # print(anchor.get_text())
        a = anchor.get_text().split(':')
        totalmin += int(a[0][1:])
        totalsec += int(a[1][:-1])

    totalmin = totalmin + totalsec // 60
    totalsec = totalsec - (totalsec // 60 * 60)

    totalhr = totalhr + totalmin // 60
    totalmin = totalmin - (totalmin // 60 * 60)

    if totalmin < 10:
        totalmin = '0' + str(totalmin)
    else:
        totalmin = str(totalmin)

    if totalsec < 10:
        totalsec = '0' + str(totalsec)
    else:
        totalsec = str(totalsec)

    print("Total Time:", str(totalhr) + ':' + totalmin + ':' + totalsec)

    # comp2200: 37:51:20
    # comp2500: 28:37:05
    # comp3200: 25:29:14

    # print('totalhr:', totalhr)
    # print('totalmin:', totalmin)
    # print('totalsec:', totalsec)



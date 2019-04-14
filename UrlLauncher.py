import webbrowser, sys, random, time
from datetime import datetime

def GetUrlsFromFile(finmename):
    urls = []
    try:
        with open(finmename, 'r') as fileReader:
            line = fileReader.readline()
            while(line):
                urls.append(line)
                line = fileReader.readline()

    except Exception as e:
        print(str(e))
        return []

    else:
        return urls

def SelectRandomUrl(urls):

    randomNumber = random.randrange(0, len(urls), 1)
    url = urls[randomNumber]

    return url

def WaitForTimer(launchTime):

    currentTime = datetime.now().strftime('%H:%M')
    while(launchTime not in currentTime):
        time.sleep(1)
        currentTime = datetime.now().strftime('%H:%M')

def LaunchUrl(url):
    print(f'Launching URL {url}')
    webbrowser.open_new_tab(url)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('Required arguments not passed')
        print('Argument 1 : URL file')
        print('Argument 2 : Time in HH:MM format')
        exit()

    urlFile = sys.argv[1]
    urls = GetUrlsFromFile(urlFile)

    if not len(urls) > 0:
        print('No URL found')
        exit()

    url = SelectRandomUrl(urls)

    launchTime = sys.argv[2]
    WaitForTimer(launchTime)

    LaunchUrl(url)

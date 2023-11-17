url = 'https://exampleURL1.com/r626c36'

def url_checker(url):
    protocol = url.split(':')[0]
    store_id = url.split('/')[-1]
    if (protocol != 'https') and (len(store_id) != 7):
        print(f"{protocol} is an invalid protocol.")
        print(f"{store_id} is an invalid store ID.")
    else:
        if protocol != 'https':
            print(f"{protocol} is an invalid protocol")
        elif len(store_id) != 7:
            print(f"{store_id} is an invalid store ID")
        else:
            print(f"Store ID: {store_id}")
            
            
url_checker('http://exampleURL1.com/r626c3')    # 'http: is an invalid protocol.'
                                                # 'r626c3 is an invalid store ID.'

url_checker('ftps://exampleURL1.com/r626c36')   # 'ftps: is an invalid protocol.

url_checker('https://exampleURL1.com/r626c3')   # 'r626c3 is an invalid store ID.'

url_checker('https://exampleURL1.com/r626c36')  # 'r626c36'

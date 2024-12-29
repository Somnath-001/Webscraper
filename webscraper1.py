import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.meesho.com/search?q=jacket&searchType=POPULAR_SEARCHES&searchIdentifier=text_search"
    #Sends a GET request to the specified url

    amazon_response = requests.get(url)

    print(amazon_response.status_code)

    soup = BeautifulSoup(amazon_response.content,'html.parser')
    print(soup.prettify()[:100])

    potential_agent_links=soup.find_all('a',href=True)

    print(f"Found{len(potential_agent_links)}potential links")

    description=soup.find(class_="DesktopHeader__HeaderStyled-sc-r0p6o1-1 crXaie").text.strip() if soup.find('p') else "No description available"
    
    apt_list = soup.find_all('a', class_="NewProductCardstyled__ProductImage-sc-6y2tys-19 czNIkn")
    for apt in apt_list:
        url = apt.get("href")
        url = "https://www.meesho.com/" + url
        print(url)
    
    keywords = [
        "Coats and Jackets",
        "Trendy mordern men jacket"
    ]

    found_keywords = [keyword for keyword in keywords if keyword.lower() in description.lower()]

    return {
         'url' : url,
         'found_key' : found_keywords,
         'description' : description
    }
 
    
if __name__ == "__main__":
    results = main()
    print(type(results))
    print(results)


    result = []
    for i, result in enumerate(results):
        print(results['url'])
        print(results['found_key'])
        print(results['description'])
        
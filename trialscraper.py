import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.meesho.com/search?q=jacket&searchType=POPULAR_SEARCHES&searchIdentifier=text_search"
    #Sends a GET request to the specified url

    amazon_response = requests.get(url)

    print(amazon_response.status_code)

    soup = BeautifulSoup(amazon_response.content,'html.parser')
    print(soup.prettify()[:100])

    potential_agent_links=soup.find_all('t',href=True)

    print(f"Found{len(potential_agent_links)}potential links")

    description=soup.find('p').text.strip() if soup.find('p') else "No description available"
    
    
    keywords = [
        "nvidia",
        "wahl",
        "nivia"
    ]

    found_keywords = [keyword for keyword in keywords if keyword.lower() in description.lower()]

    return {
         'ur' : url,
         'fk' : found_keywords,
         'd' : description
    }

    
    
if __name__ == "__main__":
    results = main()
    print(type(results))
    print(results)

    # results = {}
    for i, (key,value) in enumerate(results.items()):
        print(f"{key,value}")
      

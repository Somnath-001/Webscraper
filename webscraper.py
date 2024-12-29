import requests
from bs4 import BeautifulSoup

#DEFINE A main() FUNCTION
def main():

    #ASSIGN LINK OF A WEBSITE TO A VARIABLE
    url = "https://www.flipkart.com/beds/pr?sid=wwe,7p7&otracker=nmenu_sub_Home%20%26%20Furniture_0_Beds"

    #CHECK IF THE URL GETS POSITIVE RESPONSE
    response = requests.get(url)

    #PRINT THE RESPONSE
    print(response)

    # THIS LINE CONVERTS THE RAW HTML RESPONSE INTO STRUCTURED DATA
    soup = BeautifulSoup(response.text,'html.parser')
    
    #CREATE A LIST CONTAINING ALL ESSENTIAL <DIV>'s
    bed_list = soup.find_all('div', class_="_75nlfW")

    #CREATE A FOR LOOP
    for bed in bed_list:

        #GET LINKS OF THE BED
        url1 = bed.find('a').get('href')

        #CONCATENATES LINK AND CREATES DIRECT LINK TO PARTICULAR BED
        url2 = "https://www.flipkart.com/" + url1

        #GETS THE NAME OF THE BED
        name = bed.find('a', class_="wjcEIp").text

        print(f"Item: {name}")

        #GETS THE PRICE OF THE BED
        price = bed.find('div', class_="Nx9bqj").text

        print(f"Price: {price}")

        print(f"Link: {url2}")

        print('\n')

#CHECKS IF THE SCRIPT IS RUN DIRECTLY AND NOT IMPORTED
if __name__ == '__main__':
    #CALLS THE main() FUNCTION
    main()
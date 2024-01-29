from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler): 
    
    def do_GET(self):
        string = self.path
        url_components = parse.urlsplit(string)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        message = "Please provide a country or capital name"
        
        if "country" in dic:
            capitals = self.get_information(f"https://restcountries.com/v3.1/name/{dic['country']}", "capital")
            
            if capitals:
                message = f"The capital of {dic['country'].title()} is {', '.join(capitals)}."
            else:
                message = f"Unable to find the capital of {dic['country'].title()}."

        elif "capital" in dic:
            countries = self.get_information(f"https://restcountries.com/v3.1/capital/{dic['capital']}", "country")
            
            if countries:
                message = f"{dic['capital'].title()} is the capital of {', '.join(countries)}."
            else:
                message = f"Unable to find a country with the capital {dic['capital'].title()}."
                
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return
        
    def get_information(self, url, type):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if type == "capital":
                return str([country_data["capital"][0] for country_data in data])
            elif type == "country":
                return str([country_data["name"]["common"] for country_data in data])

        except requests.exceptions.HTTPError as err:
            return f"HTTP Error: {err}"
        except requests.exceptions.RequestException as err:
            return f"Request Exception: {err}"
        except KeyError:
            return "Error in parsing data"
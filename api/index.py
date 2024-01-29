from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler): 
    
    def do_GET(self):
        string = self.path
        url_components = parse.urlsplit(string)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        if "country" in dic:
            url = f"https://restcountries.com/v3.1/name/{dic['country']}"
            
            try:
                country_req = requests.get(url)
                country_req.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
                data = country_req.json()
                capitals = [country_data["capital"][0] for country_data in data]
                message = str(capitals)
            
            except requests.exceptions.HTTPError as err:
                message = f"HTTP Error: {err}"
            except requests.exceptions.RequestException as err:
                message = f"Request Exception: {err}"
            except KeyError:
                message = "Error in parsing country data"
        
        if "capital" in dic:
            url = f"https://restcountries.com/v3.1/capital/{dic['capital']}"
            
            try:
                capital_req = requests.get(url)
                capital_req.raise_for_status()
                data = capital_req.json()
                countries = [capital_data["name"][0] for capital_data in data]
                message = str(countries)
                
            except requests.exceptions.HTTPError as err:
                message = f"HTTP Error: {err}"
            except requests.exceptions.RequestException as err:
                message = f"Request Exception: {err}"
            except KeyError:
                message = "Error in parsing country data"
            
        else:
            message = "Please provide a country or capital name"
            
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode('utf-8'))
        return
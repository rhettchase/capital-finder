from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler): # subclass of BaseHTTPRequestHandler
    # WRRC
    def do_GET(self):
        string = self.path
        url_components = parse.urlsplit(string)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            country_req = requests.get(url + dic["country"])
            data = country_req.json()
            countries = []
            for country_data in data:
                country_capital = country_data["name"][0]["capital"][0]
                countries.append(country_capital)
            message = str(countries)
            
        else:
            message = "Please provide a country name"
            
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode('utf-8'))
        return
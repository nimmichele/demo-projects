import http.client
import mimetypes
import json
import sys

def main(args):

  query = args.get("query")
  conn = http.client.HTTPSConnection("api.twitter.com")

  payload = ''
  headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'Cookie': 'personalization_id="v1_PyXEHdYP45nnysyqaZnywA=="; guest_id=v1%3A158876007431774006'
  }
  conn.request("GET", "/labs/1/tweets/search?max_results=20&=query=" + query, payload, headers)
  
  res = conn.getresponse()
  data = res.read()
  data = data.decode("utf-8")
  print(data)
  return {"main": data}

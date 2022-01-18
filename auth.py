import http.client

access_token = 'OwNpo00TnGOaT4VceqO4DRHynPGnXypQWLbSjtwI8E8aC.99qUzcjMumiO\
TiZUYCWIms8msjfJVvN5uNcfAzLlxkAe25emA4GUcWROXgCqJf8o1VNEm6hxkX3hJ260qR'
conn = http.client.HTTPSConnection("api.surveymonkey.com")
headers = {
            'Accept': "application/json",
            'Authorization': "Bearer %s" % access_token
          }
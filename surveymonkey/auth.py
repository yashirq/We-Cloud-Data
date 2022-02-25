import http.client
import psycopg2

# Survey Monkey
access_token = ''
sm_conn = http.client.HTTPSConnection('api.surveymonkey.com')
headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer %s' % access_token
          }

# AWS S3
aws_access_key_id = ''
aws_secret_access_key = ''

#Postgres SQL
psql_conn = psycopg2.connect(
   database='postgres', user='', password='', 
    host=''
)
psql_conn.autocommit = True
cursor = psql_conn.cursor()
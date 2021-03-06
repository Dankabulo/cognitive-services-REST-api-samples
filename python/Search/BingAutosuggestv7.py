#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Add your Bing Autosuggest subscription key to your environment variables.
subscriptionKey = os.environ['BING_AUTOSUGGEST_SUBSCRIPTION_KEY']

# Add your Bing Autosuggest endpoint to your environment variables.
host = os.environ['BING_AUTOSUGGEST_ENDPOINT']
path = '/bing/v7.0/Suggestions'

mkt = 'en-US'
query = 'sail'

params = '?mkt=' + mkt + '&q=' + query

def get_suggestions ():
    "Gets Autosuggest results for a query and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    conn.request ("GET", path + params, None, headers)
    response = conn.getresponse ()
    return response.read ()

result = get_suggestions ()
print (json.dumps(json.loads(result), indent=4))

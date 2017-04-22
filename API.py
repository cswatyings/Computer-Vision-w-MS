import pandas as pd
from pandas import DataFrame, Series
import httplib, urllib, base64
import sys
import os
import csv, json
import multiprocessing
import time
import numpy as np


##Initiative Setting##
#dff = DataFrame(columns = ['T1','T2','T3'])
output = open('~/project_out_.csv','w')

params = urllib.urlencode({
    # Notes 1/3 for user: Specify your API subscription key
    #'subscription-key': 'API_KEY',
    # Notes 2/3 for user: Specify values for optional parameters or leave as 'All'
    #'visualFeatures': 'Categories',
    'visualFeatures': str('categories') + ',' + str('tags') + ',' + str('faces') + ',' + str('color')
})


try:

    headers = {
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'API-KEY'
    }
    #Initializing body variable
    body = "" 
    # Replace directory value with your own and make sure you add '/' at the end
    directory = '~/Desktop/samples/'
    
    for subdir, dirs, files in os.walk(directory):
        ###Taking out File Names###
        for file in files:
            filename = file
            name = str(filename.split('.jpg')[0])
            #print("file is", filename)
            fullpath = directory+filename
            #print("full path is", fullpath)
            #Don't need the following
            #file_ext=os.path.basename(fullpath)
            file_woext=os.path.splitext(os.path.basename(fullpath))[0]
            file_out=file_woext+'.json'
            f = open(fullpath, "rb")
            body = f.read()
            f.close()
            
            ###Connect to the API###
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()
            print ' '
            print filename
            print ' '
            print ' '
            print data
            print ' '
            print ' '
            print '-----------------------------------------------------------'
            print ' '
            j_data = json.loads(data)
            print j_data
            ###### Saving the results as json files#####
            with open('~/JSON/'+ str(name)+'.json', 'w') as f:
                json.dump(data, f)
            #dfff = DataFrame(everything['tags'])
            
            try:
                ###get everything except tags
                try:
                    c = len(j_data['categories'])
                    output.write(str(c)+',')
                except:
                    output.write(str(np.nan)+',')
                t = len(j_data['tags'])
                f = len(j_data['faces'])
                output.write(str(name)+',')
                try:
                    obj = j_data['categories'][0]['name']
                    output.write(obj+',')
                except:
                    output.write(str(np.nan)+',')
                    
                fc = j_data['color']['dominantColorForeground']
                bc = j_data['color']['dominantColorBackground']
                gender = j_data['faces'][0]['gender']
                age = j_data['faces'][0]['age']
                print t
                print f
                output.write(str(t)+','+str(f)+','+str(1)+','+str(age)+','+gender+','+fc+','+bc+',')
                
                ###Get Tags###
                try:
                    print filename
                    print name
                    for m in range(3):
                        print str(m+1)
                        result = str(j_data['tags'][m]['name'])
                        print result
                        output.write(result+',')
                except:
                    output.write(str(np.nan)+',')
                output.write('\n')    
                print ''
                #print 'Waiting 3 seconds to avoid exceeding API rate limit...'
                #time.sleep(3)
            except KeyError as e:
                print e

            except IndexError as e:
                print ''
                print 'ERROR: Could not recognize face for ' + str(filename)
                print ''
                #pic_err.append(name)
                #print 'Waiting 3 seconds to avoid exceeding API rate limit...'
                #time.sleep(3)
                #output.write(str(name)+',')
                output.write(str(t)+','+str(f)+','+str(0)+','+str(np.nan)+','+str(np.nan)+','+fc+','+bc+',')
                try:
                    print filename
                    print name
                    for m in range(3):
                        print str(m+1)
                        result = str(j_data['tags'][m]['name'])
                        print result
                        output.write(result+',')
                except:
                    output.write(str(np.nan)+',')
                output.write('\n')
                #print ''
                #print 'Waiting 3 seconds to avoid exceeding API rate limit...'
                #time.sleep(3)
            #print int(data['faces']['age'])
            conn.close()
except Exception as e:
    print(e)
output.close()

#with open('JSONData.json', 'w') as f:
#     json.dump(jsonData, f)

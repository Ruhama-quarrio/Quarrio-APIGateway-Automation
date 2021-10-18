import configparser
config = configparser.ConfigParser()


config['DEFAULT'] = { 
        'LoginURL': 'https://auth.qca-dev.com/api/api/1.0/login/',
        'baseURL' : 'https://auth.qca-dev.com/',
        'email': 'user@quarrio.com',
        'bcc': 'user@quarrio.com',
        'cc': 'user@quarrio.com',
        'theme': 'light'
     }

config['dal'] = { 
        'url': 'api/1.0/dal/?',
        'q': 'list of opps',
        'id' : '398'
     }

config['parser'] = { 
        'url': 'api/1.0/parser/?',
        'q': 'list of opps',
        'id' : '398'
     }

config['getConversation'] = { 
        'url': 'api/1.0/qca/conversation/?',
        'userid': '398',
        'limit' : '3'
     }
config['postConversation'] = { 
        'url': 'api/1.0/qca/conversation/',
        'question': 'list of opps',
        'userId': '398',
        'dateTime': '2020-03-18 05:12:30',
        'lang' : 'english'
     }

config['getDatasource'] = { 
        'url': 'api/1.0/qca/datasource/',
     }

config['postDatasource'] = { 
        'url': 'api/1.0/qca/datasource/',
         'userId': '282',
  'dbId': 'string',
  'istokenExpired' : "true",
  'salesforceEmail': 'user0980@quarrio.com',
  'salesforceSyncInterval': '0',
  'sfOrgId': 'string',
  'synchronizationStageId': '0',
  'userRole': 'string'
     }

config['putDatasource'] = { 
        'url': 'api/1.0/qca/datasource/',
         'userId': '398',
  'dbId': 'string',
  'istokenExpired' : "true",
  'salesforceEmail': 'ruhama123@quarrio.com',
  'salesforceSyncInterval': '0',
  'sfOrgId': 'string',
  'synchronizationStageId': '0',
  'userRole': 'string'
     }

config['deleteDatasource'] = { 
        'url': 'api/1.0/qca/datasource/?',
        'userId': '282'
     }

config['postfeedback'] = { 
        'url': 'api/1.0/qca/feedback/',
         'cc': 'user@quarrio.com',
  'email': 'user@quarrio.com',
  'userEmail': 'user@quarrio.com',
  'message': 'string',
  'name': 'string',
  'questionLabel': 'list of accounts',
  'subject': 'string'
     }

config['getAllUsers'] = { 
        'url': 'api/1.0/qca/get-all-users/'
     }

config['getUserOrg'] = { 
        'url': 'api/1.0/qca/get-user-org/?',
        'orgId': '45'
     }

config['getUserByType'] = { 
        'url': 'api/1.0/qca/get-users-by-type/?',
        'typeId': '2'
     }

config['getOrganization'] = { 
        'url': 'api/1.0/qca/organization/'
     }

config['postOrganization'] = { 
        'url': 'api/1.0/qca/organization/',
        'id': '473',
        'name': 'ruhama'
     }
config['putOrganization'] = { 
        'url': 'api/1.0/qca/organization/',
        'id': '470',
        'name': 'ruhama'
     }

config['deleteOrganization'] = { 
        'url': 'api/1.0/qca/organization/?',
        'id': '423',
        'name': 'Data Inc'
     }

config['getquestionFavourite'] = { 
        'url': 'api/1.0/qca/questions/favorite/?',
        'userId': '398',
        'limit': '5'
     }

config['postquestionFavourite'] = { 
        'url': 'api/1.0/qca/questions/favorite/',
        'userId': '398',
        'questionId': '919'
     }

config['postquestionUnFavourite'] = { 
        'url': 'api/1.0/qca/questions/unfavorite/',
        'questionId': '919',
        'userId': '398'
     }
config['getquestionPin'] = { 
        'url': 'api/1.0/qca/questions/pin/?',
        'userId': '398',
        'limit': '5'
     }

config['postquestionPin'] = { 
        'url': 'api/1.0/qca/questions/pin/',
        'userId': '398',
        'questionId': '919'
     }

config['postquestionUnpin'] = { 
        'url': 'api/1.0/qca/questions/unpin/',
        'userId': '398',
        'questionId': '919'
     }

config['resetPassword'] = { 
        'url': 'api/1.0/qca/reset-user-pwd/',
         'confirmPassword': 'test@098',
	'currentPassword' : 'Test@098',
	'password': 'test@098'

     }
config['postSendEmail'] = { 
        'url': 'api/1.0/qca/send-email/',
        'message': 'list of opps/opportunities',
        'subject': 'PostSendEmail'

     }

config['getSettings'] = { 
        'url': 'api/1.0/qca/setting/?',
        'userId': '398',
        'limit': '5'
     }

config['postSettings'] = { 
        'url': 'api/1.0/qca/setting/',
         'dataLimit': '2',
             'userId': '398',
             'language': 'english',
             'scheduleTime': '01:01:11',
             'scheduleTypeId': '1'
             
     }

config['userOrgType'] = { 
        'url': 'api/1.0/qca/user-org-type/?',
        'token': 'ea42458a-7728-4adc-b831-f4f3e8ac22a9'
     }

config['userSearch'] = { 
        'url': 'api/1.0/qca/user-search/?',
        'userId': '398'
     }
config['userType'] = { 
        'url': 'api/1.0/qca/user-type/?',
        'typeId': '3'
     }
config['userverifyToken'] = { 
        'url': 'api/1.0/qca/user-verify-token/?',
        'token': 'ea42458a-7728-4adc-b831-f4f3e8ac22a9'
     }

config['getQcaUser'] = { 
        'url': 'api/1.0/qca/user/?',
        'userId': '398'
     }

config['putQcaUser'] = { 
        'url': 'api/1.0/qca/user/',
        'userId': '398',
        'username': 'ruhama',
        'email': 'user@quarrio.com',
        'firstName': 'ruhama',
        'lastName': 'sardar',
        'phone': '0330747241761'   
     }

config['postUpdateSalesforceEmail'] = { 
        'url': 'api/1.0/qca/user/update-salesforce-email/',
        'userId': '398',
        'salesforceEmail': 'ruhama1.sardar@quarrio.com'
          
     }

config['getSalesforceUserDetails'] = { 
        'url': 'api/1.0/salesforce/get-user-details/?',
        'id': '398'         
     }

config['getSalesforcrceDisconnect'] = { 
        'url': 'api/1.0/salesforce/salesforce-disconnect/?',
        'operation_type':'allsubuser',
        'admin_id':'476'       
     }

config['postSalesforcrcelogin'] = { 
        'url': 'api/1.0/salesforcelogin/',
        'email':'user@quarrio.com',
        'h':'002eew3azeerzzWWfZZ'       
     }

config['status'] = { 
        'url': 'status'      
     }
config['text'] = { 
        'url': 'api/1.0/text/?',
        't' : '5'
     }

config['speech'] = { 
        'url': 'api/1.0/speech',
        'HTTP_LANGUAGE':  'en-US',
        'HTTP_FORMAT': 'wav',
         'HTTP_RATE': '48000'
     }

config['logout'] = { 
        'url': 'api/1.0/logout/',
        'id': '398'   
     }

config['visual'] = { 
        'url': 'https://visual.qca-dev.com/api/v/1/visualisation/?',
        'conversationid': '3471',
        'theme': 'light',
        'outputtype': 'table'
        
     }

with open('./dev.ini', 'w') as configfile:
      config.write(configfile)

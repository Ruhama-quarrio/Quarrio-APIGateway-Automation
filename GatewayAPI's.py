import requests
import json
import jwt
import configparser
config = configparser.ConfigParser()
#config.sections()
config.read('dev.ini')
print(config.sections())
#for key in config['dal']:
#    print(key)
def getToken():
    loginURL= config['DEFAULT']['LoginURL']
    body = {"email":"ruhama.sardar@quarrio.com","password":"Ruha@098"}
    headers = {'Content-type': 'application/json'}
    response = requests.post(url = loginURL,data=json.dumps(body), headers=headers)
    loginResponse = json.loads(response.text) 
    token = loginResponse["token"]
    decoded_token  = jwt.decode(token,'i81nl7e@njx6qmeon9hQ1LF8o#4y=tcc%58@l=pntcp34pfugb')
    userid = decoded_token["user_id"]
    print ("token:", token)
    print ("userid:", userid)
    print("login response:", response.status_code) 
    print ("#######END##########")
    return token

def apis():     
    token = getToken()
    quarrioapi = {
            
#############################Dal #############################
                  "dal": {
                        
           "url": config['DEFAULT']['baseURL']+config['dal']['url']+"q="+config['dal']['q']+" &id=" +config['dal']['id'],
          "reqType": "get",
           "headers": {
               "Content-type": "application/json",
               "Authorization" : 'jwt ' + token,
           },
           "printname": "dal"
       },
#############################parser #############################
                              "parser": {
            "url": config['DEFAULT']['baseURL']+config['parser']['url']+"q="+config['parser']['q']+" &id=" +config['parser']['id'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "parser"
      },
#############################Conversation #############################                    
                      "Get/conversation": {
            "url": config['DEFAULT']['baseURL']+config['getConversation']['url']+"userid="+config['getConversation']['userid']+" &limit=" +config['getConversation']['limit'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "Get/conversation"
        },
                              "post/Conversation": {
          "url": config['DEFAULT']['baseURL']+config['postConversation']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {

	"question": config['postConversation']['question'],
	"userId":config['postConversation']['userId'],
	"dateTime": config['postConversation']['dateTime'],
	"lang":config['postConversation']['lang']             
           },
                   "printname": "post/Conversation"
       },
 ############################Datasource #############################             
            "get/Datasource": {
            "url": config['DEFAULT']['baseURL']+config['getDatasource']['url'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/Datasource"
        },
                          "post/DataSource": {
          "url": config['DEFAULT']['baseURL']+config['postDatasource']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
                   
	 "dbId": config['postDatasource']['dbId'],
  "istokenExpired": config['postDatasource']['istokenExpired'],
  "salesforceEmail": config['postDatasource']['salesforceEmail'],
  "salesforceSyncInterval": config['postDatasource']['salesforceSyncInterval'],
  "sfOrgId": config['postDatasource']['sfOrgId'],
  "synchronizationStageId": config['postDatasource']['synchronizationStageId'],
  "userId": config['postDatasource']['userId'],
  "userRole": config['postDatasource']['userRole']
               
           },
                   "printname": "post/DataSource"
       },
           "Put/Datasource": {
          "url": config['DEFAULT']['baseURL']+config['putDatasource']['url'],
           "reqType": "put",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	 "dbId": config['putDatasource']['dbId'],
  "istokenExpired": config['putDatasource']['istokenExpired'],
  "salesforceEmail": config['putDatasource']['salesforceEmail'],
  "salesforceSyncInterval": config['putDatasource']['salesforceSyncInterval'],
  "sfOrgId": config['putDatasource']['sfOrgId'],
  "synchronizationStageId": config['putDatasource']['synchronizationStageId'],
  "userId": config['putDatasource']['userId'],
  "userRole": config['putDatasource']['userRole']             
           },
                   "printname": "Put/Datasource"
       },
           
    "delete/Datasource": {
            "url": config['DEFAULT']['baseURL']+config['deleteDatasource']['url']+"userId="+config['deleteDatasource']['userId'],
            "reqType": "delete",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "delete/Datasource"
        },   
############################feedback #############################                   
           "Post/feedback": {
          "url": config['DEFAULT']['baseURL']+config['postfeedback']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "cc": config['postfeedback']['cc'],
  "email":config['postfeedback']['email'],
  "userEmail": config['postfeedback']['userEmail'],
  "message": config['postfeedback']['message'],
  "name": config['postfeedback']['name'],
  "questionLabel": config['postfeedback']['questionLabel'],
  "subject": config['postfeedback']['subject']
            
           },
                   "printname": "post/feedback"
       },  
############################get-all-users #############################   
                     "get/get-all-users": {
            "url": config['DEFAULT']['baseURL']+config['getAllUsers']['url'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/get-all-users"
      },
                    
############################get-user-org #############################
        
       "get/get-user-org": {
            "url": config['DEFAULT']['baseURL']+config['getUserOrg']['url']+"orgId="+config['getUserOrg']['orgid'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/get-user-org"
      },
############################get-user-by-type #############################
        "get/get-users-by-type": {
            "url": config['DEFAULT']['baseURL']+config['getUserByType']['url']+"typeId="+config['getUserByType']['typeId'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/get-users-by-type"
      },
          
############################Organization #############################
                    "Get/Organization": {
            "url": config['DEFAULT']['baseURL']+config['getOrganization']['url'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "Get/Organization"
        },
    "post/Organization": {
          "url": config['DEFAULT']['baseURL']+config['postOrganization']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	
  "id": config['postOrganization']['id'],
  "name": config['postOrganization']['name'],
        
           },
                   "printname": "Post/Organization"
       },
    "Put/Organization": {
          "url": config['DEFAULT']['baseURL']+config['putOrganization']['url'],
           "reqType": "put",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
    	"id": config['putOrganization']['id'],
  "name": config['putOrganization']['name'],           
           },
       "printname": "Put/Organization"
       },                    
     "delete/Organization": {
            "url": config['DEFAULT']['baseURL']+config['deleteOrganization']['url']+"id="+config['deleteOrganization']['id']+" &name=" +config['deleteOrganization']['name'],
            "reqType": "delete",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "delete/Organization"
        },   
 #############################questions/favorite #############################
       "get/questions/Favorite": {
            "url": config['DEFAULT']['baseURL']+config['getquestionFavourite']['url']+"userId="+config['getquestionFavourite']['userId']+" &limit=" +config['getquestionFavourite']['limit'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
      "printname": "get/questions/Favorite"
        },
       "Post/questions/favorite": {
          "url": config['DEFAULT']['baseURL']+config['postquestionFavourite']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": config['postquestionFavourite']['questionId'],
      "userId":config['postquestionFavourite']['userId']
               
           },
                   "printname": "Post/questions/favorite"
       },
       "Post/questions/unfavorite": {
          "url": config['DEFAULT']['baseURL']+config['postquestionUnFavourite']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": config['postquestionUnFavourite']['questionId'],
      "userId":config['postquestionUnFavourite']['userId']
      
               
           },
                   "printname": "Post/questions/unfavorite"
       }, 
#############################questions/pin ############################# 
                             "get/questions/Pin": {
            "url": config['DEFAULT']['baseURL']+config['getquestionPin']['url']+"userId="+config['getquestionPin']['userId']+" &limit=" +config['getquestionPin']['limit'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/questions/Pin"
        },
           
       
         "Post/questions/Pin": {
          "url": config['DEFAULT']['baseURL']+config['postquestionPin']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": config['postquestionPin']['questionId'],
      "userId":config['postquestionPin']['userId']
               
           },
                   "printname": "Post/questions/Pin"
       },
                    "post/questions/unpin": {
          "url": config['DEFAULT']['baseURL']+config['postquestionUnpin']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": config['postquestionUnpin']['questionId'],
      "userId":config['postquestionUnpin']['userId']
      
               
           },
                   "printname": "post/questions/unpin"
       },
#############################reset-user-password #############################
     "post/reset-user-password": {
          "url": config['DEFAULT']['baseURL']+config['resetPassword']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "confirmPassword": config['resetPassword']['confirmPassword'],
	"currentPassword" : config['resetPassword']['currentPassword'],
	"email": config['DEFAULT']['email'],
	"password": config['resetPassword']['password']
      
               
           },
                   "printname": "post/reset-user-password"
       },
                   
#############################send email #############################
        "post/Send-email": {
          "url": config['DEFAULT']['baseURL']+config['postSendEmail']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	"bcc": config['DEFAULT']['bcc'],
  "cc": config['DEFAULT']['cc'],
  "email": config['DEFAULT']['email'],
  "message": config['postSendEmail']['message'],
  "subject": config['postSendEmail']['subject'],
  "theme": config['DEFAULT']['theme']
 	       
           },
                   "printname": "post/Send-email"
       },   
                   
#############################settings #############################
                       "get/settings": {
            "url": config['DEFAULT']['baseURL']+config['getSettings']['url']+"userId="+config['getSettings']['userId']+" &limit=" +config['getquestionPin']['limit'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/settings"
        },
                      "post/Settings": {
          "url": config['DEFAULT']['baseURL']+config['postSettings']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           }, 
           "body": {
             "dataLimit": config['postSettings']['dataLimit'],
             "userId": config['postSettings']['userId'],
             "language": config['postSettings']['language'],
             "scheduleTime": config['postSettings']['scheduleTime'],
             "scheduleTypeId": config['postSettings']['scheduleTypeId'],
             "theme": config['DEFAULT']['theme']
             
           },
                   "printname": "post/Settings"
       }, 
#############################user-org-type #############################
    "get/user-org-type": {
            "url": config['DEFAULT']['baseURL']+config['userOrgType']['url']+"token="+config['userOrgType']['token'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-org-type"
        },           
#############################user-search #############################
              "get/user-search": {
            "url": config['DEFAULT']['baseURL']+config['userSearch']['url']+"userId="+config['userSearch']['userId'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-search"
        },       
                    
##############################user-type #############################
                    "get/user-type": {
            "url": config['DEFAULT']['baseURL']+config['userType']['url']+"typeId="+config['userType']['typeId'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-type"
        },
                    
#############################user-verify-token #############################
        "get/user-verify-token": {
            "url": config['DEFAULT']['baseURL']+config['userverifyToken']['url']+"token="+config['userverifyToken']['token'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-verify-token"
        },    
##############################QCA-users #############################
                       "get/User": {
            "url": config['DEFAULT']['baseURL']+config['getQcaUser']['url']+"userId="+config['getQcaUser']['userId'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/User"
        },
                     "post/user": {
          "url": config['DEFAULT']['baseURL']+config['putQcaUser']['url'],
           "reqType": "put",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  
        "userId": config['putQcaUser']['userId'],
        "username": config['putQcaUser']['username'],
        "email": config['putQcaUser']['email'],
        "firstName": config['putQcaUser']['firstName'],
        "lastName": config['putQcaUser']['lastName'],
        "phone": config['putQcaUser']['phone']
               
           },
                   "printname": "put/user"
       },    
#############################Salesforce #############################
                "post/Update-Salesforce-Email": {
          "url": config['DEFAULT']['baseURL']+config['postUpdateSalesforceEmail']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
      "userId": config['postUpdateSalesforceEmail']['userId'],
      "salesforceEmail":config['postUpdateSalesforceEmail']['salesforceEmail']
               
           },
                   "printname": "post/Update-Salesforce-Email"
       },   
                   "get/salesforce-Get-User-Details": {
            "url": config['DEFAULT']['baseURL']+config['getSalesforceUserDetails']['url']+"id="+config['getSalesforceUserDetails']['id'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/salesforce-Get-User-Details"
        },
                    "get/salesforce-Disconnect": {
            "url": config['DEFAULT']['baseURL']+config['getSalesforcrceDisconnect']['url']+"operation_type="+config['getSalesforcrceDisconnect']['operation_type']+"&admin_id=" +config['getSalesforcrceDisconnect']['admin_id'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/salesforce-Disconnect"
        },
                     "post/salesforce-Login": {
          "url": config['DEFAULT']['baseURL']+config['postSalesforcrcelogin']['url'],
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "email": config['postSalesforcrcelogin']['email'],
      "h": config['postSalesforcrcelogin']['h'],
               
           },
                   "printname": "post/salesforce-Login"
       }, 
#############################status #############################
                          "get/status": {
            "url": config['DEFAULT']['baseURL']+config['status']['url'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/status"
        },
                    
##############################Text #############################
              "get/text": {
            "url": config['DEFAULT']['baseURL']+config['text']['url']+"t="+config['text']['t'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/text"
        },
#############################Speech #############################                 
       "speech": {
            "url": config['DEFAULT']['baseURL']+config['speech']['url'],
            "reqType": "post",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "body": {
                            "HTTP_LANGUAGE": config['speech']['HTTP_LANGUAGE'],
                            "HTTP_FORMAT": config['speech']['HTTP_FORMAT'],
                            "HTTP_RATE": config['speech']['HTTP_RATE']          
           },
                        "printname": "speech"    
        },    
###############################Text #############################
              "get/visual": {
            "url": config['visual']['url']+"conversationid="+config['visual']['conversationid']+" &theme=" +config['visual']['theme']+" &outputtype=" +config['visual']['outputtype'],
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/visual"
        },        
##############################logout #############################  
                     "logout": {
            "url": config['DEFAULT']['baseURL']+config['logout']['url'],
            "reqType": "post",
        "headers": {
                "Content-type": "application/json",
               
            },
                 
           "body": {
                "token" : token,
                    "id": config['logout']['id'],
            },       
          "printname": "logout"
        },                           
                                   
                   }
    for key, value in quarrioapi.items():
        apiKey= key
        apiInfo = value
        #print(apiKey)
        #print(apiInfo)
        print("###############################")
        urlHost = ''
        printname = ''
        reqType = ''
        header = {}
        body = {}
        for key,value in apiInfo.items():
            keyInApiInfo = key
            valueInApiInfo = value
            if keyInApiInfo == 'url':
                urlHost = valueInApiInfo
            if keyInApiInfo == 'reqType':
                reqType = valueInApiInfo
            if keyInApiInfo == 'headers':
                for key, value in valueInApiInfo.items():
                    keyInHeader = key
                    valueInHeader = value
                    header[keyInHeader] = valueInHeader
            if keyInApiInfo == 'body':
                for key, value in valueInApiInfo.items():
                    body[key] = value
            if keyInApiInfo == 'printname':
                printname = valueInApiInfo
        if reqType =='get':
            print("URL:", urlHost)
            print("RequestType:", reqType)
            print("header:", header)
            print("body:", body)
            response = requests.get(url=urlHost,data=json.dumps(body), headers=header)
            print(printname+  " response:", response.status_code)
            print("GET API response:",response.text)
        elif reqType == 'post':
            print ("URL:", urlHost)
            print("RequestType:", reqType)
            print("header:", header)
            print("body:", body)
            response = requests.post(url=urlHost,data=json.dumps(body), headers=header)
            print(printname+  " response:", response.status_code)
            print ("POST API response:",response.text)
        elif reqType =='put':
            print("URL:", urlHost)
            print ("RequestType:", reqType)
            print ("header:", header)
            print ("body:", body)
            response= requests.put(url=urlHost,data=json.dumps(body), headers=header)
            print(printname+  " response:", response.status_code)
            print("Put API response:",response.text)
        elif reqType =='delete':
            print("URL:", urlHost)
            print ("RequestType:", reqType)
            print ("header:", header)
            print ("body:", body)
            response= requests.delete(url=urlHost,data=json.dumps(body), headers=header)
            print(printname+  " response:", response.status_code)
            print("delete API response:",response.text)
               
            
            
apis()
           
         
           
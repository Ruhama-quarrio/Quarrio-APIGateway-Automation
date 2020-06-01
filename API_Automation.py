import requests
import json
import jwt
def getToken():
    loginURL= "https://auth.qca-dev.com/api/api/1.0/login/"
    body = {"email":"ruhama.sardar@quarrio.com","password":"Ruha@12345"}
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
           "url": "http://auth.qca-dev.com/api/1.0/dal?q=list of accounts&id=398",
          "reqType": "get",
           "headers": {
               "Content-type": "application/json",
               "Authorization" : 'jwt ' + token,
           },
           "printname": "dal"
       },
                   
#############################Eparser #############################
                    "parser": {
            "url": "http://auth.qca-dev.com/api/1.0/parser/?q=list of accounts&id=398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "parser"
      },
                    
#############################Conversation #############################
                    "Get/conversation": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/conversation/?userid=398&limit=3",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "Get/conversation"
        },
                      "post/Conversation": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/conversation/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	"question": "number of accounts",
	"userId": "398",
	"dateTime": "2020-03-18 05:12:30",
	"lang":"english"               
           },
                   "printname": "post/Conversation"
       },
                   
#############################datasource #############################
                        "get/Datasource": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/datasource/",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/Datasource"
        },
                        "post/DataSource": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/datasource/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	 "dbId": "string",
  "istokenExpired": "true",
  "salesforceEmail": "ruhama123@quarrio.com",
  "salesforceSyncInterval": 0,
  "sfOrgId": "string",
  "synchronizationStageId": 0,
  "userId": 398,
  "userRole": "string"
               
           },
                   "printname": "post/DataSource"
       },
           "Put/Datasource": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/datasource/",
           "reqType": "put",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "userId": 398,
  "dbId": "string",
  "istokenExpired": "true",
  "salesforceEmail": "string",
  "salesforceSyncInterval": 0,
  "sfOrgId": "string",
  "synchronizationStageId": 0,
  "userRole": "string"              
           },
                   "printname": "Put/Datasource"
       },
    "delete/Datasource": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/datasource/",
            "reqType": "delete",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "delete/Datasource"
        },   
                    
#############################feedback #############################
          "Post/feedback": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/feedback/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "cc": "ruhama.sardar@quarrio.com",
  "email": "ruhama.sardar@quarrio.com",
  "userEmail": "ruhama.sardar@quarrio.com",
  "message": "string",
  "name": "string",
  "questionLabel": "list of accounts",
  "subject": "string"
            
           },
                   "printname": "post/feedback"
       },
                
#############################get-all-users #############################   
                     "get/get-all-users": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/get-all-users/",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/get-all-users"
      },
                    
#############################get-user-org #############################
    "get/get-user-org": {
            "url": "http://auth.qca-dev.com/api/1.0/qca/get-user-org/?orgId=2",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/get-user-org"
      },     
                    
#############################get-user-by-type #############################
        "get/get-users-by-type": {
            "url": "http://auth.qca-dev.com/api/1.0/qca/get-users-by-type/?typeId=3",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/get-users-by-type"
      },   
                    
#############################Organization #############################
                    "Get/Organization": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/organization/",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "Get/Organization"
        },
    "post/Organization": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/organization/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	
  "id": 398,
  "name": "ruhama",
        
           },
                   "printname": "Post/Organization"
       },
    "Put/Organization": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/organization/",
           "reqType": "put",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
    	"id": 398,
      "name": "ruhama.sardar@quarrio.com"             
           },
       "printname": "Put/Organization"
       },                    
     "delete/OrganizationController(id)": {
            "url": "http://auth.qca-dev.com/api/1.0/qca/organization/?id=196",
            "reqType": "delete",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "delete/Organization"
        },   
    
#############################questions/favorite #############################
       "get/questions/Favorite": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/questions/favorite/?limit=5&userId=398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
      "printname": "get/questions/Favorite"
        },
       "Post/questions/favorite": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/questions/favorite/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": "919",
      "userId":"398",
               
           },
                   "printname": "Post/questions/favorite"
       },
       "Post/questions/unfavorite": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/questions/unfavorite/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": "919",
      "userId": "398",
      
               
           },
                   "printname": "Post/questions/unfavorite"
       }, 
                      "get/questions/Pin": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/questions/pin/?limit=5&userId=398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/questions/Pin"
        },
           
#############################questions/pin #############################         
         "Post/questions/Pin": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/questions/pin/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": "919",
      "userId": "398",
               
           },
                   "printname": "Post/questions/Pin"
       },
                    "post/questions/unpin": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/questions/unpin/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "questionId": "919",
      "userId": "398",
      
               
           },
                   "printname": "post/questions/unpin"
       },
                   
#############################reset-user-password #############################
     "post/reset-user-password": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/reset-user-pwd/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "confirmPassword": "Test@098",
	"currentPassword" : "Test@123",
	"email": "ruhama.sardar@quarrio.com",
	"password": "Test@098"
      
               
           },
                   "printname": "post/reset-user-password"
       },
                   
#############################send email #############################
        "post/Send-email": {
          "url": "http://auth.qca-dev.com/api/1.0/qca/send-email/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	 "bcc": "ruhama.sardar@quarrio.com",
  "cc": "ruhama.sardar@quarrio.com",
  "email": "ruhama.sardar@quarrio.com",
  "message": "list of opps/opportunities",
  "subject": "PostSendEmail"
               
           },
                   "printname": "post/Send-email"
       },   
                   
#############################settings #############################
                       "get/settings": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/setting/?limit=5&userId=398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/settings"
        },
                      "post/Settings": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/setting/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           }, 
           "body": {
             "dataLimit": "2",
             "userId": "398",
             "language": "english",
             "scheduleTime": "01:01:11",
             "scheduleTypeId": "1",
             "theme": "null"
             
           },
                   "printname": "post/Settings"
       }, 
                   
#############################user-org-type #############################
    "get/user-org-type": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/user-org-type/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozOTgsImVtYWlsIjoicnVoYW1hLnNhcmRhckBxdWFycmlvLmNvbSIsInVzZXJuYW1lIjoicnVoYW1hLnNhcmRhckBxdWFycmlvLmNvbSIsImV4cCI6MTU5MTA5NTYwOCwiZmlyc3RfbmFtZSI6InJ1aGFtYSJ9.QIfyh1ZSzFfu1v57tDMWymZIQGOT5oqP3_6oe3RdLDU",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-org-type"
        },
                    
#############################user-search #############################
              "get/user-search": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/user-search/?userId=398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-search"
        },       
                    
#############################user-type #############################
                    "get/user-type": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/user-type/?typeId=3",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-type"
        },
                    
#############################user-verify-token #############################
        "get/user-verify-token": {
            "url": "http://auth.qca-dev.com/api/1.0/qca/user-verify-token/26cfbce3-5622-4888-98c2-6145db7ff68c-NewUserToken",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/user-verify-token"
        },    
                    
#############################EQCA-users #############################
                       "get/User": {
            "url": "https://auth.qca-dev.com/api/1.0/qca/user/?userId=398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/User"
        },
                     "post/user": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/user/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  
      "userId": "398",
      "salesforceEmail": "ruhama.sardar@quarrio.com"
               
           },
                   "printname": "post/user"
       },    
                   
#############################Salesforce #############################
                "post/Update-Salesforce-Email": {
          "url": "https://auth.qca-dev.com/api/1.0/qca/user/update-salesforce-email/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
      "userId": "235",
      "salesforceEmail":"ruhama.sardar@quarrio.com"
               
           },
                   "printname": "post/Update-Salesforce-Email"
       },   
                   "get/salesforce-Get-User-Details": {
            "url": "https://auth.qca-dev.com/api/1.0/salesforce/get-user-details/?id= 398",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/salesforce-Get-User-Details"
        },
                    "get/salesforce-Disconnect": {
            "url": "https://auth.qca-dev.com/api/1.0/salesforce/salesforce-disconnect/?operation_type=allsubuser&admin_id=235",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                 
                    "printname": "get/salesforce-Disconnect"
        },
                     "post/salesforce-Login": {
          "url": "https://auth.qca-dev.com/api/1.0/salesforcelogin/",
           "reqType": "post",
       "headers": {
               "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
           },
           "body": {
	  "email": "ruhama.sardar@quarrio.com",
      "h": "002eew3azeerzzWWfZZ",
               
           },
                   "printname": "post/salesforce-Login"
       }, 
                   
#############################status #############################
                          "get/status": {
            "url": "https://auth.qca-dev.com/status",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/status"
        },
                    
#############################Text #############################
              "get/text": {
            "url": "http://auth.qca-dev.com/api/1.0/text/?t=5",
            "reqType": "get",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "printname": "get/text"
        },
#############################Speech #############################                 
       "speech": {
            "url": "https://auth.qca-dev.com/api/1.0/speech",
            "reqType": "post",
            "headers": {
                "Content-type": "application/json",
                "Authorization" : 'jwt ' + token,
            },
                    "body": {
                            "HTTP_LANGUAGE":  "en-US",
                            "HTTP_FORMAT": "wav",
                            "HTTP_RATE": "48000",            
           },
                        "printname": "speech"    
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
            #print("header:", header)
            #print("body:", body)
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
            print("PUT API response:",response.text)
            
apis()
                    
         
                    


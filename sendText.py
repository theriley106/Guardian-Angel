import os

message = """Chris has requested a guardian angel to overlook his walk home.  Check out: https://guardianangels.herokuapp.com/mySite?person=Chris&location=Home"""
os.system("lib messagebird.sms.create --recipient 18646097067 --body {}".format(message))

import facebook
import requests
result = facebook.GraphAPI(access_token='EAABtcFAn6i8BALoudmjWvAbCSrFxlgEZBQZC0NHXrDM0Q832VbDghxDsTEwIdjUznLzWuE0zMtJUUufagLsSGf0K8OiMutRZCNMnlxRZC49Sw7zu3YDguZAl9w687vtzDipZBgcFY4UqspseiG5nZBP0Ye56b87AcunFAUiZCg6YABbyPmBUsn35cMZC9FLBZCz8wZD', version='2.7')
users = result.search(type='user', q='Awuor Marvin')

# Each given id maps to an object.
for user in users['data']:
    print('%s %s' % (user['id'],user['name'].encode()))
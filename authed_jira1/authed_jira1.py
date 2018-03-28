from jira.client import JIRA
import logging
import urllib3
import os

urllib3.disable_warnings()

# Defines a function for connecting to Jira
def connect_jira(log, jira_server, jira_user, jira_password):
    '''
    Connect to JIRA. Return None on error
    '''
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server,'verify':False}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
                                        # ^--- Note the tuple
        return jira
    except Exception as e:
        log.error("Failed to connect to JIRA: %s" % e)
        return None

# create logger
log = logging.getLogger(__name__)
logging.info("Begin")

# read credentials from environment
username = os.environ['JIRA_USER']
password = os.environ['JIRA_PASS']
print("Username: ", username)
#print("Password: ", password)

#quit()

# create a connection object, jc
jc = connect_jira(log, "https://czjira.ness.com", username, password)

# read details for issue
issue = jc.issue('CUZKRUIAN-12345')

# print the issue details
print("Summary: ", issue.fields.summary)
print("Type: ", issue.fields.issuetype.name)
print("Reporter: ", issue.fields.reporter.displayName)

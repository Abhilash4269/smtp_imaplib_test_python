import imaplib , email

user = "abhilash.d@tessrac.com"
password =""
imap_url ="outlook.office365.com"

con = imaplib.IMAP4_SSL(imap_url)
con.login(user,password)
con.select('inbox')

result, data = con.fetch()

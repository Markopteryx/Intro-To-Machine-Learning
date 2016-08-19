

import urllib
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz"
urllib.request.urlretrieve(url, filename="../enron_mail_20150507.tgz") 
print ("download complete!")


print ("unzipping Enron dataset (this may take a while)")
import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
tfile.extractall(".")

print ("you're ready to go!")

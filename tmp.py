# http://omz-software.com/pythonista/docs/

import sys # docs.python.org/3/library/sys.html#module-sys
import clipboard
import console
import re
import datetime
import calendar
import json
import urllib
import urllib3
import urllib.request as req
from pytz import timezone
import webbrowser, os # to open browser
import configparser # to use config file

def main():
  print("hello")


if __name__ == "__main__":
  main()


class Url:
  # class attribute 
    # type 4 ex: amazon.com/Camera-Recorder-Fuvision-Portable-Recording/dp/B07GRRLCYS/ref=pd_aw_sbs_421_14
  urlVarType = {
    "1":"URL vars start after '?', separate with '&', and assign value with '=',
  	"2":"URL vars start after '?rh=', separate with ',', and assign value with ':'",
  	"3":"URL var value starts after '/'",
  	"4":"URL var value starts adter '/ref='"
  }
  
  urlVarTypeChkOrder = {
  	"1":"2",
  	"2":"1",
  	"4":"3",
  	"3":"4"
  }
  
  @staticmethod
  def getDomainNm(url):
    return url.split("/")[0]
    
    
  def chkSafeUrl(url):
    return 0
    
    
  def chkUrlRedirect(url)
    return 0
    
    
  def seeTrackerUsed(url):
    return 0
    
    
  def seeMyAccessibleInfo(url):
    return 0
    
    
  def chkSafeNews(url):
    return 0
  	
  def cleanUrl(url):
    return 0
  	
  	
  @staticmethod
  def rmvUrlPrefix(url):
    prefix = [
      "http://mobile.",
      "http://m.",
      "http://www.",
      "https://mobile.",
      "https://m.",
      "https://www.",
      "https://",
      "http://"
    ]
    
    for i in prefix:
      url = url.replace(i,"")
    return url 
    
    
  @classmethod
  def chkUrlVarType1(url):
    urlParts = url.split("?")
    urlDomainNm = getDomainNm(urlParts[0])
    if urlParts.count == 2:
      urlVarValStr = urlParts[1]
      if urlVarValStr.split("&").count == 2:
        print("Have - " + urlVarType[1])
        return 1
      else:
        return 0
    else:
      return 0
    
    
  @classmethod
  def chkUrlVarType2(url):
    if "?rh=" in url:
      print("Have - " + urlVarType[2])
      return 1
    else:
      return 0
    
    
  @classmethod
  def chkUrlVarType3(url):
    urlParts = url.split("/")
    urlVarVal = urlParts[-1]
    urlVar = urlVarVal.split("=")[0]
    if urlVar in urlVar_rmv3[urlDomainNm]:
      print("Have - " + urlVarType[3])
      return 1
    else:
      return 0
  
  
  def rmvUrlVar(url):
	  if chkUrlVarType1(url) == 1:
	    url = rmvUrlVarType1(url)
	  if chkUrlVarType2(url) == 1:
	    url = rmvUrlVarType2(url)
	  if chkUrlVarType3(url) == 1:
	    url = rmvUrlVarType3(url)
	  return url 
  
  
  def rmvUrlVarType1(url,urlVarsStr):
  	urlVarsStr = rmvUrlVarType1Auto(url) + rmvUrlVarType1Manual(url)
	  urlFix = url.split("?")[0] + ("?" if len(urlVarsStr) > 0 else "") + urlVarsStr[0:len(urlVarsStr)]
	  return urlFix
	  
  def rmvUrlVarType1Auto(url):
    return urlVarsStr

  def rmvUrlVarType1Manual(url):
    return urlVarsStr
	    
  def rmvUrlVarType2(url):

      
  def rmvUrlVarType3(url):


# Uses Url class in this file
class DanceByMe:
  def __init__(self):
    # instance attrbute 
    time_start = xxx  # default
    time_end = xxx  # default

  def mkJsonDoc(self):
  def getDocTemplate(self):
  def getAddress(self):
  def getGeoCode(self):
  def getDateTime(self):
  def getUrl(self): 
  def getPossibleVal(self):
  def getDefaultVal(self):
  def chgAttVal(self):
  def chgLine(self):
  def setFieldFormat(self):
  def mkAttValPrompt(self,attNm,dict):
    return attNm + "("+ Util.dict2str(dict) + ")"
    
  
class Util:
	
  def getWkDyOccurrence():
  def getOffsetFromGMT():
  def getYYMMDD_format():
  def getMongoDbISODate():
  def addYrPrefix(n):
	  now = datetime.datetime.now()
	  if len(n) > 2:
	    return n
	  else:
	    if int(n) > int(str(now.year + 1)[:2]):
	      n = "19" + n
	    else:
	      n = "20" + n
	  return n
	  
	  
  def addZeroPrefix():
  def collectMultiVal():
  def collectSingleVal():
  
  @staticmethod
  def lst2str():
    return 0
  
  @staticmethod
  def dict2str(dict):
    str = ""
    for key, value in dict.items():
      str = str + ", ("+key+")"+value[len(key):len(value)]
    return str[2:len(str)]
  
class Config:
  config = configparser.RawConfigParser()
  config.optionxform = str # keeps key case
  config.read('url.cfg')
  
  # create dictionary to hold config
	dictionary = {}
	for section in config.sections():
		# create each section dict
	  dictionary[section] = {}
	  for option in config.options(section):
	    val = config.get(section, option)
	    dictionary[section][option] = val
	    
	docNameLst = dictionary['docNameLst']
	
	fieldDefaultVal = dictionary['fieldDefaultVal']
	
	danceTypeDict = dictionary['danceTypeDict']
	
	fieldFormat = dictionary['fieldFormat']
	
	fieldValidVal = {
	 "instance":"int",
	"fallsOnInstance":fieldFormat["fallsOnInstance"],
	"alcohol":fieldFormat["alcohol"],
	"canVary":fieldFormat["canVary"],
	"liveMusic":fieldFormat["liveMusic"],
	"eventGroupID":"int",
	"eventID":"float",
	"eventGroupParts":"int"
	}
	
	floorDict = dictionary['floorDict']
	
	typeDict = dictionary['typeDict']
	
	periodDict = dictionary['periodDict']
	
	classVarDict = {
	  "oneGeoOneDay",""
	}
	
	urlVar_rmv = dictionary['urlVar_rmv']
	
	urlVar_rmv2 = dictionary['urlVar_rmv2']
	
	urlVar_rmv3 = dictionary['urlVar_rmv3']
	
	urlVar_non_rmv = dictionary['urlVar_non_rmv']
	
	newsTrust = dictionary['newsTrust']
	newsNonTrust = dictionary['newsNonTrust']

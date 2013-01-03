#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
	import httplib2 #http://code.google.com/p/httplib2/wiki/ExamplesPython3
except ImportError:
	raise Exception("try install.sh and install httplib2")
try:
	import pygame #http://d.hatena.ne.jp/umedoblock/20111001/1317424082
	pygame.mixer.init()
except ImportError:
	raise Exception("try install.sh and install pygame")
#else:
#	raise Exception("mixer.init() raised error")
try:
	import suds #https://fedorahosted.org/suds/#Documentation
except ImportError:
	raise Exception("try install.sh and install suds")

import os

class MicrosoftBingAPI():
	"""
	2011 12 01
	Syake
	"""
	def __init__(self,APIkey,lang="ja"):
		self.APIKey=APIkey
		self._lang=lang
		self._MicrosoftAPIurl="http://api.microsofttranslator.com/V2/Soap.svc"
		self._mss = suds.client.Client(self._MicrosoftAPIurl)
		self.call = self._mss.service
		self.LanguageForSpeak=['ca', 'ca-es', 'da', 'da-dk', 'de', 'de-de', 'en','en-au', 'en-ca', 'en-gb', 'en-in', 'en-us', 'es', 'es-es', 'es-mx', 'fi', 'fi-fi', 'fr', 'fr-ca', 'fr-fr', 'it', 'it-it', 'ja', 'ja-jp', 'ko', 'ko-kr', 'nb-no', 'nl', 'nl-nl', 'no', 'pl', 'pl-pl', 'pt', 'pt-br', 'pt-pt', 'ru', 'ru-ru', 'sv', 'sv-se', 'zh-chs', 'zh-cht', 'zh-cn', 'zh-hk', 'zh-tw']
		self.LanguageForTranslate=['ar', 'bg', 'ca', 'zh-CHS', 'zh-CHT', 'cs', 'da', 'nl', 'en', 'et', 'fi', 'fr', 'de', 'el', 'ht', 'he', 'hi', 'hu', 'id', 'it', 'ja', 'ko', 'lv', 'lt', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'es', 'sv', 'th', 'tr', 'uk', 'vi']
		self.ContentType=["text/plain","text/html"]
		self.Category=["general"]
		self.Format=["audio/wav"]
		self.MaxSecond=86400
		self._http=httplib2.Http()

	def __doc__(self):
		return self._mss.__str__()

	def __str__(self):
		return self._mss.__str__()

	def __del__(self):
		pygame.mixer.quit()

	def _isValidLanguageForSpeak(self,lang):
		if str(lang) not in self.LanguageForSpeak:
			return False
		return True

	def _isValidLanguageForTranslate(self,lang):
		if str(lang) not in self.LanguageForTranslate:
			return False
		return True

	def AddTranslation(self,originalText,translatedText,fromLanguage,toLanguage,\
	rating=10,contentType="text/plain",category="general",user="ME",*uri):
		return self.call.AddTranslation(self.APIKey,originalText,translatedText,fromLanguage,toLanguage,rating,contentType,category,user,uri)

	def BreakSentences(self,Sentences,language):
		return self.call.BreakSentences(self.APIKey,Sentences,language)

	def Detect(self,text):
		return self.call.Detect(self.APIKey,text)

#	def DetectArray(self,texts):
#		return self.call.DetectArray(self.APIKey,texts)

	def GetAppIdToken(self,minRatingRead=5,maxRatingWrite=4,expireSeconds=86400):#24hour
		return self.call.GetAppIdToken(self.APIKey,minRatingRead,maxRatingWrite,expireSeconds)
	
	def GetTranslations(self,text,fromLanguage,toLanguage,maxTranslations=100,*options):
		return self.call.GetTranslations(self.APIKey,text,fromLanguage,toLanguage,maxTranslations,options)

#	def GetTranslationsArray(self,texts,fromLanguage,toLanguage,maxTranslations=100,*options):
#		return self.call.GetTranslationsArray(self.APIKey,texts,fromLanguage,toLanguage,maxTranslations,options)

	def Speak(self,text,language,format="audio/wav"):
		return self.call.Speak(self.APIKey,text,language,format)

	def Translate(self,text,fromLanguage,toLanguage,contentType="text/plain",category="general"):
		return self.call.Translate(self.APIKey,text,fromLanguage,toLanguage,contentType,category)

	def TranslateThis(self,text,toLanguage="ja"):
		return self.Translate(text,str(self.Detect(text)),toLanguage)

#	def TranslateArray(self,texts,fromLanguage,toLanguage,*options):
#		return self.call.TranslateArray(self.APIKey,texts,fromLanguage,toLanguage,options)

	def SpeakThis(self,text,lang=""):
		if not text:
			text=" "
		if not lang:
			lang=str(self.Detect(text))
		filename="Stock/X%s.wav" % hash(text)
		if not os.path.isfile(filename):
			try:
				h,d=self._http.request(str(self.Speak(text,lang)) )
			except:
				raise Exception("ネットワークエラー。第2引数にlang='ja'のように言語を入力してみてください。")
			if h["status"] != "200":
				raise Exception("Microsoft SOAP APIサービスエラー.APIサービス停止もしくは文字が長すぎ。小分けにしろ")
			p=open(filename,"wb")
			p.write(d)
			p.close()
		try:
			pygame.mixer.Sound(filename).play()#Play the voice
		except:
			raise Exception("Error in 'pygame.mixer.Sound(d).play()' ")
		return lang,filename#The Language of the voice

	def SpeakTranslatedThis(self,text,LanguageForSpeak="ja"):
		translated=str(self.Translate(text,str(self.Detect(text)),LanguageForSpeak))
		self.SpeakThis(translated)
		return translated

if __name__ == "__main__":
	#import completer
	from time import sleep
	ms=MicrosoftBingAPI("2F030A04796A594C9CDDFDAFB53A615362E56DC2")
	print(ms.SpeakThis("Hello World!"))
	print(ms.SpeakTranslatedThis("Hello World!"))
	sleep(1)

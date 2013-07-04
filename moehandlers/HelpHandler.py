# coding: utf-8
'''
Created on 2013-7-4
帮助handler
@author: xuechong
'''
import Weixin
import logging

__help_key__ = {"帮助","-help"}
__help_content__="输入 **花语 或者 花语** 可以查看相应的花语哦"
class HelpHandler(object):
   
    def handle(self,handlerChain):
        
        if (handlerChain.getMsgType()=="text"):
            content = handlerChain.getMsgContent()
            if content in __help_key__:
                logging.debug("view help")
                return Weixin.textReply(handlerChain.userMsg, __help_content__);
        return handlerChain.invokeNext()

    
# -*- coding: UTF-8 -*-
# Mendeley app module
#Copyright (C) 2018 Noelia Ruiz Martínez
# Released under GPL 2

import api
import core
import controlTypes
import appModuleHandler
import addonHandler
from NVDAObjects.IAccessible import IAccessible

addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self,obj):
		if obj.role == controlTypes.ROLE_DIALOG:
			api.setForegroundObject(obj)
			if obj.name == "New Document":
				obj.description = None
		if api.getForegroundObject().name == "New Document":
			if obj.role in (controlTypes.ROLE_EDITABLETEXT, controlTypes.ROLE_CHECKBOX):
				labelObj = obj.simplePrevious
				if labelObj and labelObj.role == controlTypes.ROLE_STATICTEXT:
					obj.name = labelObj.name

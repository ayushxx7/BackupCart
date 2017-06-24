# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "paperkart"
app_title = "Paperkart"
app_publisher = "openetech"
app_description = "Paperkart"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@openetech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/paperkart/css/paperkart.css"
# app_include_js = "/assets/paperkart/js/paperkart.js"

# include js, css files in header of web template
# web_include_css = "/assets/paperkart/css/paperkart.css"
# web_include_js = "/assets/paperkart/js/paperkart.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "paperkart.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "paperkart.install.before_install"
# after_install = "paperkart.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "paperkart.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
has_permission = {
	"Payment Entry": "paperkart.paperkart.paperkart.payment_client.func.has_permission",
 }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Item": {
		"validate": "paperkart.custom_method.validate_item_duplicates"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"paperkart.tasks.all"
# 	],
# 	"daily": [
# 		"paperkart.tasks.daily"
# 	],
# 	"hourly": [
# 		"paperkart.tasks.hourly"
# 	],
# 	"weekly": [
# 		"paperkart.tasks.weekly"
# 	]
# 	"monthly": [
# 		"paperkart.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "paperkart.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "paperkart.event.get_events"
# }
fixtures = ["Custom Field","Custom Script"]

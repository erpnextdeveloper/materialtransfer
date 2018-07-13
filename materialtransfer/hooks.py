# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "materialtransfer"
app_title = "MaterialTransfer"
app_publisher = "MaterialTransfer"
app_description = "Material Transfer"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "maheshwaribhavesh95863@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = ['Custom Field', 'Property Setter', "Custom Script","Print Format"]

# include js, css files in header of desk.html
# app_include_css = "/assets/materialtransfer/css/materialtransfer.css"
# app_include_js = "/assets/materialtransfer/js/materialtransfer.js"

# include js, css files in header of web template
# web_include_css = "/assets/materialtransfer/css/materialtransfer.css"
# web_include_js = "/assets/materialtransfer/js/materialtransfer.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}


doctype_js = {
    "Customer":["custom_script/customer.js"],
    "Delivery Note":["custom_script/delivery_note.js"],
    "Material Request":["custom_script/material_request.js"],
    "Material Transfer":["custom_script/material_transfer.js"],
    "Purchase Invoice":["custom_script/purchase_invoice.js"],
    "Purchase Order":["custom_script/purchase_order.js"],
    "Purchase Receipt":["custom_script/purchase_receipt.js"],
    "Sales Invoice":["custom_script/sales_invoice.js"],
    "Sales Order":["custom_script/sales_order.js"]
}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "materialtransfer.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "materialtransfer.install.before_install"
# after_install = "materialtransfer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "materialtransfer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

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
	"Material Request": {
		"validate": "criscoconsulting.custom_method.material_request_data"
		
	},
    "Material Transfer": {
        "after_insert": "criscoconsulting.custom_method.add_to_on_material_transfer",
        "validate": "criscoconsulting.custom_method.update_material_request_data"
        
    }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"materialtransfer.tasks.all"
# 	],
# 	"daily": [
# 		"materialtransfer.tasks.daily"
# 	],
# 	"hourly": [
# 		"materialtransfer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"materialtransfer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"materialtransfer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "materialtransfer.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "materialtransfer.event.get_events"
# }


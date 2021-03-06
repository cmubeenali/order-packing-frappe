from . import __version__ as app_version

app_name = "order_packing"
app_title = "Order Packing"
app_publisher = "Mubeen Ali"
app_description = "This module is to ease kitchen packing management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "cmubeenali@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/order_packing/css/order_packing.css"
# app_include_js = "/assets/order_packing/js/order_packing.js"

# include js, css files in header of web template
# web_include_css = "/assets/order_packing/css/order_packing.css"
# web_include_js = "/assets/order_packing/js/order_packing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "order_packing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Kitchen Utility"]

# Installation
# ------------

# before_install = "order_packing.install.before_install"
# after_install = "order_packing.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "order_packing.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# this is dummy
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}e
# }

doc_events={
	'Sales Order':{
		'on_submit':'order_packing.order_packing.doctype.kitchen_utility.kitchen_utility.publish_orders_to_kitchen_queue'
	}
}



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"order_packing.tasks.all"
# 	],
# 	"daily": [
# 		"order_packing.tasks.daily"
# 	],
# 	"hourly": [
# 		"order_packing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"order_packing.tasks.weekly"
# 	]
# 	"monthly": [
# 		"order_packing.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "order_packing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "order_packing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "order_packing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"order_packing.auth.validate"
# ]

sounds = [
	{"name": "order_notification", "src": "/assets/order_packing/sounds/notification.wav", "volume": 1}	
]
# Copyright (c) 2021, Mubeen Ali and contributors
# For license information, please see license.txt

import frappe

from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class KitchenUtility(WebsiteGenerator):
	pass

def publish_orders_to_kitchen_queue(arg1,arg2):
	frappe.publish_realtime("new_order","{'status':'new_order'}")
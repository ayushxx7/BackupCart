from __future__ import unicode_literals
import frappe

def get_context(context):
	context.items = frappe.db.sql("select * from `tabItem`", as_dict=True)
from __future__ import unicode_literals
import frappe, json
import frappe.utils


from frappe import _

def validate_item_duplicates(self,method):

	if self.core or self.dia:
		#should core and dia be added to key
		pass		
	item_key = frappe.utils.data.cstr(self.width_cm) + frappe.utils.data.cstr(self.length_cm) + frappe.utils.data.cstr(self.gsm) + frappe.utils.data.cstr(self.grain) + frappe.utils.data.cstr(self.shade) + frappe.utils.data.cstr(self.finish) + frappe.utils.data.cstr(self.net_weight) + frappe.utils.data.cstr(self.stock_uom) + frappe.utils.data.cstr(self.brand)
	self.item_key = item_key
	item_name = frappe.db.sql("""select name from `tabItem` where item_key = %s""",item_key)
	if item_name:
		name = item_name[0][0]
		if self.name == name:
			pass
		else:
			frappe.throw(_("Item Name: {0} with similar attributes already exists").format(name))
	# Create Item Description
	if not self.weight_uom:
		self.weight_uom = self.stock_uom
	#both widh and length then it is a typical item without core and dia
	if self.width_cm and self.length_cm:
		item_description = 	frappe.utils.data.cstr(self.gsm) + "/ " + frappe.utils.data.cstr(self.width_cm) + " * " + frappe.utils.data.cstr(self.length_cm) + " " + frappe.utils.data.cstr(self.net_weight) + " " + frappe.utils.data.cstr(self.weight_uom) + " " + frappe.utils.data.cstr(self.brand)
	#if only width and no length, then core and dia come into picture
	if self.width_cm > 0 and not self.length_cm:
		#if core and dia exist, assumption if there is core there will be dia
		if self.core and self.dia:
			self.description = self.description + frappe.utils.data.cstr(self.core) + frappe.utils.data.cstr(self.dia)
		item_description = 	frappe.utils.data.cstr(self.gsm) + "/ " + frappe.utils.data.cstr(self.width_cm) + " " + frappe.utils.data.cstr(self.core) + " " + frappe.utils.data.cstr(self.dia) + " " + frappe.utils.data.cstr(self.net_weight) + " " + frappe.utils.data.cstr(self.weight_uom) + " " + frappe.utils.data.cstr(self.brand)
	#Override auto name generation
	if not self.override_auto_name and self.width_cm > 0:
		self.item_name = item_description
		self.description = item_description
	#if grain/shade and finish exist add to description
		if self.grain or self.shade or self.finish:
			self.description = frappe.utils.data.cstr(self.grain) + frappe.utils.data.cstr(self.shade) + frappe.utils.data.cstr(self.finish)
	self.web_long_description = self.description
	#reset to manual
	self.override_auto_name = 1

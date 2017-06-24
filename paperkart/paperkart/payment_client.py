import frappe
from frappe.model.document import Document
import json

@frappe.whitelist()
def func(ifsc):
  bank = frappe.get_doc("Bank Master",ifsc)
  b = {}
  b['state'] = bank.state
  b['pin_code'] = bank.pin_code

  return json.dumps(b)
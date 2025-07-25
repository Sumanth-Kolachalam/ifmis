# Copyright (c) 2025, Bel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EmployeeToRegionMapping(Document):
	def autoname(self):
		# Fetch employee first name
		employee_doc = frappe.get_doc("Employee", self.employee)
		employee_firstname = employee_doc.first_name.strip().replace(" ", "-")

		# Fetch region name
		region_doc = frappe.get_doc("Region", self.assigned_to_region)
		region_name = region_doc.name.strip().replace(" ", "-")

		# Set the document name
		self.name = f"{employee_firstname}-to-{region_name}"

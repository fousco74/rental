# Copyright (c) 2025, KONE Fousseni and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Vehicule(Document):

	def validate(self):
		self.set_title()
		

	def set_title(self):
		self.title = f"{self.model} {self.make}, {self.year}"

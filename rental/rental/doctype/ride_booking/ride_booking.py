# Copyright (c) 2025, KONE Fousseni and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	
	def validate(self):
		pass
		#distance_total = 0
		
		#for item in self.items:
			#distance_total += item.distance
			#self.total_amount = distance_total * self.rate
		

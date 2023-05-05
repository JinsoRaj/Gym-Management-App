# Copyright (c) 2023, Jinso Raj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymClassBooking(Document):
    def on_update(self):
        doc_name = self.choose_class
        doc = frappe.get_doc("Gym Class", doc_name)
        doc.no_of_bookings += 1
        doc.save()

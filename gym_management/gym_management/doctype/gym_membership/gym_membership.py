# Copyright (c) 2023, Jinso Raj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMembership(Document):

    def on_update(self):
        if self.locker != '' :
            frappe.db.set_value("Gym Locker", self.locker, "status", "Taken")  
            frappe.db.commit()
        			
    def on_update(self):
        if self.locker != '' :
            
            gym_locker_booking= frappe.get_doc({
            "doctype": "Gym Locker Booking",
            "locker_number": self.locker,
            "assigned_to": self.gym_member_name,
            "valid_upto": self.plan_expiry_date
            })

            gym_locker_booking.insert()
            frappe.db.commit()
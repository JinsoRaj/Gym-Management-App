# Copyright (c) 2023, Jinso Raj and Contributors
# See license.txt

import frappe
import unittest

class TestGymMembership(unittest.TestCase):
	def test_gym_membership(self):
		test_entry = frappe.get_doc({
			"doctype": "Gym Membership",
			"gym_member_name": "New User"
		}).insert()

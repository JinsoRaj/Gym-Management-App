# Copyright (c) 2023, Jinso Raj and Contributors
# See license.txt

import frappe
import unittest

class TestMeasurements(unittest.TestCase):
	def test_measurements(self):
		test_entry = frappe.get_doc({
			"doctype": "Measurements",
			"weight": "123"
		}).insert()
 
# Copyright (c) 2023, Jinso Raj and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data

def get_columns():
	return[
		"Class Name:Data/Gym Class:200",
		"Total no. of bookings:Int/Gym Class:200"
	]

def get_data():
	my_query = """
		SELECT
			gc.class,
			gc.no_of_bookings
		FROM
			`tabGym Class` as gc
		ORDER BY 
			gc.no_of_bookings DESC
	"""
	return frappe.db.sql(my_query)
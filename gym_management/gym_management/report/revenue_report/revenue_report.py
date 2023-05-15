# Copyright (c) 2023, Jinso Raj and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return[
		"Date:Date/Gym Invoice:200",
		"Customer:Link/Gym Member",
		"Plan Name:Data/Gym Invoice",
		"Total Amount:Currency/Gym Invoice"
	]

def get_data(filters):
	conditions = '1=1'
	if filters.get('to'):
		conditions += f" AND gi.date BETWEEN '{(filters.get('from'))}' AND '{(filters.get('to'))}'"

	my_query = f"""
		SELECT
			gi.date,
			gi.customer,
			gi.plan_name,
			gi.total_amount
		FROM
			`tabGym Invoice` as gi
		WHERE
			{conditions}	
	"""
	return frappe.db.sql(my_query)
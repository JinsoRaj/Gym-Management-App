# Copyright (c) 2023, Jinso Raj and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return[
		"Member:Link/Gym Member:200",
		"Date:Date/Measurements:200",
		"Weight in Kilograms:Float/Measurements:200",
		"Average Calorie Intake:Data/Measurements:200"
	]


def get_data(filters):
	conditions = '1=1'

	if filters.get('gym_member') :
		conditions += f" AND m.gym_member = '{filters.get('gym_member')}' "
	
	my_query = f"""
		SELECT
			m.gym_member,
			m.date,
			m.weight,
			m.daily_calorie
		FROM
			`tabMeasurements` as m
		WHERE
			{conditions}	
	"""
	return frappe.db.sql(my_query)

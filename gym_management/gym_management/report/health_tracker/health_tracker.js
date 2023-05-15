// Copyright (c) 2023, Jinso Raj and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Health Tracker"] = {
	"filters": [
		{
			"fieldname": "gym_member",
			"label": "Gym Member",
			"fieldtype": "Link",
			"options": "Gym Member",
			"width": 200
		}
	]
};

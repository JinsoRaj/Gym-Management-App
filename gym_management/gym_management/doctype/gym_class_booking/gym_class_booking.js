// Copyright (c) 2023, Jinso Raj and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Class Booking', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Gym Class Booking', 'class', (frm, cdt, cdn) => {
	let selectedRow = locals[cdt][cdn]
	selectedRow.user = frappe.session.user
	frm.refresh_field("user")
});
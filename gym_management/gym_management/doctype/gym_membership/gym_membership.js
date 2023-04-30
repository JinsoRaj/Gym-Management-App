// Copyright (c) 2023, Jinso Raj and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', 'plan_expiry_date', (frm, cdt, cdn) => {

	const today_date = new Date();
	let expiry_date_string = frm.doc.plan_expiry_date;
	let expiry_date = new Date(expiry_date_string);
 
	 var total_seconds = Math.abs(expiry_date - today_date) / 1000;  
  
	 var days_difference = Math.floor (total_seconds / (60 * 60 * 24)) + 1;  

	console.log(days_difference);
	frm.doc.total_gym_fee = days_difference * frm.doc.plan_fee
	frm.refresh_field("total_gym_fee")
	//console.log(frm);
});

frappe.ui.form.on('Gym Membership', 'cardio', (frm, cdt, cdn) => {

	let cardio_selected = frm.doc.cardio;
	//console.log(cardio_selected);
	if(cardio_selected == "No"){
		frm.doc.cardio_fee = 0
	}
	else{
		frm.doc.cardio_fee = 20
	}
	frm.refresh_field("cardio_fee")
});
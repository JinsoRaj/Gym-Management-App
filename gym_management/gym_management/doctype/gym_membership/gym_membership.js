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

// only list lockers with status of open
frappe.ui.form.on("Gym Membership", "onload", function(frm) {
    frm.set_query("locker", function() {
        return {
            "filters": {
                "status": "Free"
            }
        };
    });
});


frappe.ui.form.on('Gym Membership', {
	before_submit: frm => {
		frappe.call({
			method: 'gym_management.services.rest.create_revenue_report',
			args: {
				'customer' : frm.doc.gym_member_name,
				'plan' : frm.doc.plan_name,
				'total': frm.doc.total_amount
			},
			callback: r => {

			}
		})
	},
	cardio_fee: (frm) => {
        calculate_total(frm);
    }
})

let calculate_total = frm => {
    let plan = frm.doc.total_gym_fee,
    	cardio = frm.doc.cardio_fee,
		trainer= frm.doc.trainer_fee,
		locker=frm.doc.locker_fee
		total = plan + cardio + trainer + locker
    frm.set_value("total_amount", total);
    frm.refresh_field("total_amount");
}
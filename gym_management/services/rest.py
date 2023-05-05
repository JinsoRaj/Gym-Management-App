import frappe

@frappe.whitelist()
def create_revenue_report(customer, plan, total):
    
    gym_invoice = frappe.get_doc({
        "doctype": "Gym Invoice",
        "customer": customer,
        "plan_name": plan,
        "total_amount": total,
    })
    # add sales invoice record to database
    gym_invoice.insert().submit()
    frappe.db.commit()
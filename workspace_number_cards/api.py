import frappe

@frappe.whitelist()
def open_sales_orders_count():
    count = frappe.db.count(
        "Sales Order",
        {
            "docstatus": 0,              # draft
            "owner": frappe.session.user  # logged in user
        }
    )

    return {
        "value": count
    }


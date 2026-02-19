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
        "value": count,
        "fieldtype": "Int"
    }

@frappe.whitelist()
def open_warranty_claims():
    """
    Count of Draft Warranty Claims (docstatus=0) owned by logged-in user
    """
    count = frappe.db.count(
        "Warranty Claim",
        {"docstatus": Open, "owner": frappe.session.user}
    )
    return {"value": count, "fieldtype": "Int"}

import frappe
from frappe.utils import today

@frappe.whitelist()
def total_unpaid_revenue_today_user():
    """
    Sum of today's submitted Sales Invoices in Unpaid status
    for logged-in user.
    """

    total = frappe.db.get_value(
        "Sales Invoice",
        filters={
            "docstatus": 1,
            "status": "Unpaid",
            "owner": frappe.session.user,
            "posting_date": today()
        },
        fieldname="sum(grand_total)"
    )

    return {
        "value": total or 0,
        "fieldtype": "Currency"
    }


@frappe.whitelist()
def total_revenue_company(company=None):
    if not company:
        company = frappe.defaults.get_user_default("Company")
    total = frappe.db.get_value(
        "Sales Order",
        filters={"docstatus": 1, "company": company},
        fieldname="sum(grand_total)"
    )
    return {"value": total or 0, "fieldtype": "Float"}

@frappe.whitelist()
def submitted_sales_orders_company(company=None):
    if not company:
        company = frappe.defaults.get_user_default("Company")
    count = frappe.db.count(
        "Sales Order",
        filters={"docstatus": 1, "company": company}
    )
    return {"value": count, "fieldtype": "Int"}

@frappe.whitelist()
def open_warranty_claims_company(company=None):
    if not company:
        company = frappe.defaults.get_user_default("Company")
    count = frappe.db.count(
        "Warranty Claim",
        filters={"docstatus": 0, "company": company}
    )
    return {"value": count, "fieldtype": "Int"}



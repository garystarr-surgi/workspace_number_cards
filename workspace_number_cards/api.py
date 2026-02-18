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
        {"docstatus": 0, "owner": frappe.session.user}
    )
    return {"value": count, "fieldtype": "Int"}

@frappe.whitelist()
def total_revenue_user():
    total = frappe.db.get_value(
        "Sales Order",
        filters={"docstatus": 1, "owner": frappe.session.user},
        fieldname="sum(grand_total)"
    )
    return {"value": total or 0, "fieldtype": "Float"}

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



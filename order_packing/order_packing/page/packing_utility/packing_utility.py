import frappe

@frappe.whitelist()
def fetch_all_orders():
    orders= frappe.db.sql("""select name from `tabKitchen Utility` order by modified desc;""",as_dict=True)
    return orders
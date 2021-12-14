import frappe

@frappe.whitelist()
def fetch_all_orders():
    orders= frappe.db.sql("""select name from `tabSales Order` order by modified desc;""",as_dict=True)
    return orders
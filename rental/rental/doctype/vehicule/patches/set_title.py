import frappe

def execute():
    vehicules = frappe.db.get_all("Vehicule", pluck="name")

    for v in vehicules:
        vehicule = frappe.get_doc('Vehicule',v)
        vehicule.set_title()
        vehicule.save()

    frappe.db.commit()
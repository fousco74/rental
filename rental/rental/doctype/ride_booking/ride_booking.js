// Copyright (c) 2025, KONE Fousseni and contributors
// For license information, please see license.txt

   frappe.ui.form.on("Ride Booking", {
    rate(frm){
        console.log(cdn, cdt)
    } 
   });

   frappe.ui.form.on("Ride Booking Item",{
        distance(frm, cdt, cdn){
            const docE = frappe.get_doc(cdt,cdn)
            console.log(docE.distance)
        }
   });


 
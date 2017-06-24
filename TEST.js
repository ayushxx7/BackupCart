frappe.ui.form.on("Payment Entry", "func", function(frm) {
  frappe.call({
    method: "paperkart.paperkart.payment_client.func",
    callback: function(r) { };
  });
});







frappe.ui.form.on("Payment Entry", {
	ifsc_code: function(frm,cdt,cdn) {

	
		
	var payment_entry - frappe.model.get_doc('cdt','cdn');
		alert('test');
		frm.call({	
			method: "paperkart.paperkart.payment_client.func",
			args : {
				ifsc: payment_entry.ifsc_code,
			},

			callback: function(r)
			{
				alert('worked');
			}

		});

	}

});

frappe.ui.form.on('Payment Entry', {
	ifsc_code: function(frm,cdt,cdn) {
		
		var payment_entry = frappe.model.get_doc(cdt,cdn);
		if(payment_entry.ifsc_code)
		{
			
			frm.call({
				method:"paperkart.paperkart.payment_client.func",
				args:{
					ifsc:payment_entry.ifsc_code,
				},
				callback:function(r){
					
					var obj = JSON.parse(r.message); 					
					frappe.model.set_value(cdt,cdn,"state",obj.state);
					// frappe.model.set_value(cdt,cdn,"branch",obj.branch);
					// frappe.model.set_value(cdt,cdn,"micr",obj.micr);
					// frappe.model.set_value(cdt,cdn,"contact",obj.contact);
					// frappe.model.set_value(cdt,cdn,"state",obj.state);
					// frappe.model.set_value(cdt,cdn,"bank_name",obj.bank_name);
				}
			});
		}
		else
		{
			frappe.model.set_value(cdt,cdn,"bank_branch",null);
		}
		
	}
});


































// cur_frm.set_query("ifsc_code", function(doc, cdt, cdn) {
// 	var d = locals[cdt][cdn];
// 	if(d.micr){
// 	return {
// 		filters: [
// 			["micr", "=", d.micr]
// 		]
// 	}
// 	}
// });


// frappe.ui.form.on('Payment Entry',{
// 	micr: function(frm,cdt,cdn) {

// 		var payment_entry = frappe.model.get_doc(cdt,cdn);
// 		if(payment_entry.ifsc_code)
// 		{

// 			frm.call({
// 				method:"newapp.newapp.payment_entry_2.set_branch",
// 				args:{
// 					ifsc:payment_entry.ifsc_code,
// 				},
// 				callback:function(r){

// 					var obj = JSON.parse(r.message); 					frappe.model.set_value(cdt,cdn,"city",obj.city);
// frappe.model.set_value(cdt,cdn,"branch",obj.branch);
// frappe.model.set_value(cdt,cdn,"micr",obj.micr);
// frappe.model.set_value(cdt,cdn,"bank_contact",obj.contact);
// frappe.model.set_value(cdt,cdn,"state",obj.state);
// frappe.model.set_value(cdt,cdn,"bank_name",obj.bank_name);
// 				}
// 			});
// 		}
// 		else
// 		{
// 			frappe.model.set_value(cdt,cdn,"bank_branch",null);
// 		}

// 	}
// });

// frappe.ui.form.on('Payment Entry', {
// 	ifsc_code: function(frm,cdt,cdn) {

// 		var payment_entry = frappe.model.get_doc(cdt,cdn);
// 		if(payment_entry.ifsc_code)
// 		{

// 			frm.call({
// 				method:"newapp.newapp.payment_entry_2.set_branch",
// 				args:{
// 					ifsc:payment_entry.ifsc_code,
// 				},
// 				callback:function(r){

// 					var obj = JSON.parse(r.message); 					frappe.model.set_value(cdt,cdn,"city",obj.city);
// frappe.model.set_value(cdt,cdn,"branch",obj.branch);
// frappe.model.set_value(cdt,cdn,"micr",obj.micr);
// frappe.model.set_value(cdt,cdn,"contact",obj.contact);
// frappe.model.set_value(cdt,cdn,"state",obj.state);
// frappe.model.set_value(cdt,cdn,"bank_name",obj.bank_name);
// 				}
// 			});
// 		}
// 		else
// 		{
// 			frappe.model.set_value(cdt,cdn,"bank_branch",null);
// 		}

// 	}
// });

// method: "paperkart.paperkart.payment_client.func",
// 		args : {
// 			ifsc: payment_entry.ifsc_code,
// 	       	},

// 		callback: function(r)
// 		{
// 			alert('worked');
// 		}



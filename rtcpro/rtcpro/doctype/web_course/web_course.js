// Copyright (c) 2022, osama and contributors
// For license information, please see license.txt

frappe.ui.form.on('Web Course', {
	'refresh': function (frm) {
		let d = new frappe.ui.Dialog({
			title: 'Enter details',
			fields: [
				{
					label: 'Web Course',
					fieldname: 'web_course',
					fieldtype: 'Link',
					options: 'Web Course',
					read_only: true,
					default: frm.doc.name
				},
				{
					label: 'Rate',
					fieldname: 'rate',
					fieldtype: 'Rating'
				},
				{
					label: 'Comment',
					fieldname: 'comment',
					fieldtype: 'Text'
				}
			],
			primary_action_label: 'Submit',
			primary_action(values) {
				console.log(values.web_course)
				frappe.db.insert({
					"doctype": "Rating",
					"course": values.web_course,
					"rate": values.rate,
					"review_content": values.review_content,
				}).then(function (v) {
					frappe.msgprint(_('Your review Has Submitted'));
				});
				d.hide();
			}
		});
		frm.add_custom_button("Review", function () {
			// write your code
			d.show();
		}).addClass("btn-primary");;
	}
});

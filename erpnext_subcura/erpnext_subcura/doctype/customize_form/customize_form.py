# Copyright (c) 2025, subcura and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CustomizeForm(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.core.doctype.doctype_action.doctype_action import DocTypeAction
		from frappe.core.doctype.doctype_link.doctype_link import DocTypeLink
		from frappe.core.doctype.doctype_state.doctype_state import DocTypeState
		from frappe.custom.doctype.customize_form_field.customize_form_field import CustomizeFormField
		from frappe.types import DF

		actions: DF.Table[DocTypeAction]
		allow_auto_repeat: DF.Check
		allow_copy: DF.Check
		allow_import: DF.Check
		autoname: DF.Data | None
		default_email_template: DF.Link | None
		default_print_format: DF.Link | None
		default_view: DF.Literal[None]
		doc_type: DF.Link | None
		editable_grid: DF.Check
		email_append_to: DF.Check
		fields: DF.Table[CustomizeFormField]
		force_re_route_to_default_view: DF.Check
		image_field: DF.Data | None
		is_calendar_and_gantt: DF.Check
		istable: DF.Check
		label: DF.Data | None
		link_filters: DF.JSON | None
		links: DF.Table[DocTypeLink]
		make_attachments_public: DF.Check
		max_attachments: DF.Int
		naming_rule: DF.Literal["", "Set by user", "By fieldname", "By \"Naming Series\" field", "Expression", "Expression (old style)", "Random", "By script"]
		queue_in_background: DF.Check
		quick_entry: DF.Check
		search_fields: DF.Data | None
		sender_field: DF.Data | None
		sender_name_field: DF.Data | None
		show_preview_popup: DF.Check
		show_title_field_in_link: DF.Check
		sort_field: DF.Literal[None]
		sort_order: DF.Literal["ASC", "DESC"]
		states: DF.Table[DocTypeState]
		subject_field: DF.Data | None
		title_field: DF.Data | None
		track_changes: DF.Check
		track_views: DF.Check
		translated_doctype: DF.Check
	# end: auto-generated types
	pass

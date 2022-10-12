from . import __version__ as app_version

app_name = "rtcpro"
app_title = "Rtcpro"
app_publisher = "osama"
app_description = "custom style for rtcpro website"
app_email = "osama@aoai.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rtcpro/css/rtcpro.css"
# app_include_js = "/assets/rtcpro/js/rtcpro.js"

# include js, css files in header of web template
web_include_css = [
    "/assets/rtcpro/css/fontawesome.css",
    "/assets/rtcpro/libs/@fancyapps/fancybox/dist/jquery.fancybox.min.css",
    "/assets/rtcpro/libs/aos/dist/aos.css",
    "/assets/rtcpro/libs/choices.js/public/assets/styles/choices.min.css",
    "/assets/rtcpro/libs/flickity-fade/flickity-fade.css",
    "/assets/rtcpro/libs/flickity/dist/flickity.min.css",
    "/assets/rtcpro/libs/highlightjs/styles/vs2015.css",
    "/assets/rtcpro/libs/jarallax/dist/jarallax.css",
    "/assets/rtcpro/libs/quill/dist/quill.core.css",
    "/assets/rtcpro/css/custom.css",
    "/assets/rtcpro/css/theme.min.css",
]

web_include_js = [
    # "/assets/rtcpro/libs/jquery/dist/jquery.min.js", #couse error in webform
    "/assets/rtcpro/libs/bootstrap/dist/js/bootstrap.bundle.min.js",
    "/assets/rtcpro/libs/@fancyapps/fancybox/dist/jquery.fancybox.min.js",
    "/assets/rtcpro/libs/aos/dist/aos.js",
    "/assets/rtcpro/libs/choices.js/public/assets/scripts/choices.min.js",
    "/assets/rtcpro/libs/countup.js/dist/countUp.min.js",
    "/assets/rtcpro/libs/dropzone/dist/min/dropzone.min.js",
    "/assets/rtcpro/libs/flickity/dist/flickity.pkgd.min.js",
    "/assets/rtcpro/libs/flickity-fade/flickity-fade.js",
    "/assets/rtcpro/libs/highlightjs/highlight.pack.min.js",
    "/assets/rtcpro/libs/imagesloaded/imagesloaded.pkgd.min.js",
    "/assets/rtcpro/libs/isotope-layout/dist/isotope.pkgd.min.js",
    "/assets/rtcpro/libs/jarallax/dist/jarallax.min.js",
    "/assets/rtcpro/libs/jarallax/dist/jarallax-video.min.js",
    "/assets/rtcpro/libs/jarallax/dist/jarallax-element.min.js",
    "/assets/rtcpro/libs/parallax-js/dist/parallax.min.js",
    "/assets/rtcpro/libs/quill/dist/quill.min.js",
    "/assets/rtcpro/libs/smooth-scroll/dist/smooth-scroll.min.js",
    "/assets/rtcpro/libs/typed.js/lib/typed.min.js",
    "/assets/rtcpro/js/theme.min.js",
]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rtcpro/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "rtcpro.utils.jinja_methods",
#	"filters": "rtcpro.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rtcpro.install.before_install"
# after_install = "rtcpro.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rtcpro.uninstall.before_uninstall"
# after_uninstall = "rtcpro.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rtcpro.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"rtcpro.tasks.all"
#	],
#	"daily": [
#		"rtcpro.tasks.daily"
#	],
#	"hourly": [
#		"rtcpro.tasks.hourly"
#	],
#	"weekly": [
#		"rtcpro.tasks.weekly"
#	],
#	"monthly": [
#		"rtcpro.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "rtcpro.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "rtcpro.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "rtcpro.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"rtcpro.auth.validate"
# ]

fixtures = [
    # export all records from the Category table
    "Program",
    "Web Page",
    "Website Theme",
]

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import Order


class OrderAdmin(ModelAdmin):
    model = Order
    base_url_path = "orders"
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    menu_icon = "pilcrow"
    menu_label = "Orders"
    list_display = ("tracking_id", "status", "created_at", "updated_at")
    list_filter = ("status", "mode", "type")
    search_fields = ("tracking_id", "shipping_from", "shipping_to")


modeladmin_register(OrderAdmin)

from frappe import _


def get_data():
    return [
        {
            "label": _("Stock Transactions"),
            "items": [
                {
                    "type": "page",
                    "name": "packing-slip",
                    "label": _("Packing Slip")
                }
            ]
        },

    ]

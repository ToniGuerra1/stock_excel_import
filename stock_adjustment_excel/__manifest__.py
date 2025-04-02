
{
    "name": "Importar Stock Quant Wizard",
    "version": "1.0",
    "category": "Inventory",
    "author": "Toni Guerra",
    "website": "",
    "depends": [
        "stock",  # Necesario para trabajar con stock.quant y stock.location
    ],
    "data": [
        # Aquí referenciamos el archivo con la vista del wizard y la acción
        "views/import_stock_count_wizard_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": True,
    'license': 'OPL-1',
    'price': 19.90,
    'currency': 'EUR',
}

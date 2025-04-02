# 📦 Import Stock Quant from Excel (Odoo Module)

Actualiza el stock de tus productos directamente desde un archivo Excel, sin complicaciones. Este módulo te permite cargar cantidades inventariadas y aplicar los ajustes con solo unos clics.

---

## ⚙️ ¿Qué hace este módulo?

Este asistente (wizard) permite:

- Exportar productos a Excel con sus cantidades actuales.
- Cargar un Excel con nuevos valores de stock.
- Ajustar inventario automáticamente con `inventory_quantity` y `action_apply_inventory`.

---

## 📂 Estructura del archivo Excel esperada

| DEFAULT_CODE | NAME | QUANTITY |
|--------------|------|----------|
| P001         | Producto A | 15.0 |
| P002         | Producto B | 23.5 |

- La columna **DEFAULT_CODE** debe contener el código interno del producto.
- La columna **QUANTITY** representa la nueva cantidad contada del producto.

---

## 🔥 Características

- ✅ Compatible con archivos `.xlsx`
- ✅ Interfaz simple e intuitiva
- ✅ Selección de ubicación (`stock.location`) directamente desde el asistente
- ✅ Registro de logs y errores en Odoo para trazabilidad
- ✅ Uso de métodos estándar de Odoo: `inventory_quantity` y `action_apply_inventory`

---

## 💼 Casos de uso

- Cargar inventario de forma masiva desde un conteo físico.
- Reajustar stock después de auditorías.
- Importación rápida de datos desde sistemas externos o Google Sheets exportado a Excel.

---

## 🛠️ Instalación

1. Copia la carpeta del módulo en tu carpeta de addons personalizados.
2. Reinicia el servidor de Odoo.
3. Actualiza la lista de aplicaciones.
4. Instala el módulo "Import Stock Quant from Excel".

---

## 🧪 Recomendaciones

- Asegúrate de tener la librería `openpyxl` instalada en tu entorno Python.
- El archivo debe ser `.xlsx` (no se acepta `.xls`).
- El código de producto (`default_code`) debe estar correctamente asignado en Odoo.

---

## 📄 Licencia

Este módulo está licenciado bajo **OPL-1** (Odoo Proprietary License v1.0).

- Uso permitido en **una única base de datos**.
- Prohibida su redistribución o modificación sin permiso.
- El módulo se ofrece **“tal cual”**, sin garantía de funcionamiento.

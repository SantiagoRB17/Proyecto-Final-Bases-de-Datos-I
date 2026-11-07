from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


# Genera el PDF de un reporte a partir de lo que ya muestra la ventana:
# el título, los filtros elegidos y la tabla (encabezados y filas ya en texto).
class ReportePdfService:

    def exportar(self, ruta, titulo, filtros, encabezados, filas, usuario):
        estilos = getSampleStyleSheet()
        documento = SimpleDocTemplate(ruta, pagesize=landscape(A4), title=titulo,
                                      leftMargin=1.5 * cm, rightMargin=1.5 * cm,
                                      topMargin=1.5 * cm, bottomMargin=1.5 * cm)

        elementos = [Paragraph(titulo, estilos["Title"])]
        for filtro in filtros:
            elementos.append(Paragraph(filtro, estilos["Normal"]))
        generado = datetime.now().strftime("%d/%m/%Y %H:%M")
        elementos.append(Paragraph(f"Generado por {usuario.UsrNombres} {usuario.UsrApellidos} el {generado}",
                                   estilos["Normal"]))
        elementos.append(Spacer(1, 0.5 * cm))

        if filas:
            # Cada celda es un Paragraph para que el texto largo salte de línea.
            estilo_celda = estilos["BodyText"]
            datos = [[Paragraph(f"<b>{self._texto(e)}</b>", estilo_celda) for e in encabezados]]
            datos += [[Paragraph(self._texto(celda), estilo_celda) for celda in fila] for fila in filas]
            tabla = Table(datos, repeatRows=1)
            tabla.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            elementos.append(tabla)
        else:
            elementos.append(Paragraph("No hay datos para los filtros elegidos.", estilos["Normal"]))
        elementos.append(Spacer(1, 0.3 * cm))
        elementos.append(Paragraph(f"Registros: {len(filas)}", estilos["Normal"]))

        documento.build(elementos)

    # Paragraph interpreta etiquetas como <b>: los símbolos del texto se escapan.
    def _texto(self, valor):
        return str(valor).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

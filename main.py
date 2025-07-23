import webview
import os

# Todo: Allow export button
# Todo: Allow to save preferences
# Todo: Add Ctrl + S and Ctrl + D shortcut si se puede (puede ser poniendo un codigo que se ejecute al iniciar el editor dentro de svgedit-config-iife.js)
# Todo: Fix shortcut for send (back, forward, up, down)
# Todo: With a clic in the background changue to the select tool automaticaly

class SVGEditAPI:
    def save_as(self, contentsave , default_filename=""):
        """Guarda el archivo con un nuevo nombre y ubicación"""
        if not contentsave:
            return {"success": False, "error": "No hay contenido para guardar"}

        try:
            # Obtener directorio por defecto (directorio actual del archivo o directorio de trabajo)
            default_dir = os.getcwd()

            # Crear diálogo para guardar archivo
            result = webview.windows[0].create_file_dialog(
                webview.SAVE_DIALOG,
                directory=default_dir,
                save_filename=default_filename,
                file_types=("Archivos SVG (*.svg)", "Todos los archivos (*.*)"),
            )

            if result:
                # Asegurar que tenga extensión .svg si no la tiene añadirla
                save_path = result
                if not save_path.lower().endswith(".svg"):
                    save_path += ".svg"

                # Guardar el archivo
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(contentsave)

                return {
                    "success": True,
                    "message": f"Archivo guardado como: {save_path}",
                    "path": save_path,
                }
            else:
                return {"success": False, "error": "Guardado cancelado"}

        except Exception as e:
            return {"success": False, "error": str(e)}


if __name__ == "__main__":
    # Ruta al archivo HTML local
    html_path = os.path.abspath("html/editor/svg-editor.html")

    # Crear ventana
    window = webview.create_window(
        "SVG Editor", f"file://{html_path}", width=1200, height=800, js_api=SVGEditAPI()
    )

    webview.start(debug=True)

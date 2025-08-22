import webview
import base64
import os

class SVGEditAPI:
    def __init__(self, final_svg):
        self.final_svg = final_svg
    
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
                save_path = result[0]
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
    
    def save_file(self, base64_data, ext):
        # Decodificar el archivo
        default_dir = os.getcwd()

        # Crear diálogo para guardar archivo
        result = webview.windows[0].create_file_dialog(
            webview.SAVE_DIALOG,
            directory=default_dir,
            file_types=(f"Archivos {ext} (*.{ext})", "Todos los archivos (*.*)"),
        )

        if result:
            # Asegurar que tenga extensión, si no la tiene añadirla
            save_path = result[0]
            if not save_path.lower().endswith("." + ext):
                save_path += "." + ext
                
            data = base64.b64decode(base64_data)
            
            with open(save_path, "wb") as f:
                f.write(data)
            print(f"Archivo guardado en {save_path}")
            return save_path
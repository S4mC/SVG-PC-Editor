import webview
import base64
import os

class SVGEditAPI:
    def __init__(self, final_svg):
        self.final_svg = final_svg
    
    def save_as(self, contentsave , default_filename=""):
        """Save the file with a new name and location"""
        
        if not contentsave:
            return {"success": False, "error": "No content to save"}

        try:
            # Get default directory (current file directory or working directory)
            default_dir = os.getcwd()

            # Create save file dialog
            result = webview.windows[0].create_file_dialog(
                webview.SAVE_DIALOG,
                directory=default_dir,
                save_filename=default_filename,
                file_types=("Archivos SVG (*.svg)", "Todos los archivos (*.*)"),
            )

            if result:
                # Make sure it has .svg extension, add it if it doesn't
                save_path = result[0]
                if not save_path.lower().endswith(".svg"):
                    save_path += ".svg"

                # Save the file
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(contentsave)

                return {
                    "success": True,
                    "message": f"File saved as: {save_path}",
                    "path": save_path,
                }
            else:
                return {"success": False, "error": "Save cancelled"}

        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def save_file(self, base64_data, ext):
        # Decode the file
        default_dir = os.getcwd()

        # Create save file dialog
        result = webview.windows[0].create_file_dialog(
            webview.SAVE_DIALOG,
            directory=default_dir,
            file_types=(f"{ext} Files (*.{ext})", "All Files (*.*)"),
        )

        if result:
            # Make sure it has the extension, add it if it doesn't
            save_path = result[0]
            if not save_path.lower().endswith("." + ext):
                save_path += "." + ext
                
            data = base64.b64decode(base64_data)
            
            with open(save_path, "wb") as f:
                f.write(data)
            print(f"File saved at {save_path}")
            return save_path
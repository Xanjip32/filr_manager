import shutil
from pathlib import Path

# FileManager class for organizing files
class FileManager:
    def __init__(self, source: str, destination: str):
        self.source = Path(source)
        self.destination = Path(destination)

    def segregate(self, file_extensions: set, subfolder: str):
        target = self.destination / subfolder
        target.mkdir(parents=True, exist_ok=True)
        for item in self.source.iterdir():
            if item.suffix.lower() in file_extensions:
                shutil.move(str(item), str(target / item.name))
                print(f"Moved: {item.name} --> {target}")

    def segregate_video(self):
        video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"}
        self.segregate(video_extensions, "Video")

    def segregate_audio(self):
        audio_extensions = {".mp3", ".wav", ".aac", ".ogg", ".flac"}
        self.segregate(audio_extensions, "Audio")

    def segregate_excel(self):
        excel_extensions = {".xls", ".xlsx", ".xlsm", ".csv"}
        self.segregate(excel_extensions, "Excel")

    def segregate_picture(self):
        picture_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
        self.segregate(picture_extensions, "Picture")

    def segregate_word(self):
        word_extensions = {".doc", ".docx", ".odt"}
        self.segregate(word_extensions, "Word")

    def segregate_software(self):
        software_extensions = {".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"}
        self.segregate(software_extensions, "Software")

    def segregate_pdf(self):
        pdf_extensions = {".pdf"}
        self.segregate(pdf_extensions, "PDF")

if __name__ == "__main__":
    # Define source (Downloads) and destination (OrganizedFiles inside Downloads)
    downloads_path = Path.home() / "Downloads"
    destination_path = downloads_path / "OrganizedFiles"
    
    manager = FileManager(str(downloads_path), str(destination_path))
    
    # Manually call segregation methods
    manager.segregate_video()
    manager.segregate_audio()
    manager.segregate_excel()
    manager.segregate_picture()
    manager.segregate_word()
    manager.segregate_software()
    manager.segregate_pdf()
    
    print("File organization complete.")

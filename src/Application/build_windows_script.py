import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'Chess.py',
    '--windowed',
    '--noconfirm',
    '--clean',    
    '--onedir',
    '--ascii',
    f'--icon={os.path.join("assets", "imgs", "icons", "game.ico")}',
    f'--add-data={os.path.join("assets")};assets',
    f'--distpath={os.path.join("dist")}',
    f'--workpath={os.path.join("build")}',
])
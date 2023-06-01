import PyInstaller.__main__
import os

PRJ_FLDR=os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    os.path.join(PRJ_FLDR, "Chess.py"),
    '--windowed',
    '--noconfirm',
    '--clean',    
    '--onedir',
    '--ascii',
    f'--icon={os.path.join(PRJ_FLDR, "assets", "imgs", "icons", "game.ico")}',
    f'--add-data={os.path.join(PRJ_FLDR, "assets")};assets',
    f'--distpath={os.path.join(PRJ_FLDR, "dist")}',
    f'--workpath={os.path.join(PRJ_FLDR, "build")}',
])
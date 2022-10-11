# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['maintext.py'],
             pathex=['D:\\project_file\\综合项目\\读取图片并识别边界转为轨迹点'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='maintext',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , version='file_version_info.txt', icon='D:\\project_file\\综合项目\\读取图片并识别边界转为轨迹点\\tubiao.ico')

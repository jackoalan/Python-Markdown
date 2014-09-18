import zipfile
zf = zipfile.PyZipFile('markdown.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
zf.writepy('markdown')
zf.close()
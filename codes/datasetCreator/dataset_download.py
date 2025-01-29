

try:
    import magic
    import dataset_tools as dtools
    print("python-magic is installed and working correctly.")
except ImportError as e:
    print(f"Error: {e}")

quit(1)
dtools.download(dataset='BDD100K: Images 100K', dst_dir='~/dataset-ninja/')
dtools.download(dataset='Mapillary Vistas', dst_dir='~/dataset-ninja/')
dtools.download(dataset='Tsinghua Tencent 2021', dst_dir='~/dataset-ninja/')
dtools.download(dataset='BSTLD', dst_dir='~/dataset-ninja/')



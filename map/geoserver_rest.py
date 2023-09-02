from geoserver.catalog import Catalog, FailedRequestError


def tiff_to_geoserver():
    cat = Catalog(service_url=r'http://localhost:8080/geoserver/rest/', username='admin', password='geoserver')
    testing_workspace = cat.get_workspace("testing_workspace")
    try:
        store = cat.get_store(workspace=testing_workspace, name='fortest')
    except FailedRequestError:
        path = '../media/uploaded_tiffs/Landsat_ETM_2001-08-26_multispectral.tif'
        cat.create_coveragestore(name="fortest", workspace=testing_workspace, overwrite=True, data=path)


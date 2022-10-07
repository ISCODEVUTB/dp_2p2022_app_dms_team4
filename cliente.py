from DocumentAbstracbFactory import DocumentAbstracbFactory

def Cliente(factory: DocumentAbstracbFactory, **kwargs):

    factory_product = DocumentAbstracbFactory.crearDocumento(**kwargs)

    return factory_product
''' Example plugin to extend functionality '''
from spydrnet.ir import Definition as DefinitionBase

class Definition(DefinitionBase):
    ''' Extending definition class '''

    def merge_port(self, port1, port2):
        print("Merging ports %s and %s" % (port1, port2))

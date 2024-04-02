import os
from exa_py import Exa

class ExaSearchToolset():
    def _exa(self):
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
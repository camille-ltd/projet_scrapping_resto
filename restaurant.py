from pydantic import BaseModel
from typing import List, Optional


class Restaurant(BaseModel):
    enseigne: str
    adresse: str
    specialite: List[str]
    fourchette_de_prix: str
    note_globale: str
    nombre_avis: str
    top_avis: List[str]

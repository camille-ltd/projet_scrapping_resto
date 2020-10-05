from pydantic import BaseModel
from typing import List, Optional


class Restaurant(BaseModel):
    enseigne: str
    adresse: str
    specialite: str
    fourchette_de_prix: int
    note_globale: float
    nombre_avis: int
    top_avis: str

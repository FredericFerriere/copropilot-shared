from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class Copropriete(BaseModel):
    id: int | None = None
    nom: str
    adresse: str

    model_config = {"from_attributes": True}

class Exercice(BaseModel):
    id: int | None = None
    copropriete_id: int
    date_debut: date
    date_fin: date

    model_config = {"from_attributes": True}

class EtatFinancier(BaseModel):
    id: int | None = None
    exercice_id: int
    numero_compte: int
    montant_cents: int

    model_config = {"from_attributes": True}
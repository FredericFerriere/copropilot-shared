import enum
from typing import List

from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class typeAssemblee(str, enum.Enum):
    ORDINAIRE = "ordinaire"
    EXTRAORDINAIRE = "extraordinaire"
    MIXTE = "mixte"

class typeContenu(str, enum.Enum):
    ORDRE_DU_JOUR = "ordre_du_jour"
    ETAT_FINANCIER = "etat_financier"

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

class LigneEtatFinancier(BaseModel):
    id: int | None = None
    etat_financier_id: int
    numero_compte: str
    montant_cents: int | str

    model_config = {"from_attributes": True}

class EtatFinancier(BaseModel):
    id: int | None = None
    exercice_id: int
    lignes_etat_financier: List[LigneEtatFinancier] = []
    model_config = {"from_attributes": True}

class AssembleeGenerale(BaseModel):
    id: int | None = None
    date: date
    copropriete_id: int
    type: typeAssemblee

    model_config = {"from_attributes": True}

class Resolution(BaseModel):
    id: int | None = None
    assemblee_id: int
    numero: str
    libelle: str
    regle_majorite: str
    detail_resolution: str

    model_config = {"from_attributes": True}

class OrdreDuJour(BaseModel):
    id: int | None = None
    assemblee_id: int
    resolutions: List[Resolution] = []

    model_config = {"from_attributes": True}

class ContenuDocument(BaseModel):
    id: int | None = None
    document_id: int
    type_contenu: typeContenu
    contenu_id: int

    model_config = {"from_attributes": True}

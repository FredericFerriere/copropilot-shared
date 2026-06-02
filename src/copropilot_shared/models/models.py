import enum
from typing import Optional
import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String


class typeDocument(str, enum.Enum):
    CONVOCATION = "convocation AG"
    PROCES_VERBAL = "procès-verbal AG"


class typeAssemblee(str, enum.Enum):
    ORDINAIRE = "ordinaire"
    EXTRAORDINAIRE = "extraordinaire"
    MIXTE = "mixte"


class typeContenu(str, enum.Enum):
    ORDRE_DU_JOUR = "ordre_du_jour"
    ETAT_FINANCIER = "etat_financier"


class Copropriete(SQLModel, table=True):
    __tablename__ = "coproprietes"
    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    adresse: str


class AssembleeGenerale(SQLModel, table=True):
    __tablename__ = "assemblees_generales"
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date
    copropriete_id: int = Field(default=None, foreign_key="coproprietes.id")
    type: str = Field(default=None, sa_column=Column(String))


class OrdreDuJour(SQLModel, table=True):
    __tablename__ = "ordres_du_jour"
    id: Optional[int] = Field(default=None, primary_key=True)
    assemblee_id: int = Field(default=None, foreign_key="assemblees_generales.id")


class Resolution(SQLModel, table=True):
    __tablename__ = "resolutions"
    id: Optional[int] = Field(default=None, primary_key=True)
    ordre_du_jour_id: int = Field(foreign_key="ordres_du_jour.id")
    numero: str
    libelle: str
    regle_majorite: str
    detail_resolution: str


class Exercice(SQLModel, table=True):
    __tablename__ = "exercices"
    id: Optional[int] = Field(default=None, primary_key=True)
    copropriete_id: int = Field(default=None, foreign_key="coproprietes.id")
    date_debut: datetime.date
    date_fin: datetime.date


class EtatFinancier(SQLModel, table=True):
    __tablename__ = "etats_financiers"
    id: Optional[int] = Field(default=None, primary_key=True)
    exercice_id: int = Field(default=None, foreign_key="exercices.id")


class LigneEtatFinancier(SQLModel, table=True):
    __tablename__ = "lignes_etats_financiers"
    id: Optional[int] = Field(default=None, primary_key=True)
    etat_financier_id: int = Field(foreign_key="etats_financiers.id")
    numero_compte: str
    montant_cents: int


class ContenuDocument(SQLModel, table=True):
    __tablename__ = "contenus_documents"
    id: Optional[int] = Field(default=None, primary_key=True)
    document_id: int
    type_contenu: str = Field(default=None, sa_column=Column(String))
    contenu_id: int

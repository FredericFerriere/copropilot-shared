import enum
from typing import Optional
import datetime
import uuid

from sqlmodel import SQLModel, Field, Relationship


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
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nom: str
    adresse: str


class AssembleeGenerale(SQLModel, table=True):
    __tablename__ = "assemblees_generales"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    date: datetime.date
    copropriete_id: uuid.UUID = Field(default=None, foreign_key="coproprietes.id")
    type: str


class OrdreDuJour(SQLModel, table=True):
    __tablename__ = "ordres_du_jour"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    assemblee_id: uuid.UUID = Field(default=None, foreign_key="assemblees_generales.id")


class Resolution(SQLModel, table=True):
    __tablename__ = "resolutions"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    odj_id: uuid.UUID = Field(foreign_key="ordres_du_jour.id")
    numero: str
    libelle: str
    regle_majorite: str
    detail_resolution: str


class Exercice(SQLModel, table=True):
    __tablename__ = "exercices"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    copropriete_id: uuid.UUID = Field(default=None, foreign_key="coproprietes.id")
    date_debut: Optional[datetime.date] = None
    date_fin: datetime.date


class EtatFinancier(SQLModel, table=True):
    __tablename__ = "etats_financiers"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    exercice_id: uuid.UUID = Field(default=None, foreign_key="exercices.id")


class LigneEtatFinancier(SQLModel, table=True):
    __tablename__ = "lignes_etats_financiers"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    ef_id: uuid.UUID = Field(foreign_key="etats_financiers.id")
    numero_compte: str
    montant_cents: int


class CompteGestionGeneral(SQLModel, table=True):
    __tablename__ = "comptes_gestion_general"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    exercice_id: uuid.UUID = Field(default=None, foreign_key="exercices.id")


class LigneCompteGestionGeneral(SQLModel, table=True):
    __tablename__ = "lignes_comptes_gestion_general"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    cgg_id: uuid.UUID = Field(foreign_key="comptes_gestion_general.id")
    numero_compte: str
    montant_cents: int


class CompteGestionOperationsCourantes(SQLModel, table=True):
    __tablename__ = "comptes_gestion_operations_courantes"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    exercice_id: uuid.UUID = Field(default=None, foreign_key="exercices.id")


class LigneCompteGestionOperationsCourantes(SQLModel, table=True):
    __tablename__ = "lignes_comptes_gestion_operations_courantes"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    cgoc_id: uuid.UUID = Field(foreign_key="comptes_gestion_operations_courantes.id")
    position: int
    numero_compte: str
    montant_cents: int
    est_sous_total: bool = False


class AgregationLigneCompteGestionOperationsCourantes(SQLModel, table=True):
    __tablename__ = "agregations_lignes_comptes_gestion_operations_courantes"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    parent_id: uuid.UUID = Field(foreign_key="lignes_comptes_gestion_operations_courantes.id")
    feuille_id: uuid.UUID = Field(foreign_key="lignes_comptes_gestion_operations_courantes.id")
    profondeur: int


class CompteGestionTravaux(SQLModel, table=True):
    __tablename__ = "comptes_gestion_travaux"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    exercice_id: uuid.UUID = Field(default=None, foreign_key="exercices.id")


class LigneCompteGestionTravaux(SQLModel, table=True):
    __tablename__ = "lignes_comptes_gestion_travaux"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    cgt_id: uuid.UUID = Field(foreign_key="comptes_gestion_travaux.id")
    position: int
    libelle: str
    depenses_votees_n: int
    depenses_realisees_n: int
    provisions_appelees_n: int
    est_sous_total: bool = False


class EtatSoldeCoproprietaire(SQLModel, table=True):
    __tablename__ = "etats_soldes_coproprietaires"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    exercice_id: uuid.UUID = Field(default=None, foreign_key="exercices.id")


class LigneEtatSoldeCoproprietaire(SQLModel, table=True):
    __tablename__ = "lignes_etats_soldes_coproprietaires"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    esc_id: uuid.UUID = Field(foreign_key="etats_soldes_coproprietaires.id")
    nom: str
    solde_debiteur_debut: int
    solde_crediteur_debut: int
    debit: int
    credit: int
    solde_fin_exercice: int
    solde_charges: int
    solde_debiteur_approbation: int
    solde_crediteur_approbation: int
            

class AgregationLigneCompteGestionTravaux(SQLModel, table=True):
    __tablename__ = "agregations_lignes_comptes_gestion_travaux"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    parent_id: uuid.UUID = Field(foreign_key="lignes_comptes_gestion_travaux.id")
    feuille_id: uuid.UUID = Field(foreign_key="lignes_comptes_gestion_travaux.id")
    profondeur: int


class ReleveDepenses(SQLModel, table=True):
    __tablename__ = "releves_depenses"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    exercice_id: uuid.UUID = Field(default=None, foreign_key="exercices.id")


class LigneReleveDepenses(SQLModel, table=True):
    __tablename__ = "lignes_releves_depenses"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    rd_id: uuid.UUID = Field(foreign_key="releves_depenses.id")
    position: int
    categorie: str
    date_paiement: datetime.date
    descriptif_detaille: str
    montant: int
    tva: int
    recuperable: int
    deductible: int


class ContenuDocument(SQLModel, table=True):
    __tablename__ = "contenus_documents"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    document_id: uuid.UUID
    type_contenu: str
    contenu_id: uuid.UUID


class WaitlistEntry(SQLModel, table=True):
    __tablename__ = "waitlist_entries"
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=100)
    email: str = Field(unique=True, index=True)
    consent: bool = Field(default=False)
    created_at: Optional[datetime.datetime] = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    first_name: str
    hashed_password: str
    created_at: Optional[datetime.datetime] = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))


class Document(SQLModel, table=True):
    __tablename__ = "documents"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    filename: str
    file_path: str
    category: str = Field(index=True)
    uploaded_by: Optional[uuid.UUID] = Field(default=None, foreign_key="users.id", index=True)
    uploaded_at: Optional[datetime.datetime] = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))
    size: int
    description: Optional[str] = None
    processing_status: str = Field(default="pending")

    user: Optional[User] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Document.uploaded_by]", "lazy": "joined"}
    )

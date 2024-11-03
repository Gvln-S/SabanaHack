from dataclasses import dataclass, field
from typing import List

@dataclass
class NoduleConfig:
    """Configuración de palabras clave para la detección de nódulos"""
    STATES: List[str] = field(default_factory=lambda: ['nodulo', 'masa'])
    NEGATION_BEFORE: List[str] = field(default_factory=lambda: ['no hay', 'no se eviden', 'no se observan'])
    CONFIRMATION_BEFORE: List[str] = field(default_factory=lambda: ['si hay', 'hay otro', 'si se eviden', 'observo'])
    CONFIRMATION_AFTER: List[str] = field(default_factory=lambda: [
        'cordenada', 'calcificado', 
        *[f'de {i}mm' for i in range(1, 11)]
    ])
    MORPHOLOGY: List[str] = field(default_factory=lambda: ['ovalado', 'ovalada', 'irregular', 'redondo'])
    MARGIN: List[str] = field(default_factory=lambda: [
        'circusnscritos', 'microlobulados', 'indistintos', 'onscurecidos', 'espiculados'
    ])
    DENSITY: List[str] = field(default_factory=lambda: ['grasa', 'hipodenso', 'isodenso', 'hiperdenso'])
    MICRO_CAL: List[str] = field(default_factory=lambda: ['microcal'])
    BENIGN: List[str] = field(default_factory=lambda: [
        'cuatanea', 'vascular', 'pop corn', 'gruesa', 'leño', 'vara',
        'redondas', 'puntiformes', 'anulares', 'distroficas', 'suturas'
    ])
    BIRAD: List[str] = field(default_factory=lambda: ['birad', 'bi-rad', 'birads', 'bi-rads'])

@dataclass
class Nodule:
    """Clase para almacenar información sobre un nódulo"""
    contains_nodule: str = "Unknown"
    morphology: str = "Unknown"
    margin: str = "Unknown"
    density: str = "Unknown"
    micro_cal: str = "Unknown"
    benign: str = "Unknown"
    birad: str = "Unknown"

    def __str__(self) -> str:
        return (f"Nodule: {self.contains_nodule} "
                f"Morphology: {self.morphology} "
                f"Margin: {self.margin} "
                f"Densidad: {self.density} "
                f"MicroCalsificaciones: {self.micro_cal} "
                f"Benigna: {self.benign} "
                f"Birad: {self.birad}")

    def to_tuple(self) -> tuple:
        """Convierte el nódulo a una tupla de valores"""
        return (
            self.contains_nodule,
            self.morphology,
            self.margin,
            self.density,
            self.micro_cal,
            self.benign,
            self.birad
        )       

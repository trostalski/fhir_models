"""
Generated class for CodeableReference. 
Time: 2024-06-14 18:56:04
"""

from fhirmodels.fhir_base_model import FhirBaseModel
from fhirmodels.R5.CodeableConcept import *
from fhirmodels.R5.Extension import *
from fhirmodels.R5.Reference import *


class CodeableReference(FhirBaseModel):
    """CodeableReference Type: A reference to a resource (by instance), or instead, a reference to a concept defined in a terminology or ontology (by class).
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param CodeableConcept concept: Reference to a concept (by class)
    :param Reference reference: Reference to a resource (by instance)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "concept": {"class_name": "CodeableConcept", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        concept: "CodeableConcept" = None,
        reference: "Reference" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.concept = concept
        self.reference = reference

    @classmethod
    def from_dict(cls, data: dict) -> "CodeableReference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CodeableReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

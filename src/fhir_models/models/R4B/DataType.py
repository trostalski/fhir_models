"""
Generated class for DataType. 
Time: 2024-06-13 23:34:40
"""

from fhir_models.generator import FhirBaseModel
from fhir_models.models.R4B.Extension import *


class DataType(FhirBaseModel):
    """Base StructureDefinition for DataType Type: The base class for all re-useable types defined as part of the FHIR Specification.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
    ):

        self.id = id
        self.extension = extension or []

    @classmethod
    def from_dict(cls, data: dict) -> "DataType":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DataType":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

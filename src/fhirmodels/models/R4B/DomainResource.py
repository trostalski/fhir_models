"""
Generated class for DomainResource. 
Time: 2024-06-13 23:34:40
"""

from fhirmodels.models.R4B.Extension import *
from fhirmodels.models.R4B.Meta import *
from fhirmodels.models.R4B.Narrative import *
from fhirmodels.models.R4B.Resource import *


class DomainResource(Resource):
    """A resource that includes narrative, extensions, and contained resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
    ):

        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []

    @classmethod
    def from_dict(cls, data: dict) -> "DomainResource":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DomainResource":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

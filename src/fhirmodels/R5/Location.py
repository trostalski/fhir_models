"""
Generated class for Location. 
Time: 2024-06-14 18:37:55
"""

from fhirmodels.R5.Address import *
from fhirmodels.R5.Availability import *
from fhirmodels.R5.BackboneElement import *
from fhirmodels.R5.CodeableConcept import *
from fhirmodels.R5.Coding import *
from fhirmodels.R5.DomainResource import *
from fhirmodels.R5.ExtendedContactDetail import *
from fhirmodels.R5.Extension import *
from fhirmodels.R5.Identifier import *
from fhirmodels.R5.Meta import *
from fhirmodels.R5.Narrative import *
from fhirmodels.R5.Reference import *
from fhirmodels.R5.Resource import *
from fhirmodels.R5.VirtualServiceDetail import *


class Position(FhirBaseModel):
    """The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float longitude: Longitude with WGS84 datum
    :param float latitude: Latitude with WGS84 datum
    :param float altitude: Altitude with WGS84 datum
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        longitude: "float" = None,
        latitude: "float" = None,
        altitude: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude

    @classmethod
    def from_dict(cls, data: dict) -> "Location":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Location":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Location(DomainResource):
    """Details and position information for a place where services are provided and resources and participants may be stored, found, contained, or accommodated.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique code or number identifying the location to its users
    :param str status: active | suspended | inactive
    :param Coding operationalStatus: The operational status of the location (typically only for a bed/room)
    :param str name: Name of the location as used by humans
    :param str alias: A list of alternate names that the location is known as, or was known as, in the past
    :param str description: Additional details about the location that could be displayed as further information to identify the location beyond its name
    :param str mode: instance | kind
    :param CodeableConcept type: Type of function performed
    :param ExtendedContactDetail contact: Official contact details for the location
    :param Address address: Physical location
    :param CodeableConcept form: Physical form of the location
    :param Position position: The absolute geographic location
    :param Reference managingOrganization: Organization responsible for provisioning and upkeep
    :param Reference partOf: Another Location this one is physically a part of
    :param CodeableConcept characteristic: Collection of characteristics (attributes)
    :param Availability hoursOfOperation: What days/times during a week is this location usually open (including exceptions)
    :param VirtualServiceDetail virtualService: Connection details of a virtual service (e.g. conference call)
    :param Reference endpoint: Technical endpoints providing access to services operated for the location
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "operationalStatus": {"class_name": "Coding", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "contact": {"class_name": "ExtendedContactDetail", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "form": {"class_name": "CodeableConcept", "is_contained": False},
        "position": {"class_name": "Position", "is_contained": True},
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "characteristic": {"class_name": "CodeableConcept", "is_contained": False},
        "hoursOfOperation": {"class_name": "Availability", "is_contained": False},
        "virtualService": {"class_name": "VirtualServiceDetail", "is_contained": False},
        "endpoint": {"class_name": "Reference", "is_contained": False},
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
        identifier: list["Identifier"] = None,
        status: "str" = None,
        operationalStatus: "Coding" = None,
        name: "str" = None,
        alias: list["str"] = None,
        description: "str" = None,
        mode: "str" = None,
        type: list["CodeableConcept"] = None,
        contact: list["ExtendedContactDetail"] = None,
        address: "Address" = None,
        form: "CodeableConcept" = None,
        position: "Position" = None,
        managingOrganization: "Reference" = None,
        partOf: "Reference" = None,
        characteristic: list["CodeableConcept"] = None,
        hoursOfOperation: list["Availability"] = None,
        virtualService: list["VirtualServiceDetail"] = None,
        endpoint: list["Reference"] = None,
    ):

        self.resourceType = "Location"

        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.operationalStatus = operationalStatus
        self.name = name
        self.alias = alias or []
        self.description = description
        self.mode = mode
        self.type = type or []
        self.contact = contact or []
        self.address = address
        self.form = form
        self.position = position
        self.managingOrganization = managingOrganization
        self.partOf = partOf
        self.characteristic = characteristic or []
        self.hoursOfOperation = hoursOfOperation or []
        self.virtualService = virtualService or []
        self.endpoint = endpoint or []

    @classmethod
    def from_dict(cls, data: dict) -> "Location":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Location":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

"""
Generated class for DataRequirement. 
Time: 2024-06-13 23:38:27
"""

from fhir_models.generator import FhirBaseModel
from fhir_models.models.R5.CodeableConcept import *
from fhir_models.models.R5.Coding import *
from fhir_models.models.R5.Duration import *
from fhir_models.models.R5.Element import *
from fhir_models.models.R5.Extension import *
from fhir_models.models.R5.Period import *
from fhir_models.models.R5.Reference import *


class CodeFilter(FhirBaseModel):
    """Code filters specify additional constraints on the data, specifying the value set of interest for a particular element of the data. Each code filter defines an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: A code-valued attribute to filter on
    :param str searchParam: A coded (token) parameter to search on
    :param str valueSet: ValueSet for the filter
    :param Coding code: What code is expected
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        path: "str" = None,
        searchParam: "str" = None,
        valueSet: "str" = None,
        code: list["Coding"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.path = path
        self.searchParam = searchParam
        self.valueSet = valueSet
        self.code = code or []

    @classmethod
    def from_dict(cls, data: dict) -> "DataRequirement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DataRequirement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DateFilter(FhirBaseModel):
    """Date filters specify additional constraints on the data in terms of the applicable date range for specific elements. Each date filter specifies an additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: A date-valued attribute to filter on
    :param str searchParam: A date valued parameter to search on
    :param str valueDateTime: The value of the filter, as a Period, DateTime, or Duration value
    :param Period valuePeriod: The value of the filter, as a Period, DateTime, or Duration value
    :param Duration valueDuration: The value of the filter, as a Period, DateTime, or Duration value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        "valueDuration": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        path: "str" = None,
        searchParam: "str" = None,
        valueDateTime: "str" = None,
        valuePeriod: "Period" = None,
        valueDuration: "Duration" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.path = path
        self.searchParam = searchParam
        self.valueDateTime = valueDateTime
        self.valuePeriod = valuePeriod
        self.valueDuration = valueDuration

    @classmethod
    def from_dict(cls, data: dict) -> "DataRequirement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DataRequirement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ValueFilter(FhirBaseModel):
    """Value filters specify additional constraints on the data for elements other than code-valued or date-valued. Each value filter specifies an additional constraint on the data (i.e. valueFilters are AND'ed, not OR'ed).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: An attribute to filter on
    :param str searchParam: A parameter to search on
    :param str comparator: eq | gt | lt | ge | le | sa | eb
    :param str valueDateTime: The value of the filter, as a Period, DateTime, or Duration value
    :param Period valuePeriod: The value of the filter, as a Period, DateTime, or Duration value
    :param Duration valueDuration: The value of the filter, as a Period, DateTime, or Duration value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        "valueDuration": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        path: "str" = None,
        searchParam: "str" = None,
        comparator: "str" = None,
        valueDateTime: "str" = None,
        valuePeriod: "Period" = None,
        valueDuration: "Duration" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.path = path
        self.searchParam = searchParam
        self.comparator = comparator
        self.valueDateTime = valueDateTime
        self.valuePeriod = valuePeriod
        self.valueDuration = valueDuration

    @classmethod
    def from_dict(cls, data: dict) -> "DataRequirement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DataRequirement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Sort(FhirBaseModel):
    """Specifies the order of the results to be returned.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: The name of the attribute to perform the sort
    :param str direction: ascending | descending
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        path: "str" = None,
        direction: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.path = path
        self.direction = direction

    @classmethod
    def from_dict(cls, data: dict) -> "DataRequirement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DataRequirement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DataRequirement(FhirBaseModel):
    """DataRequirement Type: Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: The type of the required data
    :param str profile: The profile of the required data
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str mustSupport: Indicates specific structure elements that are referenced by the knowledge module
    :param CodeFilter codeFilter: What codes are expected
    :param DateFilter dateFilter: What dates/date ranges are expected
    :param ValueFilter valueFilter: What values are expected
    :param int limit: Number of results
    :param Sort sort: Order of the results
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "subjectCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        "codeFilter": {"class_name": "CodeFilter", "is_contained": True},
        "dateFilter": {"class_name": "DateFilter", "is_contained": True},
        "valueFilter": {"class_name": "ValueFilter", "is_contained": True},
        "sort": {"class_name": "Sort", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        type: "str" = None,
        profile: list["str"] = None,
        subjectCodeableConcept: "CodeableConcept" = None,
        subjectReference: "Reference" = None,
        mustSupport: list["str"] = None,
        codeFilter: list["CodeFilter"] = None,
        dateFilter: list["DateFilter"] = None,
        valueFilter: list["ValueFilter"] = None,
        limit: "int" = None,
        sort: list["Sort"] = None,
    ):

        self.id = id
        self.extension = extension or []
        self.type = type
        self.profile = profile or []
        self.subjectCodeableConcept = subjectCodeableConcept
        self.subjectReference = subjectReference
        self.mustSupport = mustSupport or []
        self.codeFilter = codeFilter or []
        self.dateFilter = dateFilter or []
        self.valueFilter = valueFilter or []
        self.limit = limit
        self.sort = sort or []

    @classmethod
    def from_dict(cls, data: dict) -> "DataRequirement":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "DataRequirement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

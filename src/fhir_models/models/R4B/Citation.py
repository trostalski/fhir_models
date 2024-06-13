"""
Generated class for Citation. 
Time: 2024-06-13 23:34:40
"""

from fhir_models.models.R4B.Address import *
from fhir_models.models.R4B.Annotation import *
from fhir_models.models.R4B.Attachment import *
from fhir_models.models.R4B.BackboneElement import *
from fhir_models.models.R4B.CodeableConcept import *
from fhir_models.models.R4B.ContactDetail import *
from fhir_models.models.R4B.ContactPoint import *
from fhir_models.models.R4B.DomainResource import *
from fhir_models.models.R4B.Extension import *
from fhir_models.models.R4B.HumanName import *
from fhir_models.models.R4B.Identifier import *
from fhir_models.models.R4B.Meta import *
from fhir_models.models.R4B.Narrative import *
from fhir_models.models.R4B.Period import *
from fhir_models.models.R4B.Reference import *
from fhir_models.models.R4B.Resource import *
from fhir_models.models.R4B.UsageContext import *


class Summary(FhirBaseModel):
    """A human-readable display of the citation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept style: Format for display of the citation
    :param str text: The human-readable display of the citation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "style": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        style: "CodeableConcept" = None,
        text: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.style = style
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Classification(FhirBaseModel):
    """The assignment to an organizing scheme.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of classifier (e.g. publication type, keyword)
    :param CodeableConcept classifier: The specific classification value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        classifier: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.classifier = classifier or []

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class StatusDate(FhirBaseModel):
    """An effective date or period for a status of the citation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept activity: Classification of the status
    :param bool actual: Either occurred or expected
    :param Period period: When the status started and/or ended
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "activity": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        activity: "CodeableConcept" = None,
        actual: "bool" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.activity = activity
        self.actual = actual
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RelatesTo(FhirBaseModel):
    """Artifact related to the Citation Resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationshipType: How the Citation resource relates to the target artifact
    :param CodeableConcept targetClassifier: The clasification of the related artifact
    :param str targetUri: The article or artifact that the Citation Resource is related to
    :param Identifier targetIdentifier: The article or artifact that the Citation Resource is related to
    :param Reference targetReference: The article or artifact that the Citation Resource is related to
    :param Attachment targetAttachment: The article or artifact that the Citation Resource is related to
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "relationshipType": {"class_name": "CodeableConcept", "is_contained": False},
        "targetClassifier": {"class_name": "CodeableConcept", "is_contained": False},
        "targetIdentifier": {"class_name": "Identifier", "is_contained": False},
        "targetReference": {"class_name": "Reference", "is_contained": False},
        "targetAttachment": {"class_name": "Attachment", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        relationshipType: "CodeableConcept" = None,
        targetClassifier: list["CodeableConcept"] = None,
        targetUri: "str" = None,
        targetIdentifier: "Identifier" = None,
        targetReference: "Reference" = None,
        targetAttachment: "Attachment" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relationshipType = relationshipType
        self.targetClassifier = targetClassifier or []
        self.targetUri = targetUri
        self.targetIdentifier = targetIdentifier
        self.targetReference = targetReference
        self.targetAttachment = targetAttachment

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Version(FhirBaseModel):
    """The defined version of the cited artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str value: The version number or other version identifier
    :param Reference baseCitation: Citation for the main version of the cited artifact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "baseCitation": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        value: "str" = None,
        baseCitation: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.value = value
        self.baseCitation = baseCitation

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class StatusDate(FhirBaseModel):
    """An effective date or period for a status of the cited artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept activity: Classification of the status
    :param bool actual: Either occurred or expected
    :param Period period: When the status started and/or ended
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "activity": {"class_name": "CodeableConcept", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        activity: "CodeableConcept" = None,
        actual: "bool" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.activity = activity
        self.actual = actual
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Title(FhirBaseModel):
    """The title details of the article or artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of title
    :param CodeableConcept language: Used to express the specific language
    :param str text: The title of the article or artifact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: list["CodeableConcept"] = None,
        language: "CodeableConcept" = None,
        text: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.language = language
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Abstract(FhirBaseModel):
    """Summary of the article or artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of abstract
    :param CodeableConcept language: Used to express the specific language
    :param str text: Abstract content
    :param str copyright: Copyright notice for the abstract
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        language: "CodeableConcept" = None,
        text: "str" = None,
        copyright: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.language = language
        self.text = text
        self.copyright = copyright

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Part(FhirBaseModel):
    """The component of the article or artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of component
    :param str value: The specification of the component
    :param Reference baseCitation: The citation for the full article or artifact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "baseCitation": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        value: "str" = None,
        baseCitation: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.value = value
        self.baseCitation = baseCitation

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RelatesTo(FhirBaseModel):
    """The artifact related to the cited artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationshipType: How the cited artifact relates to the target artifact
    :param CodeableConcept targetClassifier: The clasification of the related artifact
    :param str targetUri: The article or artifact that the cited artifact is related to
    :param Identifier targetIdentifier: The article or artifact that the cited artifact is related to
    :param Reference targetReference: The article or artifact that the cited artifact is related to
    :param Attachment targetAttachment: The article or artifact that the cited artifact is related to
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "relationshipType": {"class_name": "CodeableConcept", "is_contained": False},
        "targetClassifier": {"class_name": "CodeableConcept", "is_contained": False},
        "targetIdentifier": {"class_name": "Identifier", "is_contained": False},
        "targetReference": {"class_name": "Reference", "is_contained": False},
        "targetAttachment": {"class_name": "Attachment", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        relationshipType: "CodeableConcept" = None,
        targetClassifier: list["CodeableConcept"] = None,
        targetUri: "str" = None,
        targetIdentifier: "Identifier" = None,
        targetReference: "Reference" = None,
        targetAttachment: "Attachment" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relationshipType = relationshipType
        self.targetClassifier = targetClassifier or []
        self.targetUri = targetUri
        self.targetIdentifier = targetIdentifier
        self.targetReference = targetReference
        self.targetAttachment = targetAttachment

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PublishedIn(FhirBaseModel):
    """The collection the cited article or artifact is published in.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Kind of container (e.g. Periodical, database, or book)
    :param Identifier identifier: Journal identifiers include ISSN, ISO Abbreviation and NLMuniqueID; Book identifiers include ISBN
    :param str title: Name of the database or title of the book or journal
    :param Reference publisher: Name of the publisher
    :param str publisherLocation: Geographic location of the publisher
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "publisher": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        identifier: list["Identifier"] = None,
        title: "str" = None,
        publisher: "Reference" = None,
        publisherLocation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.identifier = identifier or []
        self.title = title
        self.publisher = publisher
        self.publisherLocation = publisherLocation

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DateOfPublication(FhirBaseModel):
    """Defining the date on which the issue of the journal was published.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: Date on which the issue of the journal was published
    :param str year: Year on which the issue of the journal was published
    :param str month: Month on which the issue of the journal was published
    :param str day: Day on which the issue of the journal was published
    :param str season: Season on which the issue of the journal was published
    :param str text: Text representation of the date of which the issue of the journal was published
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
        date: "str" = None,
        year: "str" = None,
        month: "str" = None,
        day: "str" = None,
        season: "str" = None,
        text: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.season = season
        self.text = text

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PeriodicRelease(FhirBaseModel):
    """The specific issue in which the cited article resides.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept citedMedium: Internet or Print
    :param str volume: Volume number of journal in which the article is published
    :param str issue: Issue, part or supplement of journal in which the article is published
    :param DateOfPublication dateOfPublication: Defining the date on which the issue of the journal was published
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "citedMedium": {"class_name": "CodeableConcept", "is_contained": False},
        "dateOfPublication": {"class_name": "DateOfPublication", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        citedMedium: "CodeableConcept" = None,
        volume: "str" = None,
        issue: "str" = None,
        dateOfPublication: "DateOfPublication" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.citedMedium = citedMedium
        self.volume = volume
        self.issue = issue
        self.dateOfPublication = dateOfPublication

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PublicationForm(FhirBaseModel):
    """If multiple, used to represent alternative forms of the article that are not separate citations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param PublishedIn publishedIn: The collection the cited article or artifact is published in
    :param PeriodicRelease periodicRelease: The specific issue in which the cited article resides
    :param str articleDate: The date the article was added to the database, or the date the article was released
    :param str lastRevisionDate: The date the article was last revised or updated in the database
    :param CodeableConcept language: Language in which this form of the article is published
    :param str accessionNumber: Entry number or identifier for inclusion in a database
    :param str pageString: Used for full display of pagination
    :param str firstPage: Used for isolated representation of first page
    :param str lastPage: Used for isolated representation of last page
    :param str pageCount: Number of pages or screens
    :param str copyright: Copyright notice for the full article or artifact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "publishedIn": {"class_name": "PublishedIn", "is_contained": True},
        "periodicRelease": {"class_name": "PeriodicRelease", "is_contained": True},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        publishedIn: "PublishedIn" = None,
        periodicRelease: "PeriodicRelease" = None,
        articleDate: "str" = None,
        lastRevisionDate: "str" = None,
        language: list["CodeableConcept"] = None,
        accessionNumber: "str" = None,
        pageString: "str" = None,
        firstPage: "str" = None,
        lastPage: "str" = None,
        pageCount: "str" = None,
        copyright: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.publishedIn = publishedIn
        self.periodicRelease = periodicRelease
        self.articleDate = articleDate
        self.lastRevisionDate = lastRevisionDate
        self.language = language or []
        self.accessionNumber = accessionNumber
        self.pageString = pageString
        self.firstPage = firstPage
        self.lastPage = lastPage
        self.pageCount = pageCount
        self.copyright = copyright

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class WebLocation(FhirBaseModel):
    """Used for any URL for the article or artifact cited.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code the reason for different URLs, e.g. abstract and full-text
    :param str url: The specific URL
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class WhoClassified(FhirBaseModel):
    """Provenance and copyright of classification.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference person: Person who created the classification
    :param Reference organization: Organization who created the classification
    :param Reference publisher: The publisher of the classification, not the publisher of the article or artifact being cited
    :param str classifierCopyright: Rights management statement for the classification
    :param bool freeToShare: Acceptable to re-use the classification
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "person": {"class_name": "Reference", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "publisher": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        person: "Reference" = None,
        organization: "Reference" = None,
        publisher: "Reference" = None,
        classifierCopyright: "str" = None,
        freeToShare: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.person = person
        self.organization = organization
        self.publisher = publisher
        self.classifierCopyright = classifierCopyright
        self.freeToShare = freeToShare

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Classification(FhirBaseModel):
    """The assignment to an organizing scheme.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of classifier (e.g. publication type, keyword)
    :param CodeableConcept classifier: The specific classification value
    :param WhoClassified whoClassified: Provenance and copyright of classification
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        "whoClassified": {"class_name": "WhoClassified", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        classifier: list["CodeableConcept"] = None,
        whoClassified: "WhoClassified" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.classifier = classifier or []
        self.whoClassified = whoClassified

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AffiliationInfo(FhirBaseModel):
    """Organization affiliated with the entity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str affiliation: Display for the organization
    :param str role: Role within the organization, such as professional title
    :param Identifier identifier: Identifier for the organization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        affiliation: "str" = None,
        role: "str" = None,
        identifier: list["Identifier"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.affiliation = affiliation
        self.role = role
        self.identifier = identifier or []

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ContributionInstance(FhirBaseModel):
    """Contributions with accounting for time or number.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The specific contribution
    :param str time: The time that the contribution was made
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        time: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.time = time

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Entry(FhirBaseModel):
    """An individual entity named in the author list or contributor list.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param HumanName name: A name associated with the person
    :param str initials: Initials for forename
    :param str collectiveName: Used for collective or corporate name as an author
    :param Identifier identifier: Author identifier, eg ORCID
    :param AffiliationInfo affiliationInfo: Organizational affiliation
    :param Address address: Physical mailing address
    :param ContactPoint telecom: Email or telephone contact methods for the author or contributor
    :param CodeableConcept contributionType: The specific contribution
    :param CodeableConcept role: The role of the contributor (e.g. author, editor, reviewer)
    :param ContributionInstance contributionInstance: Contributions with accounting for time or number
    :param bool correspondingContact: Indication of which contributor is the corresponding contributor for the role
    :param int listOrder: Used to code order of authors
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "affiliationInfo": {"class_name": "AffiliationInfo", "is_contained": True},
        "address": {"class_name": "Address", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "contributionType": {"class_name": "CodeableConcept", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "contributionInstance": {
            "class_name": "ContributionInstance",
            "is_contained": True,
        },
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "HumanName" = None,
        initials: "str" = None,
        collectiveName: "str" = None,
        identifier: list["Identifier"] = None,
        affiliationInfo: list["AffiliationInfo"] = None,
        address: list["Address"] = None,
        telecom: list["ContactPoint"] = None,
        contributionType: list["CodeableConcept"] = None,
        role: "CodeableConcept" = None,
        contributionInstance: list["ContributionInstance"] = None,
        correspondingContact: "bool" = None,
        listOrder: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.initials = initials
        self.collectiveName = collectiveName
        self.identifier = identifier or []
        self.affiliationInfo = affiliationInfo or []
        self.address = address or []
        self.telecom = telecom or []
        self.contributionType = contributionType or []
        self.role = role
        self.contributionInstance = contributionInstance or []
        self.correspondingContact = correspondingContact
        self.listOrder = listOrder

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Summary(FhirBaseModel):
    """Used to record a display of the author/contributor list without separate coding for each list member.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Either authorList or contributorshipStatement
    :param CodeableConcept style: The format for the display string
    :param CodeableConcept source: Used to code the producer or rule for creating the display string
    :param str value: The display string for the author list, contributor list, or contributorship statement
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "style": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        style: "CodeableConcept" = None,
        source: "CodeableConcept" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.style = style
        self.source = source
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Contributorship(FhirBaseModel):
    """This element is used to list authors and other contributors, their contact information, specific contributions, and summary statements.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool complete: Indicates if the list includes all authors and/or contributors
    :param Entry entry: An individual entity named in the list
    :param Summary summary: Used to record a display of the author/contributor list without separate coding for each list member
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "entry": {"class_name": "Entry", "is_contained": True},
        "summary": {"class_name": "Summary", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        complete: "bool" = None,
        entry: list["Entry"] = None,
        summary: list["Summary"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.complete = complete
        self.entry = entry or []
        self.summary = summary or []

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CitedArtifact(FhirBaseModel):
    """The article or artifact being described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: May include DOI, PMID, PMCID, etc.
    :param Identifier relatedIdentifier: May include trial registry identifiers
    :param str dateAccessed: When the cited artifact was accessed
    :param Version version: The defined version of the cited artifact
    :param CodeableConcept currentState: The status of the cited artifact
    :param StatusDate statusDate: An effective date or period for a status of the cited artifact
    :param Title title: The title details of the article or artifact
    :param Abstract abstract: Summary of the article or artifact
    :param Part part: The component of the article or artifact
    :param RelatesTo relatesTo: The artifact related to the cited artifact
    :param PublicationForm publicationForm: If multiple, used to represent alternative forms of the article that are not separate citations
    :param WebLocation webLocation: Used for any URL for the article or artifact cited
    :param Classification classification: The assignment to an organizing scheme
    :param Contributorship contributorship: Attribution of authors and other contributors
    :param Annotation note: Any additional information or content for the article or artifact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "relatedIdentifier": {"class_name": "Identifier", "is_contained": False},
        "version": {"class_name": "Version", "is_contained": True},
        "currentState": {"class_name": "CodeableConcept", "is_contained": False},
        "statusDate": {"class_name": "StatusDate", "is_contained": True},
        "title": {"class_name": "Title", "is_contained": True},
        "abstract": {"class_name": "Abstract", "is_contained": True},
        "part": {"class_name": "Part", "is_contained": True},
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        "publicationForm": {"class_name": "PublicationForm", "is_contained": True},
        "webLocation": {"class_name": "WebLocation", "is_contained": True},
        "classification": {"class_name": "Classification", "is_contained": True},
        "contributorship": {"class_name": "Contributorship", "is_contained": True},
        "note": {"class_name": "Annotation", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        relatedIdentifier: list["Identifier"] = None,
        dateAccessed: "str" = None,
        version: "Version" = None,
        currentState: list["CodeableConcept"] = None,
        statusDate: list["StatusDate"] = None,
        title: list["Title"] = None,
        abstract: list["Abstract"] = None,
        part: "Part" = None,
        relatesTo: list["RelatesTo"] = None,
        publicationForm: list["PublicationForm"] = None,
        webLocation: list["WebLocation"] = None,
        classification: list["Classification"] = None,
        contributorship: "Contributorship" = None,
        note: list["Annotation"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.relatedIdentifier = relatedIdentifier or []
        self.dateAccessed = dateAccessed
        self.version = version
        self.currentState = currentState or []
        self.statusDate = statusDate or []
        self.title = title or []
        self.abstract = abstract or []
        self.part = part
        self.relatesTo = relatesTo or []
        self.publicationForm = publicationForm or []
        self.webLocation = webLocation or []
        self.classification = classification or []
        self.contributorship = contributorship
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Citation(DomainResource):
    """The Citation Resource enables reference to any knowledge artifact for purposes of identification and attribution. The Citation Resource supports existing reference structures and developing publication practices such as versioning, expressing complex contributorship roles, and referencing computable resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this citation, represented as a globally unique URI
    :param Identifier identifier: Identifier for the Citation resource itself
    :param str version: Business version of the citation
    :param str name: Name for this citation (computer friendly)
    :param str title: Name for this citation (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: The publisher of the Citation, not the publisher of the article or artifact being cited
    :param ContactDetail contact: Contact details for the publisher of the Citation Resource
    :param str description: Natural language description of the citation
    :param UsageContext useContext: The context that the Citation Resource content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for citation (if applicable)
    :param str purpose: Why this citation is defined
    :param str copyright: Use and/or publishing restrictions for the Citation, not for the cited artifact
    :param str approvalDate: When the citation was approved by publisher
    :param str lastReviewDate: When the citation was last reviewed
    :param Period effectivePeriod: When the citation is expected to be used
    :param ContactDetail author: Who authored the Citation
    :param ContactDetail editor: Who edited the Citation
    :param ContactDetail reviewer: Who reviewed the Citation
    :param ContactDetail endorser: Who endorsed the Citation
    :param Summary summary: A human-readable display of the citation
    :param Classification classification: The assignment to an organizing scheme
    :param Annotation note: Used for general notes and annotations not coded elsewhere
    :param CodeableConcept currentState: The status of the citation
    :param StatusDate statusDate: An effective date or period for a status of the citation
    :param RelatesTo relatesTo: Artifact related to the Citation Resource
    :param CitedArtifact citedArtifact: The article or artifact being described
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        "author": {"class_name": "ContactDetail", "is_contained": False},
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        "summary": {"class_name": "Summary", "is_contained": True},
        "classification": {"class_name": "Classification", "is_contained": True},
        "note": {"class_name": "Annotation", "is_contained": False},
        "currentState": {"class_name": "CodeableConcept", "is_contained": False},
        "statusDate": {"class_name": "StatusDate", "is_contained": True},
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        "citedArtifact": {"class_name": "CitedArtifact", "is_contained": True},
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
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        name: "str" = None,
        title: "str" = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        description: "str" = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        purpose: "str" = None,
        copyright: "str" = None,
        approvalDate: "str" = None,
        lastReviewDate: "str" = None,
        effectivePeriod: "Period" = None,
        author: list["ContactDetail"] = None,
        editor: list["ContactDetail"] = None,
        reviewer: list["ContactDetail"] = None,
        endorser: list["ContactDetail"] = None,
        summary: list["Summary"] = None,
        classification: list["Classification"] = None,
        note: list["Annotation"] = None,
        currentState: list["CodeableConcept"] = None,
        statusDate: list["StatusDate"] = None,
        relatesTo: list["RelatesTo"] = None,
        citedArtifact: "CitedArtifact" = None,
    ):

        self.resourceType = "Citation"

        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.name = name
        self.title = title
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.description = description
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose
        self.copyright = copyright
        self.approvalDate = approvalDate
        self.lastReviewDate = lastReviewDate
        self.effectivePeriod = effectivePeriod
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.summary = summary or []
        self.classification = classification or []
        self.note = note or []
        self.currentState = currentState or []
        self.statusDate = statusDate or []
        self.relatesTo = relatesTo or []
        self.citedArtifact = citedArtifact

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

"""
Generated class for ImplementationGuide. 
Time: 2024-06-13 23:38:27
"""

from fhir_models.models.R5.BackboneElement import *
from fhir_models.models.R5.CodeableConcept import *
from fhir_models.models.R5.Coding import *
from fhir_models.models.R5.ContactDetail import *
from fhir_models.models.R5.DomainResource import *
from fhir_models.models.R5.Extension import *
from fhir_models.models.R5.Identifier import *
from fhir_models.models.R5.Meta import *
from fhir_models.models.R5.Narrative import *
from fhir_models.models.R5.Reference import *
from fhir_models.models.R5.Resource import *
from fhir_models.models.R5.UsageContext import *


class DependsOn(FhirBaseModel):
    """Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: Identity of the IG that this depends on
    :param str packageId: NPM Package name for IG this depends on
    :param str version: Version of the IG
    :param str reason: Why dependency exists
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
        uri: "str" = None,
        packageId: "str" = None,
        version: "str" = None,
        reason: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.uri = uri
        self.packageId = packageId
        self.version = version
        self.reason = reason

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class _global(FhirBaseModel):
    """A set of profiles that all resources covered by this implementation guide must conform to.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Type this profile applies to
    :param str profile: Profile that all resources must conform to
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
        type: "str" = None,
        profile: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.profile = profile

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Grouping(FhirBaseModel):
    """A logical group of resources. Logical groups can be used when building pages.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Descriptive name for the package
    :param str description: Human readable text describing the package
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
        name: "str" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Resource(FhirBaseModel):
    """A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Location of the resource
    :param str fhirVersion: Versions this applies to (if different to IG)
    :param str name: Human readable name for the resource
    :param str description: Reason why included in guide
    :param bool isExample: Is this an example
    :param str profile: Profile(s) this is an example of
    :param str groupingId: Grouping this is part of
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        reference: "Reference" = None,
        fhirVersion: list["str"] = None,
        name: "str" = None,
        description: "str" = None,
        isExample: "bool" = None,
        profile: list["str"] = None,
        groupingId: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference
        self.fhirVersion = fhirVersion or []
        self.name = name
        self.description = description
        self.isExample = isExample
        self.profile = profile or []
        self.groupingId = groupingId

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Page(FhirBaseModel):
    """A page / section in the implementation guide. The root page is the implementation guide home page.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str sourceUrl: Source for page
    :param str sourceString: Source for page
    :param str sourceMarkdown: Source for page
    :param str name: Name of the page when published
    :param str title: Short title shown for navigational assistance
    :param str generation: html | markdown | xml | generated
    :param Page page: Nested Pages / Sections
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "page": {"class_name": "Page", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sourceUrl: "str" = None,
        sourceString: "str" = None,
        sourceMarkdown: "str" = None,
        name: "str" = None,
        title: "str" = None,
        generation: "str" = None,
        page: list["Page"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sourceUrl = sourceUrl
        self.sourceString = sourceString
        self.sourceMarkdown = sourceMarkdown
        self.name = name
        self.title = title
        self.generation = generation
        self.page = page or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Parameter(FhirBaseModel):
    """A set of parameters that defines how the implementation guide is built. The parameters are defined by the relevant tools that build the implementation guides.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding code: Code that identifies parameter
    :param str value: Value for named type
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "Coding" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Template(FhirBaseModel):
    """A template for building resources.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Type of template specified
    :param str source: The source location for the template
    :param str scope: The scope in which the template applies
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
        code: "str" = None,
        source: "str" = None,
        scope: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.source = source
        self.scope = scope

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Definition(FhirBaseModel):
    """The information needed by an IG publisher tool to publish the whole implementation guide.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Grouping grouping: Grouping used to present related resources in the IG
    :param Resource resource: Resource in the implementation guide
    :param Page page: Page/Section in the Guide
    :param Parameter parameter: Defines how IG is built by tools
    :param Template template: A template for building resources
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "grouping": {"class_name": "Grouping", "is_contained": True},
        "resource": {"class_name": "Resource", "is_contained": True},
        "page": {"class_name": "Page", "is_contained": True},
        "parameter": {"class_name": "Parameter", "is_contained": True},
        "template": {"class_name": "Template", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        grouping: list["Grouping"] = None,
        resource: list["Resource"] = None,
        page: "Page" = None,
        parameter: list["Parameter"] = None,
        template: list["Template"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.grouping = grouping or []
        self.resource = resource or []
        self.page = page
        self.parameter = parameter or []
        self.template = template or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Resource(FhirBaseModel):
    """A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Location of the resource
    :param bool isExample: Is this an example
    :param str profile: Profile(s) this is an example of
    :param str relativePath: Relative path for page in IG
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "reference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        reference: "Reference" = None,
        isExample: "bool" = None,
        profile: list["str"] = None,
        relativePath: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference
        self.isExample = isExample
        self.profile = profile or []
        self.relativePath = relativePath

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Page(FhirBaseModel):
    """Information about a page within the IG.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: HTML page name
    :param str title: Title of the page, for references
    :param str anchor: Anchor available on the page
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
        name: "str" = None,
        title: "str" = None,
        anchor: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.title = title
        self.anchor = anchor or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Manifest(FhirBaseModel):
    """Information about an assembled implementation guide, created by the publication tooling.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str rendering: Location of rendered implementation guide
    :param Resource resource: Resource in the implementation guide
    :param Page page: HTML page within the parent IG
    :param str image: Image within the IG
    :param str other: Additional linkable file in IG
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "resource": {"class_name": "Resource", "is_contained": True},
        "page": {"class_name": "Page", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        rendering: "str" = None,
        resource: list["Resource"] = None,
        page: list["Page"] = None,
        image: list["str"] = None,
        other: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.rendering = rendering
        self.resource = resource or []
        self.page = page or []
        self.image = image or []
        self.other = other or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ImplementationGuide(DomainResource):
    """A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this implementation guide, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the implementation guide (business identifier)
    :param str version: Business version of the implementation guide
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this implementation guide (computer friendly)
    :param str title: Name for this implementation guide (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the implementation guide
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for implementation guide (if applicable)
    :param str purpose: Why this implementation guide is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str packageId: NPM Package name for IG
    :param str license: SPDX license code for this IG (or not-open-source)
    :param str fhirVersion: FHIR Version(s) this Implementation Guide targets
    :param DependsOn dependsOn: Another Implementation guide this depends on
    :param _global _global: Profiles that apply globally
    :param Definition definition: Information needed to build the IG
    :param Manifest manifest: Information about an assembled IG
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "dependsOn": {"class_name": "DependsOn", "is_contained": True},
        "_global": {"class_name": "_global", "is_contained": True},
        "definition": {"class_name": "Definition", "is_contained": True},
        "manifest": {"class_name": "Manifest", "is_contained": True},
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
        versionAlgorithmString: "str" = None,
        versionAlgorithmCoding: "Coding" = None,
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
        copyrightLabel: "str" = None,
        packageId: "str" = None,
        license: "str" = None,
        fhirVersion: list["str"] = None,
        dependsOn: list["DependsOn"] = None,
        _global: list["_global"] = None,
        definition: "Definition" = None,
        manifest: "Manifest" = None,
    ):

        self.resourceType = "ImplementationGuide"

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
        self.versionAlgorithmString = versionAlgorithmString
        self.versionAlgorithmCoding = versionAlgorithmCoding
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
        self.copyrightLabel = copyrightLabel
        self.packageId = packageId
        self.license = license
        self.fhirVersion = fhirVersion or []
        self.dependsOn = dependsOn or []
        self._global = _global or []
        self.definition = definition
        self.manifest = manifest

    @classmethod
    def from_dict(cls, data: dict) -> "ImplementationGuide":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImplementationGuide":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

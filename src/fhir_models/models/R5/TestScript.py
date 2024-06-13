"""
Generated class for TestScript. 
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


class Origin(FhirBaseModel):
    """An abstract server used in operations within this test script in the origin element.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract origin server starting at 1
    :param Coding profile: FHIR-Client | FHIR-SDC-FormFiller
    :param str url: The url path of the origin server
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "profile": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        index: "int" = None,
        profile: "Coding" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.index = index
        self.profile = profile
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Destination(FhirBaseModel):
    """An abstract server used in operations within this test script in the destination element.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract destination server starting at 1
    :param Coding profile: FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-FormProcessor
    :param str url: The url path of the destination server
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "profile": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        index: "int" = None,
        profile: "Coding" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.index = index
        self.profile = profile
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Link(FhirBaseModel):
    """A link to the FHIR specification that this test is covering.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: URL to the specification
    :param str description: Short description
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
        url: "str" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Capability(FhirBaseModel):
    """Capabilities that must exist and are assumed to function correctly on the FHIR server being tested.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool required: Are the capabilities required?
    :param bool validated: Are the capabilities validated?
    :param str description: The expected capabilities of the server
    :param int origin: Which origin server these requirements apply to
    :param int destination: Which server these requirements apply to
    :param str link: Links to the FHIR specification
    :param str capabilities: Required Capability Statement
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
        required: "bool" = None,
        validated: "bool" = None,
        description: "str" = None,
        origin: list["int"] = None,
        destination: "int" = None,
        link: list["str"] = None,
        capabilities: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.required = required
        self.validated = validated
        self.description = description
        self.origin = origin or []
        self.destination = destination
        self.link = link or []
        self.capabilities = capabilities

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Metadata(FhirBaseModel):
    """The required capability must exist and are assumed to function correctly on the FHIR server being tested.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Link link: Links to the FHIR specification
    :param Capability capability: Capabilities  that are assumed to function correctly on the FHIR server being tested
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "link": {"class_name": "Link", "is_contained": True},
        "capability": {"class_name": "Capability", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        link: list["Link"] = None,
        capability: list["Capability"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.link = link or []
        self.capability = capability or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Scope(FhirBaseModel):
    """The scope indicates a conformance artifact that is tested by the test(s) within this test case and the expectation of the test outcome(s) as well as the intended test phase inclusion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str artifact: The specific conformance artifact being tested
    :param CodeableConcept conformance: required | optional | strict
    :param CodeableConcept phase: unit | integration | production
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "conformance": {"class_name": "CodeableConcept", "is_contained": False},
        "phase": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        artifact: "str" = None,
        conformance: "CodeableConcept" = None,
        phase: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.artifact = artifact
        self.conformance = conformance
        self.phase = phase

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Fixture(FhirBaseModel):
    """Fixture in the test script - by reference (uri). All fixtures are required for the test script to execute.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool autocreate: Whether or not to implicitly create the fixture during setup
    :param bool autodelete: Whether or not to implicitly delete the fixture during teardown
    :param Reference resource: Reference of the resource
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "resource": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        autocreate: "bool" = None,
        autodelete: "bool" = None,
        resource: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.autocreate = autocreate
        self.autodelete = autodelete
        self.resource = resource

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Variable(FhirBaseModel):
    """Variable is set based either on element value in response body or on header field value in the response headers.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Descriptive name for this variable
    :param str defaultValue: Default, hard-coded, or user-defined value for this variable
    :param str description: Natural language description of the variable
    :param str expression: The FHIRPath expression against the fixture body
    :param str headerField: HTTP header field name for source
    :param str hint: Hint help text for default value to enter
    :param str path: XPath or JSONPath against the fixture body
    :param str sourceId: Fixture Id of source expression or headerField within this variable
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
        defaultValue: "str" = None,
        description: "str" = None,
        expression: "str" = None,
        headerField: "str" = None,
        hint: "str" = None,
        path: "str" = None,
        sourceId: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.defaultValue = defaultValue
        self.description = description
        self.expression = expression
        self.headerField = headerField
        self.hint = hint
        self.path = path
        self.sourceId = sourceId

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RequestHeader(FhirBaseModel):
    """Header elements would be used to set HTTP headers.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
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
        field: "str" = None,
        value: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.field = field
        self.value = value

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Operation(FhirBaseModel):
    """The operation to perform.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc
    :param str contentType: Mime type of the request payload contents, with charset etc
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param RequestHeader requestHeader: Each operation can have one or more header elements
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
        "requestHeader": {"class_name": "RequestHeader", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "Coding" = None,
        resource: "str" = None,
        label: "str" = None,
        description: "str" = None,
        accept: "str" = None,
        contentType: "str" = None,
        destination: "int" = None,
        encodeRequestUrl: "bool" = None,
        method: "str" = None,
        origin: "int" = None,
        params: "str" = None,
        requestHeader: list["RequestHeader"] = None,
        requestId: "str" = None,
        responseId: "str" = None,
        sourceId: "str" = None,
        targetId: "str" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.resource = resource
        self.label = label
        self.description = description
        self.accept = accept
        self.contentType = contentType
        self.destination = destination
        self.encodeRequestUrl = encodeRequestUrl
        self.method = method
        self.origin = origin
        self.params = params
        self.requestHeader = requestHeader or []
        self.requestId = requestId
        self.responseId = responseId
        self.sourceId = sourceId
        self.targetId = targetId
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Requirement(FhirBaseModel):
    """Links or references providing traceability to the testing requirements for this assert.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkUri: Link or reference to the testing requirement
    :param str linkCanonical: Link or reference to the testing requirement
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
        linkUri: "str" = None,
        linkCanonical: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkUri = linkUri
        self.linkCanonical = linkCanonical

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class _assert(FhirBaseModel):
    """Evaluates the results of previous operations to determine if the server under test behaves appropriately.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str label: Tracking/logging assertion label
    :param str description: Tracking/reporting assertion description
    :param str direction: response | request
    :param str compareToSourceId: Id of the source fixture to be evaluated
    :param str compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture
    :param str compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture
    :param str contentType: Mime type to compare against the 'Content-Type' header
    :param str defaultManualCompletion: fail | pass | skip | stop
    :param str expression: The FHIRPath expression to be evaluated
    :param str headerField: HTTP header field name
    :param str minimumId: Fixture Id of minimum content resource
    :param bool navigationLinks: Perform validation on navigation links?
    :param str operator: equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval | manualEval
    :param str path: XPath or JSONPath expression
    :param str requestMethod: delete | get | options | patch | post | put | head
    :param str requestURL: Request URL comparison value
    :param str resource: Resource type
    :param str response: continue | switchingProtocols | okay | created | accepted | nonAuthoritativeInformation | noContent | resetContent | partialContent | multipleChoices | movedPermanently | found | seeOther | notModified | useProxy | temporaryRedirect | permanentRedirect | badRequest | unauthorized | paymentRequired | forbidden | notFound | methodNotAllowed | notAcceptable | proxyAuthenticationRequired | requestTimeout | conflict | gone | lengthRequired | preconditionFailed | contentTooLarge | uriTooLong | unsupportedMediaType | rangeNotSatisfiable | expectationFailed | misdirectedRequest | unprocessableContent | upgradeRequired | internalServerError | notImplemented | badGateway | serviceUnavailable | gatewayTimeout | httpVersionNotSupported
    :param str responseCode: HTTP response code to test
    :param str sourceId: Fixture Id of source expression or headerField
    :param bool stopTestOnFail: If this assert fails, will the current test execution stop?
    :param str validateProfileId: Profile Id of validation profile reference
    :param str value: The value to compare to
    :param bool warningOnly: Will this assert produce a warning only on error?
    :param Requirement requirement: Links or references to the testing requirements
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "requirement": {"class_name": "Requirement", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        label: "str" = None,
        description: "str" = None,
        direction: "str" = None,
        compareToSourceId: "str" = None,
        compareToSourceExpression: "str" = None,
        compareToSourcePath: "str" = None,
        contentType: "str" = None,
        defaultManualCompletion: "str" = None,
        expression: "str" = None,
        headerField: "str" = None,
        minimumId: "str" = None,
        navigationLinks: "bool" = None,
        operator: "str" = None,
        path: "str" = None,
        requestMethod: "str" = None,
        requestURL: "str" = None,
        resource: "str" = None,
        response: "str" = None,
        responseCode: "str" = None,
        sourceId: "str" = None,
        stopTestOnFail: "bool" = None,
        validateProfileId: "str" = None,
        value: "str" = None,
        warningOnly: "bool" = None,
        requirement: list["Requirement"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.label = label
        self.description = description
        self.direction = direction
        self.compareToSourceId = compareToSourceId
        self.compareToSourceExpression = compareToSourceExpression
        self.compareToSourcePath = compareToSourcePath
        self.contentType = contentType
        self.defaultManualCompletion = defaultManualCompletion
        self.expression = expression
        self.headerField = headerField
        self.minimumId = minimumId
        self.navigationLinks = navigationLinks
        self.operator = operator
        self.path = path
        self.requestMethod = requestMethod
        self.requestURL = requestURL
        self.resource = resource
        self.response = response
        self.responseCode = responseCode
        self.sourceId = sourceId
        self.stopTestOnFail = stopTestOnFail
        self.validateProfileId = validateProfileId
        self.value = value
        self.warningOnly = warningOnly
        self.requirement = requirement or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(FhirBaseModel):
    """Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The setup operation to perform
    :param _assert _assert: The assertion to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operation": {"class_name": "Operation", "is_contained": True},
        "_assert": {"class_name": "_assert", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operation: "Operation" = None,
        _assert: "_assert" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operation = operation
        self._assert = _assert

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Setup(FhirBaseModel):
    """A series of required setup operations before tests are executed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: A setup operation or assert to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "Action", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        action: list["Action"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(FhirBaseModel):
    """Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The setup operation to perform
    :param _assert _assert: The setup assertion to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operation": {"class_name": "Operation", "is_contained": True},
        "_assert": {"class_name": "_assert", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operation: "Operation" = None,
        _assert: "_assert" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operation = operation
        self._assert = _assert

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Test(FhirBaseModel):
    """A test in this script.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param Action action: A test operation or assert to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "Action", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        description: "str" = None,
        action: list["Action"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.description = description
        self.action = action or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(FhirBaseModel):
    """The teardown action will only contain an operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The teardown operation to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operation": {"class_name": "Operation", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operation: "Operation" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operation = operation

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Teardown(FhirBaseModel):
    """A series of operations required to clean up after all the tests are executed (successfully or otherwise).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: One or more teardown operations to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "Action", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        action: list["Action"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class TestScript(DomainResource):
    """A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this test script, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the test script
    :param str version: Business version of the test script
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this test script (computer friendly)
    :param str title: Name for this test script (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the test script
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for test script (if applicable)
    :param str purpose: Why this test script is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param Origin origin: An abstract server representing a client or sender in a message exchange
    :param Destination destination: An abstract server representing a destination or receiver in a message exchange
    :param Metadata metadata: Required capability that is assumed to function correctly on the FHIR server being tested
    :param Scope scope: Indication of the artifact(s) that are tested by this test case
    :param Fixture fixture: Fixture in the test script - by reference (uri)
    :param str profile: Reference of the validation profile
    :param Variable variable: Placeholder for evaluated elements
    :param Setup setup: A series of required setup operations before tests are executed
    :param Test test: A test in this script
    :param Teardown teardown: A series of required clean up steps
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
        "origin": {"class_name": "Origin", "is_contained": True},
        "destination": {"class_name": "Destination", "is_contained": True},
        "metadata": {"class_name": "Metadata", "is_contained": True},
        "scope": {"class_name": "Scope", "is_contained": True},
        "fixture": {"class_name": "Fixture", "is_contained": True},
        "variable": {"class_name": "Variable", "is_contained": True},
        "setup": {"class_name": "Setup", "is_contained": True},
        "test": {"class_name": "Test", "is_contained": True},
        "teardown": {"class_name": "Teardown", "is_contained": True},
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
        origin: list["Origin"] = None,
        destination: list["Destination"] = None,
        metadata: "Metadata" = None,
        scope: list["Scope"] = None,
        fixture: list["Fixture"] = None,
        profile: list["str"] = None,
        variable: list["Variable"] = None,
        setup: "Setup" = None,
        test: list["Test"] = None,
        teardown: "Teardown" = None,
    ):

        self.resourceType = "TestScript"

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
        self.origin = origin or []
        self.destination = destination or []
        self.metadata = metadata
        self.scope = scope or []
        self.fixture = fixture or []
        self.profile = profile or []
        self.variable = variable or []
        self.setup = setup
        self.test = test or []
        self.teardown = teardown

    @classmethod
    def from_dict(cls, data: dict) -> "TestScript":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestScript":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

"""
Generated class for ExplanationOfBenefit. 
Time: 2024-06-13 23:38:27
"""

from fhirmodels.models.R5.Address import *
from fhirmodels.models.R5.Attachment import *
from fhirmodels.models.R5.BackboneElement import *
from fhirmodels.models.R5.CodeableConcept import *
from fhirmodels.models.R5.CodeableReference import *
from fhirmodels.models.R5.Coding import *
from fhirmodels.models.R5.DomainResource import *
from fhirmodels.models.R5.Extension import *
from fhirmodels.models.R5.Identifier import *
from fhirmodels.models.R5.Meta import *
from fhirmodels.models.R5.Money import *
from fhirmodels.models.R5.Narrative import *
from fhirmodels.models.R5.Period import *
from fhirmodels.models.R5.Quantity import *
from fhirmodels.models.R5.Reference import *
from fhirmodels.models.R5.Resource import *


class Related(FhirBaseModel):
    """Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference claim: Reference to the related claim
    :param CodeableConcept relationship: How the reference claim is related
    :param Identifier reference: File or case reference
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "claim": {"class_name": "Reference", "is_contained": False},
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        "reference": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        claim: "Reference" = None,
        relationship: "CodeableConcept" = None,
        reference: "Identifier" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.claim = claim
        self.relationship = relationship
        self.reference = reference

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Event(FhirBaseModel):
    """Information code for an event with a corresponding date or period.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specific event
    :param str whenDateTime: Occurance date or period
    :param Period whenPeriod: Occurance date or period
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "whenPeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        whenDateTime: "str" = None,
        whenPeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.whenDateTime = whenDateTime
        self.whenPeriod = whenPeriod

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Payee(FhirBaseModel):
    """The party to be reimbursed for cost of the products and services according to the terms of the policy.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of recipient
    :param Reference party: Recipient reference
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "party": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        party: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.party = party

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CareTeam(FhirBaseModel):
    """The members of the team who provided the products and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Order of care team
    :param Reference provider: Practitioner or organization
    :param bool responsible: Indicator of the lead practitioner
    :param CodeableConcept role: Function within the team
    :param CodeableConcept specialty: Practitioner or provider specialization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        provider: "Reference" = None,
        responsible: "bool" = None,
        role: "CodeableConcept" = None,
        specialty: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.provider = provider
        self.responsible = responsible
        self.role = role
        self.specialty = specialty

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SupportingInfo(FhirBaseModel):
    """Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param CodeableConcept category: Classification of the supplied information
    :param CodeableConcept code: Type of information
    :param str timingDate: When it occurred
    :param Period timingPeriod: When it occurred
    :param bool valueBoolean: Data to be provided
    :param str valueString: Data to be provided
    :param Quantity valueQuantity: Data to be provided
    :param Attachment valueAttachment: Data to be provided
    :param Reference valueReference: Data to be provided
    :param Identifier valueIdentifier: Data to be provided
    :param Coding reason: Explanation for the information
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "timingPeriod": {"class_name": "Period", "is_contained": False},
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        "valueReference": {"class_name": "Reference", "is_contained": False},
        "valueIdentifier": {"class_name": "Identifier", "is_contained": False},
        "reason": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        category: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        timingDate: "str" = None,
        timingPeriod: "Period" = None,
        valueBoolean: "bool" = None,
        valueString: "str" = None,
        valueQuantity: "Quantity" = None,
        valueAttachment: "Attachment" = None,
        valueReference: "Reference" = None,
        valueIdentifier: "Identifier" = None,
        reason: "Coding" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.category = category
        self.code = code
        self.timingDate = timingDate
        self.timingPeriod = timingPeriod
        self.valueBoolean = valueBoolean
        self.valueString = valueString
        self.valueQuantity = valueQuantity
        self.valueAttachment = valueAttachment
        self.valueReference = valueReference
        self.valueIdentifier = valueIdentifier
        self.reason = reason

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Diagnosis(FhirBaseModel):
    """Information about diagnoses relevant to the claim items.:param CodeableConcept diagnosisRelatedGroup: Package billing code
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Diagnosis instance identifier
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisReference: Nature of illness or problem
    :param CodeableConcept type: Timing or nature of the diagnosis
    :param CodeableConcept onAdmission: Present on admission
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "diagnosisRelatedGroup": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "diagnosisCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "diagnosisReference": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "onAdmission": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        diagnosisRelatedGroup: "CodeableConcept" = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        diagnosisCodeableConcept: "CodeableConcept" = None,
        diagnosisReference: "Reference" = None,
        type: list["CodeableConcept"] = None,
        onAdmission: "CodeableConcept" = None,
    ):
        self.diagnosisRelatedGroup = diagnosisRelatedGroup
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.diagnosisCodeableConcept = diagnosisCodeableConcept
        self.diagnosisReference = diagnosisReference
        self.type = type or []
        self.onAdmission = onAdmission

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Procedure(FhirBaseModel):
    """Procedures performed on the patient relevant to the billing items with the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Procedure instance identifier
    :param CodeableConcept type: Category of Procedure
    :param str date: When the procedure was performed
    :param CodeableConcept procedureCodeableConcept: Specific clinical procedure
    :param Reference procedureReference: Specific clinical procedure
    :param Reference udi: Unique device identifier
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "procedureCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "procedureReference": {"class_name": "Reference", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        type: list["CodeableConcept"] = None,
        date: "str" = None,
        procedureCodeableConcept: "CodeableConcept" = None,
        procedureReference: "Reference" = None,
        udi: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.type = type or []
        self.date = date
        self.procedureCodeableConcept = procedureCodeableConcept
        self.procedureReference = procedureReference
        self.udi = udi or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Insurance(FhirBaseModel):
    """Financial instruments for reimbursement for the health care products and services specified on the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Coverage to be used for adjudication
    :param Reference coverage: Insurance information
    :param str preAuthRef: Prior authorization reference number
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "coverage": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        focal: "bool" = None,
        coverage: "Reference" = None,
        preAuthRef: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.focal = focal
        self.coverage = coverage
        self.preAuthRef = preAuthRef or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Accident(FhirBaseModel):
    """Details of a accident which resulted in injuries which required the products and services listed in the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When the incident occurred
    :param CodeableConcept type: The nature of the accident
    :param Address locationAddress: Where the event occurred
    :param Reference locationReference: Where the event occurred
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "locationAddress": {"class_name": "Address", "is_contained": False},
        "locationReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        date: "str" = None,
        type: "CodeableConcept" = None,
        locationAddress: "Address" = None,
        locationReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.date = date
        self.type = type
        self.locationAddress = locationAddress
        self.locationReference = locationReference

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BodySite(FhirBaseModel):
    """Physical location where the service is performed or applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference site: Location
    :param CodeableConcept subSite: Sub-location
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "site": {"class_name": "CodeableReference", "is_contained": False},
        "subSite": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        site: list["CodeableReference"] = None,
        subSite: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.site = site or []
        self.subSite = subSite or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ReviewOutcome(FhirBaseModel):
    """The high-level results of the adjudication if adjudication has been performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept decision: Result of the adjudication
    :param CodeableConcept reason: Reason for result of the adjudication
    :param str preAuthRef: Preauthorization reference
    :param Period preAuthPeriod: Preauthorization reference effective period
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "decision": {"class_name": "CodeableConcept", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        "preAuthPeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        decision: "CodeableConcept" = None,
        reason: list["CodeableConcept"] = None,
        preAuthRef: "str" = None,
        preAuthPeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.decision = decision
        self.reason = reason or []
        self.preAuthRef = preAuthRef
        self.preAuthPeriod = preAuthPeriod

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Adjudication(FhirBaseModel):
    """If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this item.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param CodeableConcept reason: Explanation of adjudication outcome
    :param Money amount: Monetary amount
    :param Quantity quantity: Non-monitary value
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        reason: "CodeableConcept" = None,
        amount: "Money" = None,
        quantity: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.reason = reason
        self.amount = amount
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubDetail(FhirBaseModel):
    """Third-tier of goods and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Product or service provided
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param int noteNumber: Applicable note numbers
    :param ReviewOutcome reviewOutcome: Subdetail level adjudication results
    :param Adjudication adjudication: Subdetail level adjudication details
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrServiceEnd": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "tax": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
        "reviewOutcome": {"class_name": "ReviewOutcome", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        traceNumber: list["Identifier"] = None,
        revenue: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        productOrServiceEnd: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        patientPaid: "Money" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        tax: "Money" = None,
        net: "Money" = None,
        udi: list["Reference"] = None,
        noteNumber: list["int"] = None,
        reviewOutcome: "ReviewOutcome" = None,
        adjudication: list["Adjudication"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.traceNumber = traceNumber or []
        self.revenue = revenue
        self.category = category
        self.productOrService = productOrService
        self.productOrServiceEnd = productOrServiceEnd
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.patientPaid = patientPaid
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.tax = tax
        self.net = net
        self.udi = udi or []
        self.noteNumber = noteNumber or []
        self.reviewOutcome = reviewOutcome
        self.adjudication = adjudication or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Detail(FhirBaseModel):
    """Second-tier of goods and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Product or service provided
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param int noteNumber: Applicable note numbers
    :param ReviewOutcome reviewOutcome: Detail level adjudication results
    :param Adjudication adjudication: Detail level adjudication details
    :param SubDetail subDetail: Additional items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrServiceEnd": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "tax": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
        "reviewOutcome": {"class_name": "ReviewOutcome", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "subDetail": {"class_name": "SubDetail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        traceNumber: list["Identifier"] = None,
        revenue: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        productOrServiceEnd: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        patientPaid: "Money" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        tax: "Money" = None,
        net: "Money" = None,
        udi: list["Reference"] = None,
        noteNumber: list["int"] = None,
        reviewOutcome: "ReviewOutcome" = None,
        adjudication: list["Adjudication"] = None,
        subDetail: list["SubDetail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.traceNumber = traceNumber or []
        self.revenue = revenue
        self.category = category
        self.productOrService = productOrService
        self.productOrServiceEnd = productOrServiceEnd
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.patientPaid = patientPaid
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.tax = tax
        self.net = net
        self.udi = udi or []
        self.noteNumber = noteNumber or []
        self.reviewOutcome = reviewOutcome
        self.adjudication = adjudication or []
        self.subDetail = subDetail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Item(FhirBaseModel):
    """A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Item instance identifier
    :param int careTeamSequence: Applicable care team members
    :param int diagnosisSequence: Applicable diagnoses
    :param int procedureSequence: Applicable procedures
    :param int informationSequence: Applicable exception and supporting information
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param Reference request: Request or Referral for Service
    :param CodeableConcept modifier: Product or service billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param Period servicedPeriod: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Address locationAddress: Place of service or where product was supplied
    :param Reference locationReference: Place of service or where product was supplied
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param Reference udi: Unique device identifier
    :param BodySite bodySite: Anatomical location
    :param Reference encounter: Encounters associated with the listed treatments
    :param int noteNumber: Applicable note numbers
    :param ReviewOutcome reviewOutcome: Adjudication results
    :param Adjudication adjudication: Adjudication details
    :param Detail detail: Additional items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrServiceEnd": {"class_name": "CodeableConcept", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "servicedPeriod": {"class_name": "Period", "is_contained": False},
        "locationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "locationAddress": {"class_name": "Address", "is_contained": False},
        "locationReference": {"class_name": "Reference", "is_contained": False},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "tax": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "udi": {"class_name": "Reference", "is_contained": False},
        "bodySite": {"class_name": "BodySite", "is_contained": True},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "reviewOutcome": {"class_name": "ReviewOutcome", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        careTeamSequence: list["int"] = None,
        diagnosisSequence: list["int"] = None,
        procedureSequence: list["int"] = None,
        informationSequence: list["int"] = None,
        traceNumber: list["Identifier"] = None,
        revenue: "CodeableConcept" = None,
        category: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        productOrServiceEnd: "CodeableConcept" = None,
        request: list["Reference"] = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        servicedDate: "str" = None,
        servicedPeriod: "Period" = None,
        locationCodeableConcept: "CodeableConcept" = None,
        locationAddress: "Address" = None,
        locationReference: "Reference" = None,
        patientPaid: "Money" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        tax: "Money" = None,
        net: "Money" = None,
        udi: list["Reference"] = None,
        bodySite: list["BodySite"] = None,
        encounter: list["Reference"] = None,
        noteNumber: list["int"] = None,
        reviewOutcome: "ReviewOutcome" = None,
        adjudication: list["Adjudication"] = None,
        detail: list["Detail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.careTeamSequence = careTeamSequence or []
        self.diagnosisSequence = diagnosisSequence or []
        self.procedureSequence = procedureSequence or []
        self.informationSequence = informationSequence or []
        self.traceNumber = traceNumber or []
        self.revenue = revenue
        self.category = category
        self.productOrService = productOrService
        self.productOrServiceEnd = productOrServiceEnd
        self.request = request or []
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.servicedDate = servicedDate
        self.servicedPeriod = servicedPeriod
        self.locationCodeableConcept = locationCodeableConcept
        self.locationAddress = locationAddress
        self.locationReference = locationReference
        self.patientPaid = patientPaid
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.tax = tax
        self.net = net
        self.udi = udi or []
        self.bodySite = bodySite or []
        self.encounter = encounter or []
        self.noteNumber = noteNumber or []
        self.reviewOutcome = reviewOutcome
        self.adjudication = adjudication or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BodySite(FhirBaseModel):
    """Physical location where the service is performed or applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference site: Location
    :param CodeableConcept subSite: Sub-location
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "site": {"class_name": "CodeableReference", "is_contained": False},
        "subSite": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        site: list["CodeableReference"] = None,
        subSite: list["CodeableConcept"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.site = site or []
        self.subSite = subSite or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubDetail(FhirBaseModel):
    """The third-tier service adjudications for payor added services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param ReviewOutcome reviewOutcome: Additem subdetail level adjudication results
    :param Adjudication adjudication: Added items adjudication
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrServiceEnd": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "tax": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "reviewOutcome": {"class_name": "ReviewOutcome", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        traceNumber: list["Identifier"] = None,
        revenue: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        productOrServiceEnd: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        patientPaid: "Money" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        tax: "Money" = None,
        net: "Money" = None,
        noteNumber: list["int"] = None,
        reviewOutcome: "ReviewOutcome" = None,
        adjudication: list["Adjudication"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.traceNumber = traceNumber or []
        self.revenue = revenue
        self.productOrService = productOrService
        self.productOrServiceEnd = productOrServiceEnd
        self.modifier = modifier or []
        self.patientPaid = patientPaid
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.tax = tax
        self.net = net
        self.noteNumber = noteNumber or []
        self.reviewOutcome = reviewOutcome
        self.adjudication = adjudication or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Detail(FhirBaseModel):
    """The second-tier service adjudications for payor added services.:param int detailSequence: Detail sequence number
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier traceNumber: Number for tracking
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param int noteNumber: Applicable note numbers
    :param ReviewOutcome reviewOutcome: Additem detail level adjudication results
    :param Adjudication adjudication: Added items adjudication
    :param SubDetail subDetail: Insurer added line items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrServiceEnd": {"class_name": "CodeableConcept", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "tax": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "reviewOutcome": {"class_name": "ReviewOutcome", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "subDetail": {"class_name": "SubDetail", "is_contained": True},
    }

    def __init__(
        self,
        detailSequence: list["int"] = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        traceNumber: list["Identifier"] = None,
        revenue: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        productOrServiceEnd: "CodeableConcept" = None,
        modifier: list["CodeableConcept"] = None,
        patientPaid: "Money" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        tax: "Money" = None,
        net: "Money" = None,
        noteNumber: list["int"] = None,
        reviewOutcome: "ReviewOutcome" = None,
        adjudication: list["Adjudication"] = None,
        subDetail: list["SubDetail"] = None,
    ):
        self.detailSequence = detailSequence or []
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.traceNumber = traceNumber or []
        self.revenue = revenue
        self.productOrService = productOrService
        self.productOrServiceEnd = productOrServiceEnd
        self.modifier = modifier or []
        self.patientPaid = patientPaid
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.tax = tax
        self.net = net
        self.noteNumber = noteNumber or []
        self.reviewOutcome = reviewOutcome
        self.adjudication = adjudication or []
        self.subDetail = subDetail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AddItem(FhirBaseModel):
    """The first-tier service adjudications for payor added product or service lines.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int itemSequence: Item sequence number
    :param int detailSequence: Detail sequence number
    :param int subDetailSequence: Subdetail sequence number
    :param Identifier traceNumber: Number for tracking
    :param Reference provider: Authorized providers
    :param CodeableConcept revenue: Revenue or cost center code
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept productOrServiceEnd: End of a range of codes
    :param Reference request: Request or Referral for Service
    :param CodeableConcept modifier: Service/Product billing modifiers
    :param CodeableConcept programCode: Program the product or service is provided under
    :param str servicedDate: Date or dates of service or product delivery
    :param Period servicedPeriod: Date or dates of service or product delivery
    :param CodeableConcept locationCodeableConcept: Place of service or where product was supplied
    :param Address locationAddress: Place of service or where product was supplied
    :param Reference locationReference: Place of service or where product was supplied
    :param Money patientPaid: Paid by the patient
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param float factor: Price scaling factor
    :param Money tax: Total tax
    :param Money net: Total item cost
    :param BodySite bodySite: Anatomical location
    :param int noteNumber: Applicable note numbers
    :param ReviewOutcome reviewOutcome: Additem level adjudication results
    :param Adjudication adjudication: Added items adjudication
    :param Detail detail: Insurer added line items
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "revenue": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrService": {"class_name": "CodeableConcept", "is_contained": False},
        "productOrServiceEnd": {"class_name": "CodeableConcept", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "modifier": {"class_name": "CodeableConcept", "is_contained": False},
        "programCode": {"class_name": "CodeableConcept", "is_contained": False},
        "servicedPeriod": {"class_name": "Period", "is_contained": False},
        "locationCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "locationAddress": {"class_name": "Address", "is_contained": False},
        "locationReference": {"class_name": "Reference", "is_contained": False},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "unitPrice": {"class_name": "Money", "is_contained": False},
        "tax": {"class_name": "Money", "is_contained": False},
        "net": {"class_name": "Money", "is_contained": False},
        "bodySite": {"class_name": "BodySite", "is_contained": True},
        "reviewOutcome": {"class_name": "ReviewOutcome", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "detail": {"class_name": "Detail", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        itemSequence: list["int"] = None,
        detailSequence: list["int"] = None,
        subDetailSequence: list["int"] = None,
        traceNumber: list["Identifier"] = None,
        provider: list["Reference"] = None,
        revenue: "CodeableConcept" = None,
        productOrService: "CodeableConcept" = None,
        productOrServiceEnd: "CodeableConcept" = None,
        request: list["Reference"] = None,
        modifier: list["CodeableConcept"] = None,
        programCode: list["CodeableConcept"] = None,
        servicedDate: "str" = None,
        servicedPeriod: "Period" = None,
        locationCodeableConcept: "CodeableConcept" = None,
        locationAddress: "Address" = None,
        locationReference: "Reference" = None,
        patientPaid: "Money" = None,
        quantity: "Quantity" = None,
        unitPrice: "Money" = None,
        factor: "float" = None,
        tax: "Money" = None,
        net: "Money" = None,
        bodySite: list["BodySite"] = None,
        noteNumber: list["int"] = None,
        reviewOutcome: "ReviewOutcome" = None,
        adjudication: list["Adjudication"] = None,
        detail: list["Detail"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemSequence = itemSequence or []
        self.detailSequence = detailSequence or []
        self.subDetailSequence = subDetailSequence or []
        self.traceNumber = traceNumber or []
        self.provider = provider or []
        self.revenue = revenue
        self.productOrService = productOrService
        self.productOrServiceEnd = productOrServiceEnd
        self.request = request or []
        self.modifier = modifier or []
        self.programCode = programCode or []
        self.servicedDate = servicedDate
        self.servicedPeriod = servicedPeriod
        self.locationCodeableConcept = locationCodeableConcept
        self.locationAddress = locationAddress
        self.locationReference = locationReference
        self.patientPaid = patientPaid
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.factor = factor
        self.tax = tax
        self.net = net
        self.bodySite = bodySite or []
        self.noteNumber = noteNumber or []
        self.reviewOutcome = reviewOutcome
        self.adjudication = adjudication or []
        self.detail = detail or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Total(FhirBaseModel):
    """Categorized monetary totals for the adjudication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Type of adjudication information
    :param Money amount: Financial total for the category
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        amount: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Payment(FhirBaseModel):
    """Payment details for the adjudication of the claim.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Partial or complete payment
    :param Money adjustment: Payment adjustment for non-claim issues
    :param CodeableConcept adjustmentReason: Explanation for the variance
    :param str date: Expected date of payment
    :param Money amount: Payable amount after adjustment
    :param Identifier identifier: Business identifier for the payment
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "adjustment": {"class_name": "Money", "is_contained": False},
        "adjustmentReason": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Money", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        adjustment: "Money" = None,
        adjustmentReason: "CodeableConcept" = None,
        date: "str" = None,
        amount: "Money" = None,
        identifier: "Identifier" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.adjustment = adjustment
        self.adjustmentReason = adjustmentReason
        self.date = date
        self.amount = amount
        self.identifier = identifier

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ProcessNote(FhirBaseModel):
    """A note that describes or explains adjudication results in a human readable form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int number: Note instance identifier
    :param CodeableConcept type: Note purpose
    :param str text: Note explanatory text
    :param CodeableConcept language: Language of the text
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
        number: "int" = None,
        type: "CodeableConcept" = None,
        text: "str" = None,
        language: "CodeableConcept" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.number = number
        self.type = type
        self.text = text
        self.language = language

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Financial(FhirBaseModel):
    """Benefits Used to date.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedUnsignedInt: Benefits allowed
    :param str allowedString: Benefits allowed
    :param Money allowedMoney: Benefits allowed
    :param int usedUnsignedInt: Benefits used
    :param Money usedMoney: Benefits used
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "allowedMoney": {"class_name": "Money", "is_contained": False},
        "usedMoney": {"class_name": "Money", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        allowedUnsignedInt: "int" = None,
        allowedString: "str" = None,
        allowedMoney: "Money" = None,
        usedUnsignedInt: "int" = None,
        usedMoney: "Money" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.allowedUnsignedInt = allowedUnsignedInt
        self.allowedString = allowedString
        self.allowedMoney = allowedMoney
        self.usedUnsignedInt = usedUnsignedInt
        self.usedMoney = usedMoney

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BenefitBalance(FhirBaseModel):
    """Balance by Benefit Category.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Benefit classification
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param Financial financial: Benefit Summary
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "network": {"class_name": "CodeableConcept", "is_contained": False},
        "unit": {"class_name": "CodeableConcept", "is_contained": False},
        "term": {"class_name": "CodeableConcept", "is_contained": False},
        "financial": {"class_name": "Financial", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        excluded: "bool" = None,
        name: "str" = None,
        description: "str" = None,
        network: "CodeableConcept" = None,
        unit: "CodeableConcept" = None,
        term: "CodeableConcept" = None,
        financial: list["Financial"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.excluded = excluded
        self.name = name
        self.description = description
        self.network = network
        self.unit = unit
        self.term = term
        self.financial = financial or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ExplanationOfBenefit(DomainResource):
    """This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the resource
    :param Identifier traceNumber: Number for tracking
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: Category or discipline
    :param CodeableConcept subType: More granular claim type
    :param str use: claim | preauthorization | predetermination
    :param Reference patient: The recipient of the products and services
    :param Period billablePeriod: Relevant time frame for the claim
    :param str created: Response creation date
    :param Reference enterer: Author of the claim
    :param Reference insurer: Party responsible for reimbursement
    :param Reference provider: Party responsible for the claim
    :param CodeableConcept priority: Desired processing urgency
    :param CodeableConcept fundsReserveRequested: For whom to reserve funds
    :param CodeableConcept fundsReserve: Funds reserved status
    :param Related related: Prior or corollary claims
    :param Reference prescription: Prescription authorizing services or products
    :param Reference originalPrescription: Original prescription if superceded by fulfiller
    :param Event event: Event information
    :param Payee payee: Recipient of benefits payable
    :param Reference referral: Treatment Referral
    :param Reference encounter: Encounters associated with the listed treatments
    :param Reference facility: Servicing Facility
    :param Reference claim: Claim reference
    :param Reference claimResponse: Claim response reference
    :param str outcome: queued | complete | error | partial
    :param CodeableConcept decision: Result of the adjudication
    :param str disposition: Disposition Message
    :param str preAuthRef: Preauthorization reference
    :param Period preAuthRefPeriod: Preauthorization in-effect period
    :param CodeableConcept diagnosisRelatedGroup: Package billing code
    :param CareTeam careTeam: Care Team members
    :param SupportingInfo supportingInfo: Supporting information
    :param Diagnosis diagnosis: Pertinent diagnosis information
    :param Procedure procedure: Clinical procedures performed
    :param int precedence: Precedence (primary, secondary, etc.)
    :param Insurance insurance: Patient insurance information
    :param Accident accident: Details of the event
    :param Money patientPaid: Paid by the patient
    :param Item item: Product or service provided
    :param AddItem addItem: Insurer added line items
    :param Adjudication adjudication: Header-level adjudication
    :param Total total: Adjudication totals
    :param Payment payment: Payment Details
    :param CodeableConcept formCode: Printed form identifier
    :param Attachment form: Printed reference or actual form
    :param ProcessNote processNote: Note concerning adjudication
    :param Period benefitPeriod: When the benefits are applicable
    :param BenefitBalance benefitBalance: Balance by Benefit Category
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "traceNumber": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subType": {"class_name": "CodeableConcept", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "billablePeriod": {"class_name": "Period", "is_contained": False},
        "enterer": {"class_name": "Reference", "is_contained": False},
        "insurer": {"class_name": "Reference", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        "fundsReserveRequested": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "fundsReserve": {"class_name": "CodeableConcept", "is_contained": False},
        "related": {"class_name": "Related", "is_contained": True},
        "prescription": {"class_name": "Reference", "is_contained": False},
        "originalPrescription": {"class_name": "Reference", "is_contained": False},
        "event": {"class_name": "Event", "is_contained": True},
        "payee": {"class_name": "Payee", "is_contained": True},
        "referral": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "facility": {"class_name": "Reference", "is_contained": False},
        "claim": {"class_name": "Reference", "is_contained": False},
        "claimResponse": {"class_name": "Reference", "is_contained": False},
        "decision": {"class_name": "CodeableConcept", "is_contained": False},
        "preAuthRefPeriod": {"class_name": "Period", "is_contained": False},
        "diagnosisRelatedGroup": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "careTeam": {"class_name": "CareTeam", "is_contained": True},
        "supportingInfo": {"class_name": "SupportingInfo", "is_contained": True},
        "diagnosis": {"class_name": "Diagnosis", "is_contained": True},
        "procedure": {"class_name": "Procedure", "is_contained": True},
        "insurance": {"class_name": "Insurance", "is_contained": True},
        "accident": {"class_name": "Accident", "is_contained": True},
        "patientPaid": {"class_name": "Money", "is_contained": False},
        "item": {"class_name": "Item", "is_contained": True},
        "addItem": {"class_name": "AddItem", "is_contained": True},
        "adjudication": {"class_name": "Adjudication", "is_contained": True},
        "total": {"class_name": "Total", "is_contained": True},
        "payment": {"class_name": "Payment", "is_contained": True},
        "formCode": {"class_name": "CodeableConcept", "is_contained": False},
        "form": {"class_name": "Attachment", "is_contained": False},
        "processNote": {"class_name": "ProcessNote", "is_contained": True},
        "benefitPeriod": {"class_name": "Period", "is_contained": False},
        "benefitBalance": {"class_name": "BenefitBalance", "is_contained": True},
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
        traceNumber: list["Identifier"] = None,
        status: "str" = None,
        type: "CodeableConcept" = None,
        subType: "CodeableConcept" = None,
        use: "str" = None,
        patient: "Reference" = None,
        billablePeriod: "Period" = None,
        created: "str" = None,
        enterer: "Reference" = None,
        insurer: "Reference" = None,
        provider: "Reference" = None,
        priority: "CodeableConcept" = None,
        fundsReserveRequested: "CodeableConcept" = None,
        fundsReserve: "CodeableConcept" = None,
        related: list["Related"] = None,
        prescription: "Reference" = None,
        originalPrescription: "Reference" = None,
        event: list["Event"] = None,
        payee: "Payee" = None,
        referral: "Reference" = None,
        encounter: list["Reference"] = None,
        facility: "Reference" = None,
        claim: "Reference" = None,
        claimResponse: "Reference" = None,
        outcome: "str" = None,
        decision: "CodeableConcept" = None,
        disposition: "str" = None,
        preAuthRef: list["str"] = None,
        preAuthRefPeriod: list["Period"] = None,
        diagnosisRelatedGroup: "CodeableConcept" = None,
        careTeam: list["CareTeam"] = None,
        supportingInfo: list["SupportingInfo"] = None,
        diagnosis: list["Diagnosis"] = None,
        procedure: list["Procedure"] = None,
        precedence: "int" = None,
        insurance: list["Insurance"] = None,
        accident: "Accident" = None,
        patientPaid: "Money" = None,
        item: list["Item"] = None,
        addItem: list["AddItem"] = None,
        adjudication: list["Adjudication"] = None,
        total: list["Total"] = None,
        payment: "Payment" = None,
        formCode: "CodeableConcept" = None,
        form: "Attachment" = None,
        processNote: list["ProcessNote"] = None,
        benefitPeriod: "Period" = None,
        benefitBalance: list["BenefitBalance"] = None,
    ):

        self.resourceType = "ExplanationOfBenefit"

        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.traceNumber = traceNumber or []
        self.status = status
        self.type = type
        self.subType = subType
        self.use = use
        self.patient = patient
        self.billablePeriod = billablePeriod
        self.created = created
        self.enterer = enterer
        self.insurer = insurer
        self.provider = provider
        self.priority = priority
        self.fundsReserveRequested = fundsReserveRequested
        self.fundsReserve = fundsReserve
        self.related = related or []
        self.prescription = prescription
        self.originalPrescription = originalPrescription
        self.event = event or []
        self.payee = payee
        self.referral = referral
        self.encounter = encounter or []
        self.facility = facility
        self.claim = claim
        self.claimResponse = claimResponse
        self.outcome = outcome
        self.decision = decision
        self.disposition = disposition
        self.preAuthRef = preAuthRef or []
        self.preAuthRefPeriod = preAuthRefPeriod or []
        self.diagnosisRelatedGroup = diagnosisRelatedGroup
        self.careTeam = careTeam or []
        self.supportingInfo = supportingInfo or []
        self.diagnosis = diagnosis or []
        self.procedure = procedure or []
        self.precedence = precedence
        self.insurance = insurance or []
        self.accident = accident
        self.patientPaid = patientPaid
        self.item = item or []
        self.addItem = addItem or []
        self.adjudication = adjudication or []
        self.total = total or []
        self.payment = payment
        self.formCode = formCode
        self.form = form
        self.processNote = processNote or []
        self.benefitPeriod = benefitPeriod
        self.benefitBalance = benefitBalance or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExplanationOfBenefit":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExplanationOfBenefit":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

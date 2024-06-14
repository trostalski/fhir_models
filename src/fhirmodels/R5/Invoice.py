"""
Generated class for Invoice. 
Time: 2024-06-14 18:37:55
"""

from fhirmodels.R5.Annotation import *
from fhirmodels.R5.BackboneElement import *
from fhirmodels.R5.CodeableConcept import *
from fhirmodels.R5.DomainResource import *
from fhirmodels.R5.Extension import *
from fhirmodels.R5.Identifier import *
from fhirmodels.R5.Meta import *
from fhirmodels.R5.MonetaryComponent import *
from fhirmodels.R5.Money import *
from fhirmodels.R5.Narrative import *
from fhirmodels.R5.Period import *
from fhirmodels.R5.Reference import *
from fhirmodels.R5.Resource import *


class Participant(FhirBaseModel):
    """Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement in creation of this Invoice
    :param Reference actor: Individual who was involved
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        role: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class LineItem(FhirBaseModel):
    """Each line item represents one charge for goods and services rendered. Details such.ofType(date), code and amount are found in the referenced ChargeItem resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence number of line item
    :param str servicedDate: Service data or period
    :param Period servicedPeriod: Service data or period
    :param Reference chargeItemReference: Reference to ChargeItem containing details of this line item or an inline billing code
    :param CodeableConcept chargeItemCodeableConcept: Reference to ChargeItem containing details of this line item or an inline billing code
    :param MonetaryComponent priceComponent: Components of total line item price
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "servicedPeriod": {"class_name": "Period", "is_contained": False},
        "chargeItemReference": {"class_name": "Reference", "is_contained": False},
        "chargeItemCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "priceComponent": {"class_name": "MonetaryComponent", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        sequence: "int" = None,
        servicedDate: "str" = None,
        servicedPeriod: "Period" = None,
        chargeItemReference: "Reference" = None,
        chargeItemCodeableConcept: "CodeableConcept" = None,
        priceComponent: list["MonetaryComponent"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence
        self.servicedDate = servicedDate
        self.servicedPeriod = servicedPeriod
        self.chargeItemReference = chargeItemReference
        self.chargeItemCodeableConcept = chargeItemCodeableConcept
        self.priceComponent = priceComponent or []

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Invoice(DomainResource):
    """Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for item
    :param str status: draft | issued | balanced | cancelled | entered-in-error
    :param str cancelledReason: Reason for cancellation of this Invoice
    :param CodeableConcept type: Type of Invoice
    :param Reference subject: Recipient(s) of goods and services
    :param Reference recipient: Recipient of this invoice
    :param str date: DEPRICATED
    :param str creation: When posted
    :param str periodDate: Billing date or period
    :param Period periodPeriod: Billing date or period
    :param Participant participant: Participant in creation of this Invoice
    :param Reference issuer: Issuing Organization of Invoice
    :param Reference account: Account that is being balanced
    :param LineItem lineItem: Line items of this Invoice
    :param MonetaryComponent totalPriceComponent: Components of Invoice total
    :param Money totalNet: Net total of this Invoice
    :param Money totalGross: Gross total of this Invoice
    :param str paymentTerms: Payment details
    :param Annotation note: Comments made about the invoice
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "recipient": {"class_name": "Reference", "is_contained": False},
        "periodPeriod": {"class_name": "Period", "is_contained": False},
        "participant": {"class_name": "Participant", "is_contained": True},
        "issuer": {"class_name": "Reference", "is_contained": False},
        "account": {"class_name": "Reference", "is_contained": False},
        "lineItem": {"class_name": "LineItem", "is_contained": True},
        "totalPriceComponent": {
            "class_name": "MonetaryComponent",
            "is_contained": False,
        },
        "totalNet": {"class_name": "Money", "is_contained": False},
        "totalGross": {"class_name": "Money", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
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
        cancelledReason: "str" = None,
        type: "CodeableConcept" = None,
        subject: "Reference" = None,
        recipient: "Reference" = None,
        date: "str" = None,
        creation: "str" = None,
        periodDate: "str" = None,
        periodPeriod: "Period" = None,
        participant: list["Participant"] = None,
        issuer: "Reference" = None,
        account: "Reference" = None,
        lineItem: list["LineItem"] = None,
        totalPriceComponent: list["MonetaryComponent"] = None,
        totalNet: "Money" = None,
        totalGross: "Money" = None,
        paymentTerms: "str" = None,
        note: list["Annotation"] = None,
    ):

        self.resourceType = "Invoice"

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
        self.cancelledReason = cancelledReason
        self.type = type
        self.subject = subject
        self.recipient = recipient
        self.date = date
        self.creation = creation
        self.periodDate = periodDate
        self.periodPeriod = periodPeriod
        self.participant = participant or []
        self.issuer = issuer
        self.account = account
        self.lineItem = lineItem or []
        self.totalPriceComponent = totalPriceComponent or []
        self.totalNet = totalNet
        self.totalGross = totalGross
        self.paymentTerms = paymentTerms
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Invoice":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

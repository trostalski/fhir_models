"""
Generated class for ProductShelfLife. 
Time: 2024-06-14 18:56:04
"""
from fhirmodels.fhir_base_model import FhirBaseModel
from fhirmodels.R5.CodeableConcept import *
from fhirmodels.R5.Duration import *
from fhirmodels.R5.Extension import *


class ProductShelfLife(FhirBaseModel):
    """ ProductShelfLife Type: The shelf-life and storage information for a medicinal product item or container can be described using this class.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: This describes the shelf life, taking into account various scenarios such as shelf life of the packaged Medicinal Product itself, shelf life after transformation where necessary and shelf life after the first opening of a bottle, etc. The shelf life type shall be specified using an appropriate controlled vocabulary The controlled term and the controlled term identifier shall be specified
    :param Duration periodDuration: The shelf life time period can be specified using a numerical value for the period of time and its unit of time measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param str periodString: The shelf life time period can be specified using a numerical value for the period of time and its unit of time measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used
    :param CodeableConcept specialPrecautionsForStorage: Special precautions for storage, if any, can be specified using an appropriate controlled vocabulary The controlled term and the controlled term identifier shall be specified
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "periodDuration": {"class_name": "Duration", "is_contained": False},
        
        
        
        "specialPrecautionsForStorage": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  periodDuration:  'Duration'  = None,  periodString:  'str'  = None,  specialPrecautionsForStorage:  list['CodeableConcept']  = None, ):
        
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.periodDuration = periodDuration 
        self.periodString = periodString 
        self.specialPrecautionsForStorage = specialPrecautionsForStorage or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ProductShelfLife":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ProductShelfLife":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:69d946a4-00bc-11e6-8359-6c40088fdb3a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://example.org/ns#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 54, 16)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://example.org/ns#}BigChoice
class BigChoice (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """A choice amongst integers"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BigChoice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 71, 4)
    _Documentation = 'A choice amongst integers'
BigChoice._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BigChoice, enum_prefix=None)
BigChoice._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
BigChoice._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
BigChoice._CF_enumeration.addEnumeration(unicode_value='42', tag=None)
BigChoice._InitializeFacetMap(BigChoice._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BigChoice', BigChoice)
_module_typeBindings.BigChoice = BigChoice

# Complex type {http://example.org/ns#}BareComplexType with content type EMPTY
class BareComplexType (pyxb.binding.basis.complexTypeDefinition):
    """A bare complex type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BareComplexType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BareComplexType = BareComplexType
Namespace.addCategoryObject('typeBinding', 'BareComplexType', BareComplexType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """An element with some structure"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 27, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://example.org/ns#}BareElement uses Python identifier BareElement
    __BareElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BareElement'), 'BareElement', '__httpexample_orgns_CTD_ANON_httpexample_orgnsBareElement', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 5, 4), 0, None, )

    
    BareElement = property(__BareElement.value, __BareElement.set, None, 'A bare element')

    
    # Element {http://example.org/ns#}subElement1 uses Python identifier subElement1
    __subElement1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subElement1'), 'subElement1', '__httpexample_orgns_CTD_ANON_httpexample_orgnssubElement1', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 29, 16), 1, 1, )

    
    subElement1 = property(__subElement1.value, __subElement1.set, None, 'StructuredElement.subElement1 is bare')

    
    # Attribute {http://example.org/ns#}BareAttribute uses Python identifier BareAttribute
    __BareAttribute = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'BareAttribute'), 'BareAttribute', '__httpexample_orgns_CTD_ANON_httpexample_orgnsBareAttribute', pyxb.binding.datatypes.anySimpleType, required=True)
    __BareAttribute._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 17, 4)
    __BareAttribute._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 58, 12)
    
    BareAttribute = property(__BareAttribute.value, __BareAttribute.set, None, 'A bare attribute')

    
    # Attribute at1Bare uses Python identifier at1Bare
    __at1Bare = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'at1Bare'), 'at1Bare', '__httpexample_orgns_CTD_ANON_at1Bare', pyxb.binding.datatypes.anySimpleType)
    __at1Bare._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 40, 12)
    __at1Bare._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 40, 12)
    
    at1Bare = property(__at1Bare.value, __at1Bare.set, None, 'StructuredElement.at1Bare is an optional bare')

    
    # Attribute at2Double uses Python identifier at2Double
    __at2Double = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'at2Double'), 'at2Double', '__httpexample_orgns_CTD_ANON_at2Double', pyxb.binding.datatypes.double)
    __at2Double._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 45, 12)
    __at2Double._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 45, 12)
    
    at2Double = property(__at2Double.value, __at2Double.set, None, 'StructuredElement.at2Double is an optional double')

    
    # Attribute at3RestrictedDouble uses Python identifier at3RestrictedDouble
    __at3RestrictedDouble = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'at3RestrictedDouble'), 'at3RestrictedDouble', '__httpexample_orgns_CTD_ANON_at3RestrictedDouble', _module_typeBindings.STD_ANON)
    __at3RestrictedDouble._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 50, 12)
    __at3RestrictedDouble._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 50, 12)
    
    at3RestrictedDouble = property(__at3RestrictedDouble.value, __at3RestrictedDouble.set, None, 'StructuredElement.at3RestrictedDouble is an optional restricted Double')

    
    # Attribute FancyAttribute uses Python identifier FancyAttribute
    __FancyAttribute = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'FancyAttribute'), 'FancyAttribute', '__httpexample_orgns_CTD_ANON_FancyAttribute', _module_typeBindings.BigChoice, prohibited=True)
    __FancyAttribute._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 63, 12)
    __FancyAttribute._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 63, 12)
    
    FancyAttribute = property(__FancyAttribute.value, __FancyAttribute.set, None, 'StructuredElement.BigChoice is a prohipited BigChoice')

    _ElementMap.update({
        __BareElement.name() : __BareElement,
        __subElement1.name() : __subElement1
    })
    _AttributeMap.update({
        __BareAttribute.name() : __BareAttribute,
        __at1Bare.name() : __at1Bare,
        __at2Double.name() : __at2Double,
        __at3RestrictedDouble.name() : __at3RestrictedDouble,
        __FancyAttribute.name() : __FancyAttribute
    })
_module_typeBindings.CTD_ANON = CTD_ANON


BareElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BareElement'), pyxb.binding.datatypes.anyType, documentation='A bare element', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', BareElement.name().localName(), BareElement)

StructuredElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StructuredElement'), CTD_ANON, documentation='An element with some structure', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 23, 4))
Namespace.addCategoryObject('elementBinding', StructuredElement.name().localName(), StructuredElement)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BareElement'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, documentation='A bare element', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 5, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subElement1'), BareComplexType, scope=CTD_ANON, documentation='StructuredElement.subElement1 is bare', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 29, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 34, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subElement1')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 29, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BareElement')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/elements.xsd', 34, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()


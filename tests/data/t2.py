
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:69cdac54-00bc-11e6-8ca7-6c40088fdb3a')

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
Namespace = pyxb.namespace.NamespaceForURI('http://ncbi.nlm.nih.gov/gap/mms#', create_if_missing=True)
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


# Atomic simple type: {http://ncbi.nlm.nih.gov/gap/mms#}ST1
class ST1 (pyxb.binding.datatypes.string):

    """Simple type 1"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ST1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 55, 4)
    _Documentation = 'Simple type 1'
ST1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ST1', ST1)
_module_typeBindings.ST1 = ST1

# Complex type {http://ncbi.nlm.nih.gov/gap/mms#}CT1 with content type EMPTY
class CT1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex Type 1"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CT1')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CT1 = CT1
Namespace.addCategoryObject('typeBinding', 'CT1', CT1)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """ElementWrapper 3"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 20, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ncbi.nlm.nih.gov/gap/mms#}E1 uses Python identifier E1
    __E1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'E1'), 'E1', '__httpncbi_nlm_nih_govgapmms_CTD_ANON_httpncbi_nlm_nih_govgapmmsE1', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 22, 16), 1, 1, )

    
    E1 = property(__E1.value, __E1.set, None, None)

    
    # Attribute A1 uses Python identifier A1
    __A1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'A1'), 'A1', '__httpncbi_nlm_nih_govgapmms_CTD_ANON_A1', pyxb.binding.datatypes.anySimpleType)
    __A1._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 24, 12)
    __A1._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 24, 12)
    
    A1 = property(__A1.value, __A1.set, None, None)

    _ElementMap.update({
        __E1.name() : __E1
    })
    _AttributeMap.update({
        __A1.name() : __A1
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """ElementWrapper 2"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 32, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ncbi.nlm.nih.gov/gap/mms#}E1 uses Python identifier E1
    __E1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'E1'), 'E1', '__httpncbi_nlm_nih_govgapmms_CTD_ANON__httpncbi_nlm_nih_govgapmmsE1', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 34, 16), 0, None, )

    
    E1 = property(__E1.value, __E1.set, None, 'ElementWrapper 2 ElementWrapper 1 Complex Type 2')

    
    # Attribute A1 uses Python identifier A1
    __A1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'A1'), 'A1', '__httpncbi_nlm_nih_govgapmms_CTD_ANON__A1', pyxb.binding.datatypes.date)
    __A1._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 40, 12)
    __A1._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 40, 12)
    
    A1 = property(__A1.value, __A1.set, None, 'ElementWrapper 2 Attribute 1 Date')

    _ElementMap.update({
        __E1.name() : __E1
    })
    _AttributeMap.update({
        __A1.name() : __A1
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://ncbi.nlm.nih.gov/gap/mms#}CT2 with content type ELEMENT_ONLY
class CT2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex Type 2"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CT2')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 66, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ncbi.nlm.nih.gov/gap/mms#}E1 uses Python identifier E1
    __E1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'E1'), 'E1', '__httpncbi_nlm_nih_govgapmms_CT2_httpncbi_nlm_nih_govgapmmsE1', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 10, 4), 1, 1, )

    
    E1 = property(__E1.value, __E1.set, None, 'ElementWrapper 1')

    
    # Element {http://ncbi.nlm.nih.gov/gap/mms#}E3 uses Python identifier E3
    __E3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'E3'), 'E3', '__httpncbi_nlm_nih_govgapmms_CT2_httpncbi_nlm_nih_govgapmmsE3', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 71, 12), 1, 1, )

    
    E3 = property(__E3.value, __E3.set, None, 'Complex Type 2 ElementWrapper 3 (No type)')

    
    # Element {http://ncbi.nlm.nih.gov/gap/mms#}E2 uses Python identifier E2
    __E2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'E2'), 'E2', '__httpncbi_nlm_nih_govgapmms_CT2_httpncbi_nlm_nih_govgapmmsE2', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 76, 12), 1, 1, )

    
    E2 = property(__E2.value, __E2.set, None, 'Complex Type 2 ElementWrapper 2 (CT1)')

    
    # Attribute {http://ncbi.nlm.nih.gov/gap/mms#}A1 uses Python identifier A1
    __A1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'A1'), 'A1', '__httpncbi_nlm_nih_govgapmms_CT2_httpncbi_nlm_nih_govgapmmsA1', pyxb.binding.datatypes.anySimpleType)
    __A1._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 49, 4)
    __A1._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 87, 8)
    
    A1 = property(__A1.value, __A1.set, None, 'Attribute 1')

    
    # Attribute A2 uses Python identifier A2
    __A2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'A2'), 'A2', '__httpncbi_nlm_nih_govgapmms_CT2_A2', pyxb.binding.datatypes.double)
    __A2._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 92, 8)
    __A2._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 92, 8)
    
    A2 = property(__A2.value, __A2.set, None, 'Complex Type 2 Attribute 2 (double)')

    
    # Attribute A3 uses Python identifier A3
    __A3 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'A3'), 'A3', '__httpncbi_nlm_nih_govgapmms_CT2_A3', pyxb.binding.datatypes.anySimpleType)
    __A3._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 97, 8)
    __A3._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 97, 8)
    
    A3 = property(__A3.value, __A3.set, None, 'Complex Type 2 Attribute 3 (No Type)')

    
    # Attribute A4 uses Python identifier A4
    __A4 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'A4'), 'A4', '__httpncbi_nlm_nih_govgapmms_CT2_A4', _module_typeBindings.ST1)
    __A4._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 102, 8)
    __A4._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 102, 8)
    
    A4 = property(__A4.value, __A4.set, None, 'Complex Type 2 Attribute 4 (ST1)')

    _ElementMap.update({
        __E1.name() : __E1,
        __E3.name() : __E3,
        __E2.name() : __E2
    })
    _AttributeMap.update({
        __A1.name() : __A1,
        __A2.name() : __A2,
        __A3.name() : __A3,
        __A4.name() : __A4
    })
_module_typeBindings.CT2 = CT2
Namespace.addCategoryObject('typeBinding', 'CT2', CT2)


E1 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E1'), pyxb.binding.datatypes.anyType, documentation='ElementWrapper 1', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 10, 4))
Namespace.addCategoryObject('elementBinding', E1.name().localName(), E1)

E3 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E3'), CTD_ANON, documentation='ElementWrapper 3', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 16, 4))
Namespace.addCategoryObject('elementBinding', E3.name().localName(), E3)

E2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E2'), CTD_ANON_, documentation='ElementWrapper 2', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 28, 4))
Namespace.addCategoryObject('elementBinding', E2.name().localName(), E2)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E1'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 22, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'E1')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 22, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E1'), CT2, scope=CTD_ANON_, documentation='ElementWrapper 2 ElementWrapper 1 Complex Type 2', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 34, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 34, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'E1')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 34, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CT2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E1'), pyxb.binding.datatypes.anyType, scope=CT2, documentation='ElementWrapper 1', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 10, 4)))

CT2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E3'), pyxb.binding.datatypes.anyType, scope=CT2, documentation='Complex Type 2 ElementWrapper 3 (No type)', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 71, 12)))

CT2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E2'), CT1, scope=CT2, documentation='Complex Type 2 ElementWrapper 2 (CT1)', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 76, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CT2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'E3')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 71, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CT2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'E2')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 76, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CT2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'E1')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t2.xsd', 81, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CT2._Automaton = _BuildAutomaton_2()


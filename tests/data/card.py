
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:69d5f762-00bc-11e6-8b4a-6c40088fdb3a')

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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 5, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://example.org/ns#}opt uses Python identifier opt
    __opt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'opt'), 'opt', '__httpexample_orgns_CTD_ANON_httpexample_orgnsopt', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 7, 16), 0, 1, )

    
    opt = property(__opt.value, __opt.set, None, None)

    
    # Element {http://example.org/ns#}req uses Python identifier req
    __req = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'req'), 'req', '__httpexample_orgns_CTD_ANON_httpexample_orgnsreq', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 8, 16), 1, 1, )

    
    req = property(__req.value, __req.set, None, None)

    
    # Element {http://example.org/ns#}zeroton uses Python identifier zeroton
    __zeroton = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zeroton'), 'zeroton', '__httpexample_orgns_CTD_ANON_httpexample_orgnszeroton', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 9, 16), 0, 2, )

    
    zeroton = property(__zeroton.value, __zeroton.set, None, None)

    
    # Element {http://example.org/ns#}oneton uses Python identifier oneton
    __oneton = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oneton'), 'oneton', '__httpexample_orgns_CTD_ANON_httpexample_orgnsoneton', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 10, 16), 1, 3, )

    
    oneton = property(__oneton.value, __oneton.set, None, None)

    
    # Element {http://example.org/ns#}minzero uses Python identifier minzero
    __minzero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minzero'), 'minzero', '__httpexample_orgns_CTD_ANON_httpexample_orgnsminzero', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 11, 16), 0, None, )

    
    minzero = property(__minzero.value, __minzero.set, None, None)

    
    # Element {http://example.org/ns#}minone uses Python identifier minone
    __minone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minone'), 'minone', '__httpexample_orgns_CTD_ANON_httpexample_orgnsminone', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 12, 16), 1, None, )

    
    minone = property(__minone.value, __minone.set, None, None)

    _ElementMap.update({
        __opt.name() : __opt,
        __req.name() : __req,
        __zeroton.name() : __zeroton,
        __oneton.name() : __oneton,
        __minzero.name() : __minzero,
        __minone.name() : __minone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


E1 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'E1'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 4, 4))
Namespace.addCategoryObject('elementBinding', E1.name().localName(), E1)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opt'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 7, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'req'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 8, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zeroton'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 9, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oneton'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 10, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minzero'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 11, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minone'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 12, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 7, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 9, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=1, max=3, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 10, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 11, 16))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opt')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'req')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zeroton')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 9, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oneton')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 10, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minzero')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 11, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minone')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/card.xsd', 12, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()


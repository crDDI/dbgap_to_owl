
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:69d40838-00bc-11e6-8eef-6c40088fdb3a')

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 16, 28)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ncbi.nlm.nih.gov/gap/mms#}MetaLink uses Python identifier MetaLink
    __MetaLink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetaLink'), 'MetaLink', '__httpncbi_nlm_nih_govgapmms_CTD_ANON_httpncbi_nlm_nih_govgapmmsMetaLink', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 8, 16), 0, None, )

    
    MetaLink = property(__MetaLink.value, __MetaLink.set, None, '\n                            Links a variable to a metavariable\n                        ')

    _ElementMap.update({
        __MetaLink.name() : __MetaLink
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
                            Links a variable to a metavariable
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 14, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute variableAccession uses Python identifier variableAccession
    __variableAccession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variableAccession'), 'variableAccession', '__httpncbi_nlm_nih_govgapmms_CTD_ANON__variableAccession', _module_typeBindings.STD_ANON)
    __variableAccession._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 15, 24)
    __variableAccession._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 15, 24)
    
    variableAccession = property(__variableAccession.value, __variableAccession.set, None, None)

    
    # Attribute metavariable_id uses Python identifier metavariable_id
    __metavariable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'metavariable_id'), 'metavariable_id', '__httpncbi_nlm_nih_govgapmms_CTD_ANON__metavariable_id', pyxb.binding.datatypes.int)
    __metavariable_id._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 20, 24)
    __metavariable_id._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 20, 24)
    
    metavariable_id = property(__metavariable_id.value, __metavariable_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __variableAccession.name() : __variableAccession,
        __metavariable_id.name() : __metavariable_id
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


MetaLinks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetaLinks'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', MetaLinks.name().localName(), MetaLinks)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetaLink'), CTD_ANON_, scope=CTD_ANON, documentation='\n                            Links a variable to a metavariable\n                        ', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 8, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 8, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetaLink')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/crDDI/dbgap_to_owl/tests/data/t3.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()


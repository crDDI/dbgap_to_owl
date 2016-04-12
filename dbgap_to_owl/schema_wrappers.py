# Copyright (c) 2016, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
from pyxb.binding.datatypes import anyType, anySimpleType
from pyxb.binding.facets import CF_enumeration
from rdflib import URIRef, Graph, RDF, RDFS, OWL, Namespace, Literal, BNode, XSD
from rdflib.collection import Collection
from typing import Union, Optional


from pyxb.binding.content import AttributeUse, ElementDeclaration
from pyxb.binding.basis import simpleTypeDefinition, complexTypeDefinition, element

from pyxb.namespace import ExpandedName

PREFIX = 'GAP'


BFO = Namespace("http://purl.obolibrary.org/obo/")
DCE = Namespace("http://purl.org/dc/elements/1.1/")
GAP = Namespace("http://ncbi.nlm.nih.gov/gap/mms#")
GAPI = Namespace("http://ncbi.nlm.nih.gov/gapi/mms#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
ISO = Namespace("http://metadata-standards.org/iso11179-3.owl#")
DC = Namespace("http://purl.org/dc/elements/1.1/")

namespaces = {'gap': GAP,
              'gapi': GAPI,
              'owl': OWL,
              'dc': DC,
              'skos': SKOS,
              'iso': ISO
              }


# Value documentation supplied by pyxb when annotation is not available
DEFAULT_ATT_DOC = 'Get the value of the attribute from the instance.'
ELEMENT_CT_DOC = 'Complex type [anonymous] with content type ELEMENT_ONLY'


def nsuri(n: ExpandedName) -> str:
    """ Return the string form of the namespace URI
    :param n: expanded name to be returned
    :return: stringified URI
    """
    # There appears to be a flaw in pyxb -- anyType comes from a different 'xsd' than int, string, etc
    rval = str(GAP['']) if not n.namespaceURI() else \
        str(XSD['']) if n.namespaceURI() == "http://www.w3.org/2001/XMLSchema" else str(n.namespaceURI())
    return rval     # two steps so a breakpoint works


def fulluri(n: ExpandedName) -> URIRef:
    """ Return the full uri of the expanded name
    :param n: expanded name
    :return: full URI
    """
    return URIRef(nsuri(n) + n.localName())


def add_cardinality(subj: Union[URIRef, BNode], obj: URIRef, min_: int, max_: Optional[str], g: Graph) -> None:
    """ Generate the appropriate OWL cardinality constraints for subj
    :param subj: the subject to be constrained
    :param obj: the URI of the target
    :param min_: minimum cardinality
    :param max_: maximum cardinality -- None means infinite
    :param g: Graph to add constraints to
    """
    if max_ is None:
        if min_ > 0:
            g.add((subj, OWL.minQualifiedCardinality, Literal(min_, datatype=XSD.nonNegativeInteger)))
        else:
            g.add((subj, OWL.allValuesFrom, obj))
    elif int(max_) == min_:
        g.add((subj, OWL.qualifiedCardinality, Literal(min_, datatype=XSD.nonNegativeInteger)))
    else:
        g.add((subj, OWL.maxQualifiedCardinality, Literal(int(max_), datatype=XSD.nonNegativeInteger)))
        if min_ > 0:
            g.add((subj, OWL.minQualifiedCardinality, Literal(min_, datatype=XSD.nonNegativeInteger)))


def make_graph(g: Optional[Graph]) -> Graph():

    if not g:
        g = Graph()
        for ns, uri in namespaces.items():
            g.bind(ns, uri)
        g.add((GAP[''], RDF.type, OWL.Ontology))
        g.add((GAP[''], OWL.versionIRI, URIRef("http://ncbi.nlm.nih.gov/gap/mms/v2.1.5")))
        # g.add((GAP[''], OWL.imports, URIRef("http://purl.obolibrary.org/obo/iao/2015-02-23/iao.owl")))
    return g


def add_labels(subj: URIRef, local_name: str, g: Graph) -> None:
    g.add((subj, SKOS.prefLabel, Literal(local_name)))
    g.add((subj, RDFS.label, Literal(PREFIX + ' ' + local_name)))


def proc_enum(dt: simpleTypeDefinition, scoping_uri: URIRef, nodeid: Union[URIRef, BNode], g: Graph) -> None:
    if dt != anySimpleType:
        individuals = []
        for e in dt._FacetMap().get(CF_enumeration, {}).values():
            enumid = URIRef(str(scoping_uri) + '_' + str(e))
            g.add((enumid, RDF.type, OWL.NamedIndividual))
            g.add((enumid, RDF.type, nodeid))
            g.add((enumid, OWL.hasValue, Literal(e)))
            individuals.append(enumid)
        if individuals:
            indlist = BNode()
            Collection(g, indlist, individuals)
            g.add((nodeid, OWL.oneOf, indlist))


def gap_i(gap_uri: URIRef) -> URIRef:
    return URIRef(str(gap_uri).replace('/mms/', '/mmsi/'))


class DataTypeWrapper:
    def __init__(self, dt: simpleTypeDefinition):
        self._dt = dt

    @property
    def uri(self):
        # The superType represents a constrained type
        return fulluri(self._dt._ExpandedName if self._dt._ExpandedName else self._dt.XsdSuperType()._ExpandedName)

    def as_rdf(self, g: Graph) -> Graph:
        g = make_graph(g)
        # TODO: Enumeration elements in
        # TODO: Other facets (pattern)
        if self._dt._ExpandedName and self._dt._ExpandedName.namespaceURI() != XSD[''][:-1]:
            SimpleTypeDefinition(self._dt, self._dt._ExpandedName).as_rdf(g)
        return g


class AttributeUseWrapper:
    def __init__(self, au: AttributeUse, container) -> None:
        """ Wrapper for AttributeUse type
        :param au: attribute to be wrapped
        :param container: container that references the attribute
        """
        self._au = au
        self._container = container

    def as_rdf(self, g: Optional[Graph] = None) -> Graph:
        g = make_graph(g)
        # Make the property as a combination of the container and the actual property name
        local_name = self._container.name.localName() + '_' + self._au.name().localName()
        att_uri = URIRef(nsuri(self._au.name()) + local_name)
        g.add((att_uri, RDF.type, OWL.DatatypeProperty))
        add_labels(att_uri, local_name, g)
        g.add((att_uri, RDFS.domain, fulluri(self._container.name)))
        dt = DataTypeWrapper(self._au.dataType())
        g.add((att_uri, RDFS.range, dt.uri))
        doc = self._container.doc_for(self._au.id())
        if doc and doc != DEFAULT_ATT_DOC:
            g.add((att_uri, DCE.description, Literal(doc)))

        # Add the Restriction BNode
        nodeid = BNode()
        g.add((nodeid, RDF.type, OWL.Restriction))
        g.add((nodeid, OWL.onProperty, att_uri))
        dt.as_rdf(g)
        g.add((nodeid, OWL.onDataRange,  dt.uri))
        add_cardinality(nodeid, dt.uri, 1 if self._au.required() else 0, "0" if self._au.prohibited() else "1", g)
        proc_enum(self._au.dataType(), att_uri, nodeid, g)
        g.add((self._container.uri, RDFS.subClassOf, nodeid))
        add_labels(self._container.uri, self._container.name.localName(), g)

        return g


class ElementDeclarationWrapper:
    def __init__(self, ed: ElementDeclaration, container) -> None:
        self._ed = ed
        self._container = container

    def as_rdf(self, g: Optional[Graph] = None) -> Graph:
        g = make_graph(g)
        binding = self._ed.elementBinding()
        td = binding.typeDefinition()
        local_name = self._container.name.localName() + '_' + self._ed.name().localName()
        ed_uri = URIRef(nsuri(self._ed.name()) + local_name)
        nodeid = BNode()

        if issubclass(td, simpleTypeDefinition):
            g.add((ed_uri, RDF.type, OWL.DatatypeProperty))
            obj = DataTypeWrapper(td).uri
            g.add((nodeid, OWL.onDataRange,  obj))
            proc_enum(td, ed_uri, nodeid, g)
        elif td == anyType:
            g.add((ed_uri, RDF.type, OWL.ObjectProperty))
            obj = OWL.Thing
            g.add((nodeid, OWL.onClass, obj))
            g.add((ed_uri, OWL.onProperty, obj))
        else:
            inner_name = td._ExpandedName if td._ExpandedName else binding.name()
            obj = fulluri(inner_name)
            g.add((nodeid, OWL.onClass, obj))
            g.add((ed_uri, RDF.type, OWL.ObjectProperty))
            ElementBindingWrapper(binding, inner_name).as_rdf(g)
        g.add((ed_uri, RDFS.domain, ed_uri))
        g.add((ed_uri, RDFS.range, obj))
        add_labels(ed_uri, local_name, g)
        doc = self._ed.elementBinding().documentation()
        if doc:
            g.add((ed_uri, DCE.description, Literal(doc.strip())))
        g.add((nodeid, RDF.type, OWL.Restriction))
        g.add((nodeid, OWL.onProperty, ed_uri))
        # This requires modifications to the PyXB package
        min_, max_ = self._ed.card()
        add_cardinality(nodeid, obj, min_, max_, g)
        g.add((self._container.uri, RDFS.subClassOf, nodeid))
        add_labels(self._container.uri, self._container.name.localName(), g)
        return g


class ElementBindingWrapper:
    def __init__(self, b: element, subj: ExpandedName) -> None:
        """ A binding that needs to be added as a base class
        :param b: reference binding
        :param subj: Name of container if anonymous
        """
        self._b = b
        self._subj = subj

    def as_rdf(self, g: Optional[Graph] = None) -> Graph:
        g = make_graph(g)
        td = self._b.typeDefinition()
        type_definition(td, td._ExpandedName if td._ExpandedName else self._subj).as_rdf(g)
        return g


class ElementWrapper:
    def __init__(self, el: element, name: Optional[ExpandedName] = None) -> None:
        """ An XML Schema ElementWrapper
        :param el: pyxb element definition
        :param name: reference name of element if not internal
        """
        self._el = el
        self.name = name if name else self._el.name()
        self.uri = fulluri(self.name)

    def as_rdf(self, g: Optional[Graph] = None) -> Graph:
        """ Emit the ElementWrapper as an OWL class
        :param g: graph to publish to
        :return: resulting graph
        """
        g = make_graph(g)
        g.add((self.uri, RDF.type, OWL.Class))
        add_labels(self.uri, self.name.localName(), g)
        if self._el.documentation():
            g.add((self.uri, DCE.description, Literal(self._el.documentation().strip())))
        if self._el.typeDefinition():
            type_definition(self._el.typeDefinition(), self.name).as_rdf(g)
        return g

    def as_iso(self, g: Optional[Graph] = None) -> Graph:
        g = make_graph(g)
        g.add((gap_i(self.uri), RDF.type, ISO.ObjectClass))


class SimpleTypeDefinition:
    def __init__(self, std: simpleTypeDefinition, def_name: ExpandedName) -> None:
        self._std = std
        self.name = def_name
        self.uri = fulluri(self.name)

    def as_rdf(self, g: Optional[Graph] = None) -> Graph:
        g = make_graph(g)
        if self._std.XsdSuperType():
            g.add((self.uri, RDF.type, OWL.Restriction))
            dt = DataTypeWrapper(self._std.XsdSuperType())
            g.add((self.uri, OWL.onDataRange, dt.uri))
            dt.as_rdf(g)
        else:
            g.add((self.uri, RDF.type, RDFS.Datatype))
        doc = self._std.__doc__.strip()
        if doc:
            g.add((self.uri, DCE.description, Literal(doc)))
        proc_enum(self._std, self.uri, self.uri, g)
        return g


class ComplexTypeDefinition:
    def __init__(self, ctd: complexTypeDefinition, def_name: ExpandedName) -> None:
        self._ctd = ctd
        self.name = def_name
        self.uri = fulluri(self.name)

    def doc_for(self, att_id: str) -> str:
        return self._ctd.__dict__[att_id].__doc__.strip()

    def as_rdf(self, g: Optional[Graph] = None) -> Graph:
        g = make_graph(g)
        if not self._ctd._ElementMap and not self._ctd._AttributeMap:
            g.add((self.uri, RDF.type, OWL.Class))
            doc = self._ctd.__doc__.strip()
            if doc:
                g.add((self.uri, DCE.description, Literal(doc)))
        for e in self._ctd._ElementMap.values():
            ElementDeclarationWrapper(e, self).as_rdf(g)
        for a in self._ctd._AttributeMap.values():
            AttributeUseWrapper(a, self).as_rdf(g)

        return g


def type_definition(type_def: Union[simpleTypeDefinition, complexTypeDefinition], def_name: ExpandedName) \
        -> Union[ComplexTypeDefinition, SimpleTypeDefinition]:
    return ComplexTypeDefinition(type_def, def_name) if issubclass(type_def, complexTypeDefinition) else\
        SimpleTypeDefinition(type_def, def_name)



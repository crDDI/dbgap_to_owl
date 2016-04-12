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
#     Neither the name of the Mayo Clinic nor the names of its contributors
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

# Test harness for dbgap XML Schema to OWL
import os
import pyxb.binding.generate
from pyxb.binding.basis import element
from rdflib.compare import isomorphic, graph_diff, to_canonical_graph
from rdflib import Graph
from typing import Union, List
from dbgap_to_owl.schema_wrappers import ElementWrapper


def gen_schema(test_name: str, output_python: bool=True) -> str:
    """ Generate an XML schema and return the resulting python code.  The code should be handled via "eval(rv)"
    :param test_name: name of test (without .xsd)
    :param output_python: If true, write resulting code to <test_name>.py
    :return: resulting compiled code. Must be evaluated in the GLOBAL namespace (!!!)
    """
    python_file = os.path.join('data', '%s.py' % test_name)
    code = pyxb.binding.generate.GeneratePython(schema_location=os.path.join('data', '%s.xsd' % test_name))
    if output_python:
        open(python_file, 'w').write(code)
    rv = compile(code, test_name, 'exec')
    return rv


def test_schema(element_name: Union[element, List[element]], ttl_file_name: str, test_ttl: bool=True,
                print_ttl: bool=False, print_diff=False) -> bool:
    """ Convert the compiled schema to RDF
    :param element_name: ElementWrapper name(s) to convert to RDF
    :param ttl_file_name: Name of RDF file (including .ttl). If test_ttl is false, this file is written, else read
    :param test_ttl: True means compare compiled schema to ttl file.  False means write ttl file
    :param print_ttl: True means print the ttl file to stdout.
    :param print_diff: True means print the difference if failure
    :return: True if test passed
    """
    if not isinstance(element_name, list):
        element_name = [element_name]
    g1 = ElementWrapper(element_name[0]).as_rdf()
    for e in element_name[1:]:
        ElementWrapper(e).as_rdf(g1)
    if print_ttl:
        print(g1.serialize(format='turtle').decode('utf-8'))
    if test_ttl:
        g2 = Graph().parse(os.path.join('data', ttl_file_name), format="turtle")
        return isomorphic(g1, g2) or eval_diffs(g1, g2, print_diff)

    else:
        open(os.path.join('data', ttl_file_name), 'w').write(g1.serialize(format='turtle').decode('utf-8'))
    return False


def eval_diffs(g1: Graph, g2: Graph, print_diff: bool) -> bool:
    """ Print the differences between to graphs on stdout
    :param g1: first graph
    :param g2: second graph
    :param print_diff: True means enable printing
    :return: constant False
    """
    if print_diff:
        _, in_g1, in_g2 = graph_diff(to_canonical_graph(g1), to_canonical_graph(g2))
        in_g1_ = [t for t in in_g1]
        in_g2_ = [t for t in in_g2]
        if in_g1_:
            print("Triples not in .ttl file:")
            print('\n\t'.join(["%s %s %s" % e for e in in_g1]))
        if in_g2_:
            print("Expected:")
            print('\n\t'.join(["%s %s %s" % e for e in in_g2]))
    return False


def comp_graphs(f1: Union[Graph, str], f2: Union[Graph, str], print_diff: bool) -> bool:
    """ Compare two graphs
    :param f1: graph 1 either as an rdflib Graph or a turtle string
    :param f2: graph 2 either as an rdflib Graph or a turtle string
    :param print_diff: True means say what is different, if any
    :return: True if graphs are identical, False if differences exist
    """
    g1 = f1 if isinstance(f1, Graph) else Graph().parse(source=f1, format="turtle")
    g2 = f2 if isinstance(f2, Graph) else Graph().parse(source=f2, format="turtle")
    return isomorphic(g1, g2) or eval_diffs(g1, g2, print_diff)

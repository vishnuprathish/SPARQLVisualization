#!/Users/vishnu/anaconda/bin/python
print "Content-type: text/html"
print
print "<html><head>"
print ""
#print "</head><body>"
print "Test Page"
#print "</body></html>"


print '<meta charset="utf-8" />'
print '<title>SPARQL QUERY Visualization</title>'

print '<script src="jquery.js"></script>'
print '<link href="css/ui-lightness/jquery-ui-1.10.3.custom.css" rel="stylesheet"/>'

print '<script src="js/jquery-1.9.1.js"></script>'
print '<script src="js/jquery-ui-1.10.3.custom.js"></script>'
#print "</body></html>"


print "</head>"

print '<script>  $(function() {    $( "#accordion" ).accordion();  });  </script>'


import rdflib
from rdflib import plugin
import matplotlib.pyplot as plt
import networkx as nx
import time

G=nx.Graph()


plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

g = rdflib.Graph()
#time.sleep(10)


# ... add some triples to g somehow ...
g.parse("web_foaf.rdf")


#qres = g.query(
#    """SELECT DISTINCT ?aname ?bname
#       WHERE {
#          ?a foaf:knows ?b .
#          ?a foaf:name ?aname .
#          ?b foaf:name ?bname .
#       }""")
#"""
       

qres = g.query(
    """CONSTRUCT { ?aname foaf:knows ?bname }
        WHERE {
          ?a foaf:knows ?b .
          ?a foaf:name ?aname .
          ?b foaf:name ?bname .
       }
       """)


for row in qres:
    #print("%s knows %s" % row)
    #print row[0] + " isFriendsWith " + row[2]
    #print (row)
    
    G.add_node(row[0])
    G.add_node(row[2])
    G.add_edge(row[0],row[2])
    
    

dfs_edges1 = [x for x in nx.dfs_edges(G)]



print '<body>'

print '<div id="accordion">'
for edge in dfs_edges1:
    print '<h3>' + "hello" + '</h3>'
    print '<div>'
    print '<p>'
    print "well , its well and good if I get here. Then will see"
    print '</p>'
    print '</div>'
    
print '</div>'

print "</body></html>"
